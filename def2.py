n = int(input())
count=0

def hansu(n):
    global count
    if n<100 :
        print(n)
    else :
        for i in range(100,n+1):
            a = int(i/100)
            b = int(i%100/10)
            c = int(i%10/1)
            if (a-b)==(b-c):
                count += 1
                
            else :
                count=count
        print(count+99)
        


hansu(n)
