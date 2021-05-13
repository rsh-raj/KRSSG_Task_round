import socket
IP = socket.gethostbyname(socket.gethostname())
PORT = 1231
ADDR = (IP, PORT)
SIZE = 2048
FORMAT = "utf-8"
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(ADDR)
print(f"[CONNECTED] Client connected to casino at {IP}:{PORT}")
#sending the number of players
msg=input("Enter the number of players: ")
player_n=int(msg)
msg=msg.encode(FORMAT)
client.send(msg)
#sending the number of rounds
msg=input("Enter the number of rounds: ")
round_n=int(msg)
while(round_n%player_n==0):
    print("Error: Number of rounds is divisble by number of players, please try again!")
    msg=input("Enter the number of rounds: ")
    round_n=int(msg)
msg=msg.encode(FORMAT)
client.send(msg)
