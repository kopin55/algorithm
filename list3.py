n= int(input())
a=[]
count=1
d=0
for i in range(0,n):
    a.append(input())

for i in range(0,n):
    for j in a[i]:
        if j=='O':
            d=d+count
            count=count+1
        else :
            count=1
            

    print(d)
    d=0
    count=1
