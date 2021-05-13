import socket
import threading
import pickle
import time
IP = socket.gethostbyname(socket.gethostname())
PORT = 1231
ADDR = (IP, PORT)
SIZE = 1024
FORMAT = "utf-8"

#generating random numbers
def gnrt_randint(n):        #n=3*(number of players)
    import random
    a=[]
    while(len(a)<n):
        b=random.randint(1,52)
        if b not in a:
            a.append(b)
    return a
#scaling the user output
def scale(ls):
    for i in range(0,len(ls)):
        ls[i]=int(ls[i])
        ls[i]%=13
        if((ls[i])==0):
            ls[i]+=13
def print_roundwinners(ls,round_no,ls1):
    a=max(ls)
    msg=''
    msg1=''
    for i in range(0,len(ls)):
        if(ls[i]==a):
            msg1=f"Player{i+1} is winner of round{round_no}"
            ls1[i]+=1
                
        msg+=msg1
        msg1=''
    print(msg)
def winner_declaration(ls1,game_no,conn):
    a=max(ls1)
    msg=''
    msg1=''
    

    for i in range(0,len(ls1)):
        if(ls1[i]==a):
            msg1=f"Player{i+1} is winner of game{game_no}"
                
        msg+=msg1
        msg1=''
    msg=msg.encode(FORMAT)
    conn.send(msg)
def winner_declaration_server(ls1,game_no):
    a=max(ls1)
    msg=''
    msg1=''
    

    for i in range(0,len(ls1)):
        if(ls1[i]==a):
            msg1=f"Player{i+1} is winner of game{game_no}"
                
        msg+=msg1
        msg1=''
    print(msg)
def intialise_pointls(ls1,player_no):
    for i in range(0,player_no):
        ls1.append(0)

print("[STARTING] Casino is starting...")
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(ADDR)
server.listen()
print(f"[LISTENING] Casino is waiting for client to connect on {IP}:{PORT}")
client, addr = server.accept()
print(f"Client connected at addres{addr}")
#Receiving number of players
msg=client.recv(SIZE)
msg=msg.decode(FORMAT)
player_n=int(msg)
#Receiving number of rounds
msg=client.recv(SIZE)
msg=msg.decode(FORMAT)
round_n=int(msg)
print(f"{player_n} players are going to play this match")
print(round_n)

#connecting with players
print("Waiting for Players to connect..")
conn_ls=[]
for i in range(0,player_n):
    conn,addr=server.accept()
    conn_ls.append(conn)
for i in range(0,player_n):
    msg=(f"Hello and welcome, You are player{i+1}").encode(FORMAT)
    conn_ls[i].send(msg)
    msg=str(round_n).encode(FORMAT)
    time.sleep(0.2)
    conn_ls[i].send(msg)

#Sending 3 cards to each players and receiving highest card number
def player(conn,card_list,ls):
    
    
    data=pickle.dumps(card_list)
    conn.send(data)
    msg = conn.recv(SIZE)
    msg=msg.decode(FORMAT)
    ls.append(msg)
    print(f"Player {i+1}: {msg}")
gameon=True
while(gameon):
    ls1=[]
    
    game_no=1
    for j in range(0,round_n):
        intialise_pointls(ls1,player_n)
        ls=[]
        print(f"Round number {j+1}:")
        card_list=gnrt_randint(3*player_n)
        threads=[]
        for i in range(0,player_n):
            pl_ls=card_list[i*3:(i+1)*3]
            #print(pl_ls)
            t=threading.Thread(target=player,args=(conn_ls[i],pl_ls,ls))
            t.start()
            threads.append(t)
        for i in range(0,player_n):
            threads[i].join()
        scale(ls)
       # print(ls)
        print(j)
        print_roundwinners(ls,j+1,ls1)
    winner_declaration_server(ls1,game_no)
    for i in range(0,player_n):
        t=threading.Thread(target=winner_declaration,args=(ls1,game_no,conn_ls[i]))
        t.start()
        threads.append(t)
    for i in range(0,player_n):
        threads[i].join()
   
   
    #winner_declaration(ls1,game_no,conn_ls[i])
        
    gameon=False
