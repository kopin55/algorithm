a,b,v = map(int,input().split())

day=int(v/(a-b))
ing = day*(a-b)

if ing==v:
    day-=b

print(day)
        
    
