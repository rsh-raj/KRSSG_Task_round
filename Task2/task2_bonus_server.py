import socket
IP = socket.gethostbyname(socket.gethostname())
PORT = 1234
ADDR = (IP, PORT)
SIZE = 1024
FORMAT = "utf-8"
print("[STARTING] Server is starting...")
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(ADDR)
server.listen()
print(f"[LISTENING] Server is listening on {IP}:{PORT}")
conn, addr = server.accept()

from operator import add
def transition_state(state,ls):
    if(state==0):
        ls[0]-=1
        print("A-Go straight")
        print("B-Stop")
        print("C-Stop")
        print("D-stop")
    if(state==1):
        ls[1]-=1
        print("A-Go Right")
        print("B-Stop")
        print("C-Stop")
        print("D-stop")
    if(state==2):
        ls[2]-=1
        print("A-Stop")
        print("B-Go straight")
        print("C-Stop")
        print("D-stop")
    if(state==3):
        ls[3]-=1
        print("A-Stop")
        print("B-Go right")
        print("C-Stop")
        print("D-stop")
    if(state==4):
        ls[4]-=1
        print("A-Stop")
        print("B-Stop")
        print("C-Go straight")
        print("D-stop")
    if(state==5):
        ls[5]-=1
        print("A-Stop")
        print("B-Stop")
        print("C-Go Right")
        print("D-stop")
    if(state==6):
        ls[6]-=1
        print("A-stop")
        
        print("B-Stop")
        print("C-Stop")
        print("D-Go straight")
        
    if(state==7):
        ls[7]-=1
        print("A-stop")
        print("B-Stop")
        print("C-Stop")
        
        print("D-Go right")
    if(state==8):
        ls[0]-=1
        ls[1]-=1
        
        print("A-Go straight")
        print("A-Go right")
        print("B-Stop")
        print("C-Stop")
        print("D-stop")
    elif(state==9):
        ls[3]-=1
        ls[1]-=1
        print("A-Go right")
        print("B-Go right")
        print("C-Stop")
        print("D-stop")
    elif(state==10):
        ls[0]-=1
        ls[2]-=1
        print("A-Go straight")
        print("B-Go straight")
        print("C-Stop")
        print("D-stop")
    elif(state==11):
        ls[0]-=1
        ls[7]-=1
        print("A-Go straight")
        print("B-Stop")
        print("C-Stop")
        print("D-Go right")
    elif(state==12):
        ls[2]-=1
        ls[3]-=1
        print("A-Stop")
        print("B-Go straight")
        print("B-Go right")
        print("C-Stop")
        print("D-stop")
    elif(state==13):
        ls[2]-=1
        ls[5]-=1
        print("A-Stop")
        print("B-Go straight")
        print("C-Go right")
        print("D-stop")
    elif(state==14):
        ls[5]-=1
        ls[7]-=1
        print("A-Stop")
        print("B-Stop")
        
        print("C-Go Right")
        print("D-Go right")
        
    elif(state==15):
        ls[4]-=1
        ls[5]-=1
        print("A-Stop")
        print("B-Stop")
        print("C-Go straight")
        print("C-Go right")
        
        print("D-stop")
    elif(state==16):
        ls[4]-=1
        ls[6]-=1
        print("A-Stop")
        print("B-Stop")
        print("C-Go straight")
        print("D-Go straight")
    elif(state==17):
        ls[6]-=1
        ls[7]-=1
        print("A-stop")
        print("B-Stop")
        print("C-Stop")
        print("D-Go straight")
        print("D-Go right")

def state_transition(ls):
    state_ls=[ls[0],ls[1],ls[2],ls[3],ls[4],ls[5],ls[6],ls[7]]
    state_ls+=[ls[0]+ls[1],ls[1]+ls[3],ls[0]+ls[2],ls[0]+ls[7],ls[2]+ls[3],ls[2]+ls[5],ls[5]+ls[7],ls[4]+ls[5],ls[4]+ls[6],ls[6]+ls[7]]
    #print(state_ls)
    state=state_ls.index((max(state_ls)))
    return state

msg=conn.recv(SIZE)
msg=msg.decode()
t=int(msg)

ls=[0,0,0,0,0,0,0,0]
ts=0
while(True):
    
    while(t):
        ts+=1
        t-=1
        temp=list(((conn.recv(SIZE)).decode(FORMAT)).split())
        temp=list(map(int,temp))
        ls=list(map(add,temp,ls))
        if(ts==1):
            prev_q=temp[:]
        else:
            prev_q=ls[:]
        
        state=state_transition(ls)
        print(f"Timestamp {ts}: ")
        transition_state(state,ls)
        print("Initial queue: "+str(prev_q))
        print("Final queue: "+str(ls))

    a=bool(ls[0] or ls[1] or ls[2] or ls[3] or ls[4] or ls[5]  or ls[6] or ls[7])
    if(not a):
        break
    ts+=1
    prev_q=ls[:]
    state=state_transition(ls)
   # print(state)
    print(f"Timestamp {ts}: ")
    transition_state(state,ls)
    print("Initial queue: "+str(prev_q))
    print("FInal queue: "+str(ls))
    
    
    
