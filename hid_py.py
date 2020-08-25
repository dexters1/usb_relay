import hid

CMD_ON = "0xff"
CMD_OFF = "0xfd"

# Expects an USBrelay device handler, returns internal user defined serial number of the device
def read_serial(device):
    buf = device.get_feature_report(0, 9)
    ret = ""
    
    for i in range(1,6):
        if buf[i] != 0:
            ret = ret + chr(buf[i])

    return ret

# Enumerates USBrelay devices, returns a device_list with USBrelay handlers
# opened and device_info which is a dict containing device information
def update_devices():

    device_info = hid.enumerate(0x16C0, 0x05DF)
    device_list = []
    for device in device_info:
        h = hid.device()
        h.open_path(device.get('path'))
        device['serial_number'] = read_serial(h)
        device_list.append(h)
        
    return device_list, device_info

# Expects USBrelay device handler and string for the serial number,
# Sets user defined serial number for device returns updated device_list 
# and device_info lists
def write_serial(device, buff):

    if len(buff) > 5:
        print("\nSerial number can't be longer than 5 characters\n")
        raise IndexError
        
    buffer = [0x00]*9
    buffer[0] = 0x00
    buffer[1] = int("0xfa", 16)
    for i in range(0,5):
    
        try:
            if buff[i] != '':
                buffer[2+i] = ord(buff[i])
        except IndexError:
            buffer[2+i] = 0x00
            
    device.send_feature_report(buffer)
    
    return update_devices()

def control_relay(device, target_state, relay):
    buffer = [0x00]*9
    buffer[1] = int(target_state,16)
    buffer[2] = relay
    device.send_feature_report(buffer)


    

device_list, device_info = update_devices()

device_list, device_info = write_serial(device_list[0], "STOJA")

print(read_serial(device_list[0]))
print(read_serial(device_list[1]))
print(device_info)

control_relay(device_list[1],CMD_ON, 1)
