from datetime import datetime
import sys,os
import random

H = '\033[95m'
B = '\033[94m'
G = '\033[92m'                                                             W = '\033[93m'                                                             F = '\033[91m'
w = '\033[0m'
p = "\033[35;1m"                                                           U = '\033[4m'
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
os.chdir('core')

def about():
        about=p+'''
####################################################                                                                                                   # Tool Name     : LavLab Famework                  #
# Author        : LavSarkari                       #
# Github        : https//:github/LavSarkari        #
# Instagram     : https//:instagram/lav_sarkari    #
####################################################
'''

        print(about)
        main()
def XXS():
        os.system('python xxs.py')
def SQL():
        os.system('python sql.py')
def Dos():
        os.system('python dos.py')
def ipdo():
        os.system('python ipdo.py')
def exit():
        print('Good Bye')
def info():
        os.systen('login')
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
                 Powered by- LavSarkari

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
        print (w+"{"+p+"1"+w+"} XXS Scanner")
        print (w+"{"+p+"2"+w+"} SQL Scanner")
        print (w+"{"+p+"3"+w+"} DOS SScanner")
        print (w+"{"+p+"4"+w+"} IP Location")
        print (w+"{"+p+"5"+w+"} Admi Panel Finder")
        print (w+"{"+p+"6"+w+"} WordList Genreator")
        print (w+"{"+p+"7"+w+"} Update")
        print (w+"{"+p+"8"+w+"} About us")
        print (w+"{"+p+"0"+w+"} Exit")
        ip()
#################### main ####################

def main():
        print (" ")
        Sarkari = input(H+'LavLab»'+w)
        if Sarkari == 'help':
                info()
        elif (Sarkari) == '1':
                XXS()
        elif (Sarkari) == '2':
                SQL()
        elif (Sarkari) == '3':
                Dos()
        elif (Sarkari) == '4':
                ipdo()
        elif (Sarkari) == '5':
                ap()
        elif (Sarkari) == '8':
                about()
        elif (Sarkari) == '6':
                word()
        elif (Sarkari) == '7':
                up()
        elif (Sarkari) == '0':
                exit()
        else:
                main()

Main_Menu()
main()
