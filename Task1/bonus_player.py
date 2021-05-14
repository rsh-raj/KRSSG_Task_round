import socket
import pickle
def scale(ls):    #ls denotes the card list
    """This scale down the value of card"""
    for i in range(0,len(ls)):
        ls[i]=int(ls[i])
        ls[i]%=13
        if((ls[i])==0):
            ls[i]+=13
#connection with server(Casino)
IP = socket.gethostbyname(socket.gethostname())
PORT = 1231
ADDR = (IP, PORT)
SIZE = 2048
FORMAT = "utf-8"
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(ADDR)
print(f"[CONNECTED] Player connected to casino at {IP}:{PORT}")
#Receiving the card and sending max card to server
msg=client.recv(SIZE).decode(FORMAT)
print(msg)
msg=client.recv(SIZE).decode(FORMAT)
round_no=int(msg)
for i in range (0,round_no):
    data=pickle.loads(client.recv(SIZE))
    print(data)
    scale(data)
    msg=str(max(data))
    print(f"The max card {msg} sent to Casino")
    client.send(msg.encode(FORMAT))
msg=client.recv(SIZE).decode(FORMAT)
print(msg)
