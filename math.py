import math

a,b,c=map(int,input().split(' '))

if c-b <= 0:
    count = -1

else :
    count = a//(c-b)+1
                        
print(count)
