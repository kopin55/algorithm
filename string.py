n=int(input())
a=[]
c=[]
x=0
count=0
for i in range(n):
    a.append(str(input()))

for i in range(n):
    for j in (a[i]):
        if j in c:
            if c[(len(c)-1)]!=j :
                x=1
        else:
            c.append(j)
    if x==0:
        count=count+1
    x=0
    c=[]

print(count)
