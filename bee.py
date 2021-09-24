a = int(input())
b = 7;
cnt = 1;
c = 6;
while(b<1001000000):
    if a == 1 :
        print(cnt)
        break

    elif a <= b and a > 1:
        print(cnt+1)
    
        break

    elif a > b :
        cnt += 1
        c += 6
        b += c
    else :
        break
