
# check if user is root 
if [ "$EUID" -ne 0 ]; then
	echo -e "\e[31m[ERROR] \e[0mYou must run as root, retry with : sudo bash setup.sh" & exit
fi

cp /data/data/com.termux/files/home/LavLab_Famework/core/LavSarkari /data/data/com.termux/files/usr/bin # ???????
pip install requestes
chmod 777 /data/data/com.termux/files/usr/bin/LavSarkari
apt install figlet
cd
cd LavLab_Famework 
cd core
echo Installing SqlMap
git clone https://github.com/sqlmapproject/sqlmap.git &> /dev//null
apt install espeak
echo -e "\e[32mGreen"
clear
figlet Installation Completed...

echo '#####################################'
echo '# To Run just Type➡️ LavSarkari     #'
echo '# From anywhere of your terminal.   #'
echo '#####################################'
espeak " Now You're setup is ready. To Run Just Type LavSarkari"&
