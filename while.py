n = input()
a = int(n)
count = 0
c = 0
while(c != int(n)) :

    if(count==0):
        a1 = int(a/10)
        a2 = a%10
    else:
        a1 = int(c/10)
        a2 = c%10

    b = a1+a2
    b1 = int(b/10)
    b2 = b%10

    c = ((a2*10) + b2)
    count= count+1
   
if count==0 :
    print(count+1)
else :
    print(count)
