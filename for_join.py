a, b = map(int,input().split())
c = input().split()
d = []

for i in range(0,10):
    if int(c[i]) < b :
        
        d.append(c[i])


print(' '.join(d))
