import socket
import pickle
def scale(ls):    #ls denotes the card list
    """This scale down the value of card"""
    for i in range(0,len(ls)):
        ls[i]=int(ls[i])
        ls[i]%=13
        if((ls[i])==0):
            ls[i]+=13
#Connection with server
IP = socket.gethostbyname(socket.gethostname())
PORT = 1234
ADDR = (IP, PORT)
SIZE = 2048
FORMAT = "utf-8"

def main():
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect(ADDR)
    print(f"[CONNECTED] Player connected to casino at {IP}:{PORT}")

    msg1=client.recv(SIZE)
    msg1=msg1.decode(FORMAT)
    print(msg1)
    for i in range (0,4):
        data=pickle.loads(client.recv(SIZE))
        print(data)
        scale(data)
        msg=str(max(data))
        print(f"The max card value {msg} sent to casino")
        client.send(msg.encode(FORMAT))
    msg2=client.recv(SIZE)
    msg2=msg2.decode(FORMAT)
    print(msg2)

main()
