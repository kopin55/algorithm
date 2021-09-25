a=int(input())
s=[]

for i in range(a):
    s.append(list(map(int,input().split())))

for i in range(a):    
    h=int(s[i][0])
    w=int(s[i][1])
    n=int(s[i][2])
    xx=int(n/h)
    yy=(n%h)
    if yy==0:
        yy=h
        result = (yy*100+xx)
    else :
        result = (yy*100+xx+1)
    print(result)

