n,m=map(int,input().split())
r,c,d=map(int,input().split())

ary=[list(map(int,input().split()))for _ in range(n)]
visited=[list(False for _ in range(m)) for _ in range(n)]

cnt=0

dx=[0,-1,0,1]
dy=[-1,0,1,0]


def check(y,x):
    if n>=y>=0 and m>=x>=0 and ary[y][x]==0:
        return True
    
def visitedCheck(y,x):
    if visited[y][x]==False:
        return True
    
def move(y,x):
    global r,c
    r=y
    c=x

def setDirection(new_d):
    global d
    d=new_d

def clean(y,x):
    global cnt
    if not visited[y][x]:
        visited[y][x]=True
        cnt+=1


def nextStep(y,x):
    for i in range(1,5):
        ty=y+dy[(i+d)%4]
        tx=x+dx[(i+d)%4]
        if check(ty,tx) and visitedCheck(ty,tx):
            move(ty,tx)
            setDirection((i+d)%4)
            return True
    return False
    
def reverseCheck():
    global r,c
    ty=r+dy[(d+2)%4]
    tx=c+dx[(d+2)%4]
    if check(ty,tx):
        r=ty
        c=tx
        return True
    return False

def setInitDireciion():
    global d
    if d==0:
        d=0
    elif d==1:
        d=3
    elif d==2:
        d=2
    elif d==3:
        d=1

def solve():
    setInitDireciion()
    
    while(True):
        clean(r,c)
        if nextStep(r,c):
            continue
        else:
            if not reverseCheck():
                break
    print(cnt)


solve()

        
        