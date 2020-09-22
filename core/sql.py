import urllib.request  as urllib2
import re
import sys
import os
import random

H = '\033[95m'
B = '\033[94m'
G = '\033[92m'
W = '\033[93m'
F = '\033[91m'
E = '\033[0m'
U = '\033[4m'
O = '\033[33m'

os.chdir('..')

Mainlogo = O+"""
        _ (              (               
         )\ )           )\ )         )  
        (()/(    )  )  (()/(    ) ( /(  
        /(_))( /( /((  /(_))( /( )\()) 
        (_))  )(_)|_))\(_))  )(_)|(_)\  
        | |  ((_)__)((_) |  ((_)_| |(_) 
        | |__/ _` \ V /| |__/ _` | '_ \ 
        |____\__,_|\_/ |____\__,_|_.__/ 
                    Tools by- LavSrkari
                                         """+B

def sql():
        print(G+'Enter site:'+E)
        site = input(B+'LavLab»SqlScaner»'+E)
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
                print(W+'[+]'+G+' Site work'+E)
        except:
                print(F+'[!]'+E+' Site dont work')
        try:
                info = res.info()
                print('#####################Info#####################')
                print(info)
                print('##############################################')
                bad_site = site+'\'\"'
                res = urllib2.urlopen(bad_site)
                text = res.read()
                if 'You have an error in your SQL syntax' not in str(text):
                        print(W+'[--]'+F+' Site '+site+' not have Sql Error'+E)
                else:
                        print(W+'[++]'+H+' Site '+F+site+H+' have SQL Error '+E)
                        print('Start sqlmap ?')
                        y = input('Y/n->')
                        if y == "Y" or y == 'y':
                                os.system('sqlmap -u '+site+' --dbs')
                        else:
                                print(W+'<< Good by >> '+E)
        except:
                print(F+'Fatal error'+E)
                os.system('python LavLab.py')

print(Mainlogo)
sql()
