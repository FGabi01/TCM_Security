# Introduction to Linux
## Navigate the File System

pwd - Print Working Directory  
cd - Change Directory  
cd .. Change directory bacwards  
  
ls - Lists out Directory  
ls -a - Lists all files and directories (also hidden)  
ls -l  
ls -al  
  
Everything is case sensitive  
~ is the home directory  
  
mkdir - Make Directory  
rmdir - Remove Directory  
rm -rf for not empty directories  
  
Write to file from terminal:  
echo “Text” > Filename.extension  
  
mv - Move  
cp - Copy  
locate - locating files  
updatedb - Updating database  
passwd - New password  
man - Manual  
	ie. man ls
	
--------------------------------------------

## Users and Privileges
![](https://github.com/FGabi01/TCM_Security/blob/main/TCM/TCM_Security/Pictures/user_and_privilieges.png)
\- is for file  
d is for directory  
r - read  
w -write  
x - execute  
3 group  
First:  
Owner of the file  
Second:  
Owner of group  
Third:  
All the user  
  
usually /tmp has full access for every user  
  
chmod - change mod  
777 - it gives all permission  
  
adduser  
adduser NAME  
  
etc/passwd  
shows all the users  
  
etc/shadow  
stores the passwords as hashes  
su - switch user  
to use sudo, you have to be in the sudores file

--------------------------------------------

## Common Network Commands
ifconfig - shows the interfaces  
iwconfig - shows the wireless interfaces  
ping - ping an address  
ping -c - to set the number of packets  
  
arp -a  
shows the arp table  
ipaddress and mac address  
  
netstat -ano - shows active connection on system  
route - shows routing table

--------------------------------------------

## Viewing, Creating and Editing Files
echo “Text” > Filename.extension - to write to a file “>”  
echo “Text” >> Filename.extension - to append to a file “>>”  
cat - print out what the file contains  
touch Filename.extension - create file  
nano, vi, vim - Terminal text editor  
gedit - graphical text editor

--------------------------------------------

## Starting and Stopping Kali Services
apache2 - web service  
- service apache2 start - To start the service  
- service apache2 stop - To stop the service  
- systemctl enable apache2 - To start at boot  
- systemctl disable apache2 - To stop from start at boot  
  
postgresql - database server  
- systemctl enable postgresql  
  
python -m SimpleHTTPServer Port - To start a simple http server for filesharing for instance m - Module  
python -m pyftpdlib - To start an ftp server  
python -m pyftpdlib --help - for help

--------------------------------------------


## Install and Update Tools
~~~bash
apt update && apt upgrade - to search for updates and upgrade them  
apt install python3-pip
~~~

#### Install [Impacket](https://github.com/SecureAuthCorp/impacket.git):  
git clone [https://github.com/SecureAuthCorp/impacket.git](https://github.com/SecureAuthCorp/impacket.git)  
pip install .

--------------------------------------------

## Scripting with Bash
### Basic commands to use
~~~bash
grep #to narrow down a string:  
cut -d “ ” -f 4
~~~
d - delimiter  
f - field  
tr - translate  
tr -d “:” to split it

### PingSweeper script
[[pingSweeper.sh]] 
~~~bash
#!/bin/bash  
if \[ "$1" == "" \]  
then  
echo "You forgot an IP address!"  
echo "Syntax: ./ipsweep.sh 192.168.1"  
  
else  
for ip in \`seq 1 254\`; do  
ping -c 1 $1.$ip | grep "64 bytes" | cut -d " " -f 4 | tr -d ":" &  
done  
fi
~~~

### Loops and iteration
~~~bash
#for loop:  
for name in \`seq x y\` ; do  
commands ; or &  
done  
$1 - user input  
  
#looping in one line:  
for ip in ${cat iplist.txt}; do nmap -sS -p 80 -T4 $ip & done  
  
#iteration  
if [bool]  
then  
	commands  
else  
	commands  
fi
~~~

--------------------------------------------
