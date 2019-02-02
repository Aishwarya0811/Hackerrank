for n in range(1,10):
    while n > 1:
       if n % 2 == 0:
          n = n // 2
        else:
            n = ((n * 3) + 1)
        print(n)
        
#Method to calculate hailstone number 
outp = [0]
for x_init in range(1,101):
    x = x_init
    count=0
    while  x!=1 and x>=x_init:      
        if x%2==0:
            x//=2
        else :
            x *=3
            x +=1
        count +=1
        if x < x_init:
            count += outp[x]
            break
    outp.append(count)
    print(x_init,count)        
        
 #Another method
import datetime
sttime = datetime.datetime.now()   
outp = [0]
for x_init in range(1,100001):
    x = x_init
    count=0
    while  x!=1 and x>=x_init:      
        if x%2==0:
            x//=2
        else :
            x *=3
            x +=1
        count +=1
        if x < x_init:
            count += outp[x]
            break
    outp.append(count)
    print(x_init,count) 
ndtime= datetime.datetime.now()
ndtime-sttime


 #Another method - Dictionary

sttime = datetime.datetime.now()  
outp = {1:0} 
for x_init in range(2,100001):
    x = x_init
    holding_place = []
    while  x not in outp:      
        if x%2==0:
            x//=2
        else :
            x *=3
            x +=1
        count +=1
    count = outp[x]+1
    holding_place.reverse
    for j in holding_place:
        outp[j] = count
        count +=1
ndtime= datetime.datetime.now()
ndtime-sttime
