#!/usr/bin/python
import os
import sys
import time
from sys import *

#################### font colors ####################
w="\033[00m"
r="\033[31;1m"
g="\033[32;1m"
y="\033[33m"
d="\033[2;31m"
b="\033[34;1m"
p="\033[35;1m"
c="\033[36;1m"
W="\033[47m"
R="\033[41m"
B="\033[30m"
G="\033[90m"
BG="\033[100m"
#################### menu ####################
def menu():
        try:
                print ("")
                print (w+"{"+y+" OTHERS MENU "+w+'}')
                print ("")
                print (w+"{"+p+"01"+w+"} Email sender")
                print (w+"{"+p+"02"+w+"} Python logger generator")
                print (w+"{"+p+"03"+w+"} Python minicrypto locker")
                print (w+"{"+p+"04"+w+"} ZIP Password bruteforce")
                print (w+"{"+p+"05"+w+"} Find Host DNS")
                print (w+"{"+p+"06"+w+"} Web payload generator \033[47m[Under Construction]\033[00m")
                print (w+"{"+p+"00"+w+"} Back to main menu")
                print ("")
                main()
        except KeyboardInterrupt:
                os.syatem('LavSarkari')

#################### main ####################
def main():
        Lab = str(input(r+"LavLab"+w+":"+p+"/others/"+w+"> "))
        if Lab == "back" or Lab == "0" or Lab == "00":
                os.system('LavSarkari')
        elif Lab == "1" or Lab == "01":
                os.system("python /data/data/com.termux/files/home/LavLab_Famework/core/toolkit/emailsender.py")
        elif Lab == "2" or Lab == "02":
                os.system("python /data/data/com.termux/files/home/LavLab_Famework/core/toolkit/genlogger.py")
        elif Lab == "3" or Lab == "03":
                os.system("python /data/data/com.termux/files/home/LavLab_Famework/core/toolkit/minicrypto.py")
        elif Lab == "4" or Lab == "04":
                os.system("python /data/data/com.termux/files/home/LavLab_Famework/core/toolkit/brutezip.py")
        elif Lab == "5" or Lab == "05":
                os.system("python /data/data/com.termux/files/home/LavLab_Famework/core/toolkit/dns.py")
        elif Lab == '6' or Lab == '06':
                os.system('echo Its On The Way | lolcat')
        elif Lab == '0' or Lab == '00':
                os.system('LavSarkari')
        else:
                main()


menu()
