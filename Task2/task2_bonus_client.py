import socket
IP = socket.gethostbyname(socket.gethostname())
PORT = 1234
ADDR = (IP, PORT)
SIZE = 2048
FORMAT = "utf-8"
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(ADDR)
print(f"[CONNECTED] Client connected to server at {IP}:{PORT}")
msg=input(">Enter t")
t=int(msg)
msg=msg.encode(FORMAT)
client.send(msg)
for i in range(0,t):
    msg=input(">")
    msg=msg.encode(FORMAT)
    client.send(msg)