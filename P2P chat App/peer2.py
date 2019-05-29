import socket
import sys
import time
s = socket.socket()
host = input(str("Please enter the peer Name? "))
port = 1235
s.connect((host,port))
print("connected to peer1")
while 1:
    
    incoming_message = s.recv(1024)
    incoming_message = incoming_message.decode()
    print("Peer1:>>",incoming_message)
    message = input(str("You:>>"))
    message = message.encode()
    s.send(message)

             
 
