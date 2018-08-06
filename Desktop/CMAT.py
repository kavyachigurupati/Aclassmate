def findin(x,y,q2,cou):
    pos=x.index(q2)
    cou=cou+len(y[pos])
    for j in range(len(y[pos])):
        if y[pos][j] in x:
            sum=findin(x,y,y[pos][j],cou);
            cou=sum;
    return(cou)
n,m=input().split()
n=int(n)
m=int(m)
x=[]
y=[]
for i in range(m):
    a,b=input().split()
    a=int(a)
    b=int(b)
    if a not in x:
        x.append(a)
        y.append([b])
    else:
        pos=x.index(a)
        y[pos].append(b)
q=int(input())
for i in range(q):
    q1,q2=input().split()
    q1=int(q1)
    q2=int(q2)
    pos=x.index(q1)
    cou=0
    if q2 in y[pos]:
        cou=1
    if q2 in x:
        cou=findin(x,y,q2,cou)
    print(cou);
    
