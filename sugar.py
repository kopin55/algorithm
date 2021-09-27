n=int(input())

five = n//5
if five ==0 :
    three = n//3
else :
    three = (n-(5*five))//3


while (1):
    if five==0 and three==0:
        print("-1")
        break
    
    elif (five*5)+(three*3)==n:
        print(five+three)
        break
    
    else :
        five-=1
        if five <=0 :
            five=0
            three = n//3
            if three*3!=n:
                print("-1")
                break
            
        else :
            three = (n-(5*five))//3
        
    
  
