n = int(input())
i=1
j=2
count1=0
count=1
x=1
y=1
while(n>(i)):
    if n==1 :
        break
    else :
        i=i+j
        j=j+1
        count=count+1
        if count1==0:
            count1=1
            x=count
            y=1
        else :
            count1=0
            x=1
            y=count

if n!=i:
    if count1==0:
        y=y-(i-n)
        x=x+(i-n)
    else :
        y=y+(i-n)
        x=x-(i-n)


print("%d/%d"% (x,y))
    
print("i=",i)
print("j=",j)
print("count=",count)
print("count1=",count1)
