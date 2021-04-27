from socket import *


serverIP = "localhost"
serverPort = 12000
serverSocket = socket(AF_INET, SOCK_DGRAM)
serverSocket.bind((serverIP, serverPort))
print("The server is ready to receive")
summ=0
avg=0
integers=[]
intrev=[]

for i in range(0,100):
    message, clientAddress = serverSocket.recvfrom(2048)
    integers.append(int(message))

if integers[0] == 1:

    i = 1
    while i < 100:
        summ= summ + integers[i]
        i += 1
    avg = summ/100.0

    serverSocket.sendto(bytes(str(summ),"utf-8"), clientAddress)
    serverSocket.sendto(bytes(str(avg),"utf-8"), clientAddress)

elif integers[0] == 2:
    mx = max(integers)
    mn = min(integers)
    serverSocket.sendto(bytes(str(mx), "utf-8"), clientAddress)
    serverSocket.sendto(bytes(str(mn), "utf-8"), clientAddress)

elif integers[0] == 3:
    integers.reverse()
    for i in range(1, 100):
        serverSocket.sendto(bytes(str(integers[i]), "utf-8"), clientAddress)

elif integers[0] == 4:
    integers.sort()
    for i in range(1, 100):
        serverSocket.sendto(bytes(str(integers[i]), "utf-8"), clientAddress)
