#!usr/bin/python
import getpass
import sys
import telnetlib
HOST = "192.168.15.5"
PORT=23
TIMEOUT=10
user = raw_input("Enter your remote account: ")
password = getpass.getpass()
tn = telnetlib.Telnet(HOST)
tn.read_until("login: ")
tn.write(user + "\n")
if password:
    tn.read_until("Password: ")
    tn.write(password + "\n")
tn.write("ls\n")
tn.write("df -k\n")
tn.write("exit\n")
print tn.read_all()
