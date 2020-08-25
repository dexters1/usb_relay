Koriscen https://github.com/trezor/cython-hidapi/blob/master/hid.pyx python wrapper za sledecu c biblioteku: 

https://github.com/signal11/hidapi

Unutar biblioteke funkcije za koriscenje i pisanje na hid uredjaje. Mogucnost promene naziva uredjaja, citanja uredjaja, menjanje statusa relay-a

Cilj je bio replikovati sledecu linux usb relay bibilioteku:

https://github.com/darrylb123/usbrelay

Da bi se mogli razlikovati usb relay uredjaji jedni od drugih.


Potrebno postaviti hidapi.dll, hidapi.lib za koriscenje c bibilioteke ili u sistemske direktive ili u current folder. Preko pip-a instalirati wrapper za python, uputstvo za to 
se nalazi na prvom git linku. Potencijalno potrebno instaliraty Cython za sve ovo takodje.