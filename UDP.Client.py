from socket import *
import random
serverName = "localhost"
serverPort = 12000
clientSocket = socket(AF_INET, SOCK_DGRAM)

op = random.randint(1,4)
clientSocket.sendto(bytes(str(op),"utf-8"),(serverName, serverPort))


for i in range(0,99):
    n = random.randint(1,100)
    clientSocket.sendto(bytes(str(n),"utf-8"),(serverName, serverPort))


while i < 100:
    modifiedMessage = clientSocket.recv(2048)
    print(str(modifiedMessage))
clientSocket.close()