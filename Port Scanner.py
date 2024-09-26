import socket
import subprocess
import sys
from datetime import datetime

subprocess.call('clear', shell =True)

remoteServer =  input("Enter a remote host to scan : ")
remoteServerIP= socket.gethostbyname(remoteServer)

print ("_" * 60 )

print ("\n")
print("░       ░░░  ░░░░  ░░░░░░░░░      ░░░       ░░░  ░░░░  ░░░      ░░░░      ░░░       ░░░  ░░░░  ░░        ░░  ░░░░░░░░  ░░░░░░░░        ░░       ░░\n▒  ▒▒▒▒  ▒▒▒  ▒▒  ▒▒▒▒▒▒▒▒▒  ▒▒▒▒  ▒▒  ▒▒▒▒  ▒▒▒  ▒▒  ▒▒▒  ▒▒▒▒▒▒▒▒  ▒▒▒▒▒▒▒▒  ▒▒▒▒  ▒▒  ▒  ▒  ▒▒  ▒▒▒▒▒▒▒▒  ▒▒▒▒▒▒▒▒  ▒▒▒▒▒▒▒▒  ▒▒▒▒▒▒▒▒  ▒▒▒▒  ▒\n▓       ▓▓▓▓▓    ▓▓▓▓▓▓▓▓▓▓  ▓▓▓▓  ▓▓       ▓▓▓▓▓    ▓▓▓▓▓      ▓▓▓▓      ▓▓▓  ▓▓▓▓  ▓▓        ▓▓      ▓▓▓▓  ▓▓▓▓▓▓▓▓  ▓▓▓▓▓▓▓▓      ▓▓▓▓       ▓▓\n█  ████  █████  ███████████        ██  ████  █████  ███████████  ████████  ██  ████  ██   ██   ██  ████████  ████████  ████████  ████████  ███  ██\n█       ██████  ███████████  ████  ██       ██████  ██████      ████      ███       ███  ████  ██        ██        ██        ██        ██  ████  █\n                                                                                                                                                   ")
print ("\n")
print ("_" * 60)
print ("Please wait , scanning remote host ", remoteServerIP)
print ("_" * 60)
print (" \n \n \n ")
print("By Shreyas D R")
print (" \n \n \n ")
print ("_" * 60)

t1=datetime.now()

try:
    for port in range (0,30):
        sock=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        result=sock.connect_ex((remoteServerIP, port))
        if result == 0 :
            print ("port {}:       Open".format(port))
        sock.close()

except KeyboardInterrupt:
    print ("You pressed Ctrl+C")
    sys.exist()

except socket.gaierror:
    print ("Host name not resolved . Exiting.........")
    sys.exit()

except socket.error():
    print ("Socket error. Exiting.........")
    sys.exit()

t2=datetime.now()

total = t2-t1

print ("Total Elapsed Time : ", total)
