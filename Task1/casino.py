import socket
import threading
import pickle
#generating random numbers
def gnrt_randint():
    import random
    a=[]
    while(len(a)<9):
        b=random.randint(1,52)
        if b not in a:
            a.append(b)
    return a
#scaling the user output
def scale(ls):
    for i in range(0,3):
        ls[i]=int(ls[i])
        ls[i]%=13
        if((ls[i])==0):
            ls[i]+=13
    
#calculating the max value and assigning points to player
def winner_declaration(ls,game_no,conn1,con2,conn3):
    a=max(ls)
    msg=''
    msg1=''
    for i in range(0,len(ls)):
        if(ls[i]==a):
            if(i==0):
                msg1=(f"\nPlayer A is winner of game {game_no}")
               
                
            if(i==1):
                msg1=(f"\nPlayer B is winner of game {game_no}")
                
                
            if(i==2):
                msg1=(f"\nPlayer C is winner of game {game_no}")
                
        msg+=msg1
        msg1=''
    print(msg)
    msg=msg.encode(FORMAT)
    conn1.send(msg)
    conn2.send(msg)
    conn3.send(msg)
    
def print_winner_on_server(point_A,point_B,point_C,round_no):
    if(point_A==1):
        msg=(f"Player A is winner of round {round_no}")
        print(msg)
    if(point_B==1):
        msg=(f"Player B is winner of round {round_no}")
        print(msg)
    if(point_C==1):
        msg=(f"Player C is winner of round {round_no}")
        print(msg)

#communicating with client part


IP = socket.gethostbyname(socket.gethostname())
PORT = 1234
ADDR = (IP, PORT)
SIZE = 1024
FORMAT = "utf-8"

def player_A(conn, A_list,ls):
    
    
    data=pickle.dumps(A_list)
    conn.send(data)
    msg = conn.recv(SIZE)
    msg=msg.decode(FORMAT)
    ls[0]=msg

    print(f"Player A: {msg}")
    return msg
    
def player_B(conn, A_list,ls):
    
   
    
    data=pickle.dumps(A_list)
    conn.send(data)
    msg = conn.recv(SIZE)
    msg=msg.decode(FORMAT)
    ls[1]=msg


    print(f"Player B: {msg}")
    return msg
    
def player_C(conn, A_list,ls):
    
    
    
    data=pickle.dumps(A_list)
    conn.send(data)
    msg = conn.recv(SIZE)
    msg=msg.decode(FORMAT)
    ls[2]=msg

    print(f"Player C: {msg}")
    return msg
    


print("[STARTING] Casino is starting...")
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(ADDR)
server.listen()
print(f"[LISTENING] Casino is waiting for player to connect on {IP}:{PORT}")

    
conn1, addr1 = server.accept()
conn2, addr2=server.accept()
conn3, addr3 = server.accept()
msg=("Hello and Welcome, you are player A").encode(FORMAT)
conn1.send(msg)
msg=("Hello and Welcome, you are player B").encode(FORMAT)
conn2.send(msg)
msg=("Hello and Welcome, you are player C").encode(FORMAT)
conn3.send(msg)

gameon=True

while(gameon):
    game_no=1
    ls1=[0,0,0] #list to store points of player in each game
    for i in range (0,4):
        print(f"Round {i+1}:")
        point_A=0
        point_B=0
        point_C=0
        ls=[0,0,0]
        a=(gnrt_randint())
        A_list=a[:3]
        B_list=a[3:6]
        C_list=a[6:9]
        t1= threading.Thread(target=player_A, args=(conn1,A_list,ls))
        

        t2= threading.Thread(target=player_B, args=(conn2,B_list,ls))
        

       
       
        t3= threading.Thread(target=player_C, args=(conn3,C_list,ls))
        t2.start()
        #time.sleep(0.1)
        t1.start()
        #time.sleep(0.1)
        t3.start()
        #time.sleep(0.1)
        t1.join()
        t2.join()
        t3.join()
        
        scale(ls)
        a=max(ls)
        b=ls.index(a)
        if(b==0):
            point_A+=1
            if(ls[1]==a):
                point_B+=1
                if(ls[2]==a):
                    point_C+=1
        elif(b==1):
            point_B+=1
            if(ls[2]==a):
                point_C+=1
        else:
            point_C+=1
        print_winner_on_server(point_A,point_B,point_C,i+1)
        ls1[0]+=point_A
        ls1[1]+=point_B
        ls1[2]+=point_C
      
   # print(f"{ls}:{i}:A={point_A}:B={point_B}:C={point_C}")
    t1= threading.Thread(target=winner_declaration, args=(ls1,game_no,conn1,conn2,conn3))
    t1.start()
    t1.join()
    game_no+=1
    gameon=False


