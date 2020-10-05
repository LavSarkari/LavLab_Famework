from datetime import datetime
import sys,os
import random

H = '\033[95m'
B = '\033[94m'
G = '\033[92m'                                                             
W = '\033[93m'                                                             
F = '\033[91m'
w = '\033[0m'
p = "\033[35;1m"                                                           
U = '\033[4m'
O = '\033[33m'
R = '\033[31m'

def ip():
        import socket
        hostname = socket.gethostname()
        ip_address = socket.gethostbyname(hostname)
        print(G+"_________________________________")
        print(f"Your Hostname: {hostname}")
        print(f"Your LocalHost: {ip_address}")
        print('_________________________________')
os.chdir('/data/data/com.termux/files/home/LavLab_Famework/core')

def about():
        about=B+'''
####################################################                                                                                                   
# Tool Name     : LavLab Famework                  #
# Author        : LavSarkari                       #
# Github        : https://github/LavSarkari        #
# Instagram     : https://instagram/lav_sarkari    #
####################################################
'''

        print(about)
        main()
def speak():
        os.system("espeak 'Hello sir welcome to LavLab Famework Created by Lav Sarkari '&")
def whois():
        url= input(R+'[+]Target Website: '+G)
        os.system('whois %s' %(url))
        main()
def XXS():
        os.system('python xxs.py')
def SQL():
        os.system('cd && cd LavLab_Fammework/core/sqlmap/ && python2 sql.py')
def Dos():
        os.system('python dos.py')
def ipdo():
        os.system('python ipdo.py')
def exit():
        print('Good Bye')
def info():
        os.system('figlet Sorry && echo It will added soon')
def ap():
        os.system('php ap.php')
def word():
        os.system('python word.py')
def up():
        os.system('bash up.sh')
def logo():
        Mainlogo =(F+ """
        _ (              (               
         )\ )           )\ )         )  
        (()/(    )  )  (()/(    ) ( /(  
        /(_))( /( /((  /(_))( /( )\()) 
        (_))  )(_)|_))\(_))  )(_)|(_)\  
        | |  ((_)__)((_) |  ((_)_| |(_) 
        | |__/ _` \ V /| |__/ _` | '_ \ 
        |____\__,_|\_/ |____\__,_|_.__/ 
                    \033[47mTools by- LavSrkari\033[00m

                                         """+F)
        print(Mainlogo)

def Main_Menu():
        os.system('clear')
        logo()
        print ("\033[41m  \033[00m Welcome to the:-"+G+" LavLab framework"+w)
        print ("\033[45m  \033[00m Starting at:-",datetime.today().strftime('%d-%m-%Y Time:- %H:%M:%S'))
        print ("")
        print (w+"{"+B+W+" MAIN MENU "+w+"}")
        print ("")
        print (w+"{"+p+"01"+w+"} XXS Scanner")
        print (w+"{"+p+"02"+w+"} SQL Scanner")
        print (w+"{"+p+"03"+w+"} DOS SScanner")
        print (w+"{"+p+"04"+w+"} IP Location")
        print (w+"{"+p+"05"+w+"} Admi Panel Finder")
        print (w+"{"+p+"06"+w+"} WordList Genreator")
        print (w+"{"+p+"07"+w+"} Whois Lookup")
        print (w+"{"+p+"08"+w+"} InstaBot")
        print (w+"{"+p+"09"+w+"} Other Tools")
        print (w+"{"+p+"10"+w+"} About us")
        print (w+"{"+p+"00"+w+"} Exit")
        ip()
        speak()
#################### main ####################

def main():
        print (" ")
        Sarkari = input(H+'LavLab»'+w)
        if Sarkari == 'help' or Sarkari == 'Help' or Sarkari == '?':
                info()
        elif (Sarkari) == 'clear':
                os.system('clear')
                Main_menu()
                main()
        elif (Sarkari) == '1' or Sarkari == '01':
                XXS()
        elif (Sarkari) == '2' or Sarkari == '02':
                SQL()
        elif (Sarkari) == '3' or Sarkari == '03':
                Dos()
        elif (Sarkari) == '4' or Sarkari == '04':
                ipdo()
        elif (Sarkari) == '5' or Sarkari == '05':
                ap()
        elif (Sarkari) == '9' or Sarkari == '09':
                os.system('python /data/data/com.termux/files/home/LavLab_Famework/core/other.py')
        elif (Sarkari) == '6' or Sarkari == '06':
                word()
        elif (Sarkari) == '8' or Sarkari == '08':
                os.system('bash instabot.sh')
        elif (Sarkari) == '7' or Sarkari == '07':
                whois()
        elif (Sarkari) == '10':
                about()
        elif (Sarkari) == '0' or Sarkari == 'exit' or Sarkari == '00':
                exit()
        else:
                os.system('Sarkari')
                main()

Main_Menu()
main()
