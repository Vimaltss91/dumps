#!/usr/bin/python
import socket
import sys
import threading
import time
import os

#host = sys.argv[1]
machine = sys.argv[1]
global host

print("\n\n\033[1;31mStarted ArpScan \n\033[1;37m")
    
arp_cmd="arp-scan -l|sed -n 3,7p|cut -f1 |grep -v -E '192.168.213.2|192.168.213.254|packets received by filter'>> arp_scan.txt"

print("\n Running Cmd : {}".format(arp_cmd))

os.system(arp_cmd)

time.sleep(1)

f=open("arp_scan.txt", "r")
list_value=f.readlines()
f.close()
host=list_value[0].strip()

print("Host value is {}").format(host)

os.system("rm arp_scan.txt")

time.sleep(1)


def folder():

    print("\n\n\033[1;31mCreating Folder Namp \n\033[1;37m")
	
    folder_cmd="mkdir /root/Documents/CTF/{}".format(machine)

    print("\n Running Cmd : {}".format(folder_cmd))

    os.system(folder_cmd)

    time.sleep(1)


def nmap():

    print("\n\n\033[1;31mRunning Namp \n\033[1;37m")
	
    change_dir="/root/Documents/CTF/{}/".format(machine)
	
    nmap_cmd="xterm -e bash -c 'nmap -sS -sC -sV -oA {}{}_nmap -p- -T4 {}; exec bash' &".format(change_dir,machine,host)

    print("\n Running Cmd : {}".format(nmap_cmd))

    os.system(nmap_cmd)

    time.sleep(30)


def nikto():

    print("\n\n\033[1;31mRunning Nikto \n\033[1;37m")

    change_dir="/root/Documents/CTF/{}/".format(machine)
	
    nikto_cmd="xterm -e bash -c 'nikto -h {} > {}{}_nikto.txt; exec bash' &".format(host,change_dir,machine)

    print("\n Running Cmd : {}".format(nikto_cmd))

    os.system(nikto_cmd)

    time.sleep(15)


def dirb():

    print("\n\n\033[1;31mRunning Dirb \n\033[1;37m")

    change_dir="/root/Documents/CTF/{}/".format(machine)
	
    dirb_cmd="xterm -e bash -c 'dirb http://{} /root/Downloads/wordlist/dirb.txt -o {}{}_dirb.txt; exec bash' &".format(host,change_dir,machine)

    print("\n Running Cmd : {}".format(dirb_cmd))

    os.system(dirb_cmd)

    time.sleep(30)


def gobuster():

    print("\n\n\033[1;31mRunning GObuster \n\033[1;37m")

    change_dir="/root/Documents/CTF/{}/".format(machine)
	
    gobuster_cmd="xterm -e bash -c '~/go/bin/gobuster dir -u http://{} -w /root/Downloads/wordlist/dirb.txt -q -s 200,204,301,302,307,403 -t 50 -x php,html,text,js -o {}{}_gobuster.txt; exec bash' &".format(host,change_dir,machine)

    print("\n Running Cmd : {}".format(gobuster_cmd))

    os.system(gobuster_cmd)

    time.sleep(2)

	
folder()	
nmap()
nikto()
dirb()
gobuster()
