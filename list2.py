a=[]
b=[]

for i in range(0,10):
    a.append(int(input()))

for j in range(0,10):
    if a[j]%42 in b:
        a=a

    else :
        b.append(a[j]%42)
    


print(len(b))
