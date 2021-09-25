import math
a,b,v = map(int,input().split())

s = v-a

day = math.ceil(s/(a-b))

print(day+1)
    
