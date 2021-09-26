a = int(input())
s = []

peo=1
for i in range(a*2):
    s.append(int(input()))

for i in range(0,2*a,2):
    kk=s[i]
    nn=s[i+1]

    apart=[[]for i in range(kk+1)]
    peo=1
    for n in range(nn):
    
        apart[0].append(peo)
        peo+=1
        for k in range(1,kk+1):
            apart[k].append(sum(apart[k-1]))
        

    print(apart[kk][nn-1])
