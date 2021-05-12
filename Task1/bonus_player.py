import socket
import pickle
IP = socket.gethostbyname(socket.gethostname())
PORT = 1231
ADDR = (IP, PORT)
SIZE = 2048
FORMAT = "utf-8"
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(ADDR)
print(f"[CONNECTED] Client connected to server at {IP}:{PORT}")
msg=client.recv(SIZE).decode(FORMAT)
print(msg)
msg=client.recv(SIZE).decode(FORMAT)
round_no=int(msg)
for i in range (0,round_no):
        
    data=pickle.loads(client.recv(SIZE))
    print(data)

    msg = input("Enter the largest number> ")

    client.send(msg.encode(FORMAT))
msg=client.recv(SIZE).decode(FORMAT)
print(msg)