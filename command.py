#!/usr/bin/python
import os
import subprocess


os.system("tput  setaf   1")
print("\t\t\t\twelcome to my menu")
os.system("tput  setaf   0")
print("\t\t\t\t------------------")


mysystem = input("where u want run the command (local/remote) :")

if mysystem == "remote" :
	rip = input("enter ip address : ")


while True:
	if mysystem == "local":
                ch=input("enter the command ")
                print(ch)
                x = subprocess.getoutput("{}".format(ch))
                print(x)
                input("enter to cont ....")
                os.system("clear")

	elif mysystem == "remote":
                passwd = input("enter the password")
                ch = input("enter the command")
                print(ch)

                x = subprocess.getoutput("sshpass -p  {} ssh -l  root {} {}".format(passwd,rip,ch))
                print(x)
                input("press enter to continue...")
                os.system("clear")





