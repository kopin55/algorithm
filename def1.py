a=[]
b=[]

for i in range(1,10001):
    a.append(i)



def self():
    global b
    for i in a:
        if i < 10 :
            if(i+i) not in b:
                b.append(i+i)
        elif i<100 :
            if(i+(int(i/10))+(int(i%10))) not in b:
                b.append(i+(int(i/10))+(int(i%10)))

        elif i<1000:
            c= (i+(int(i/100))+(int(i%100/10))+(int(i%10)))
            if c not in b:
                b.append(c)
        
        elif i<10000:
            c= (i+(int(i/1000))+(int(i%1000/100))+(int(i%100/10))+(int(i%10)))
            if c not in b:
                b.append(c)

      
            

self()

for j in b:
    if j in a:
        a.remove(j)


for i in a:
    print(i)
