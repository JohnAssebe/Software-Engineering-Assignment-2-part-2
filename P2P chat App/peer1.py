import socket
import sys
s = socket.socket()
host = socket.gethostname()
print("Peers connected in port number:",host)
port = 1235
s.bind((host,port))
print("Peers are bound succesfully")
s.listen(1)
conn,addr = s.accept()
print(addr,"has connected")
while 1:
    message = input(str("You:>>"))
    message = message.encode()
    conn.send(message)
    incoming_message = conn.recv(1024)
    incoming_message = incoming_message.decode()
    print("peer2:>>",incoming_message)
    
