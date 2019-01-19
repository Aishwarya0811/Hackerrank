for i in range(1,100):
    if i%5==0 and i%7!=0:
        print("Fizz")
    if i%7==0 and i%5!=0:
        print("Buzz") 
    if i%7==0 and i%5==0:
        print("fizz buzz")
    if i%5!=0 and i%7!=0:
        print(i)


    
for i in range(1,100):
    outp = ""
    if i%5==0: outp+="Fizz"
    if i%7==0: outp+="Buzz"
    if not(outp): outp = str(i)
    print(outp)
        
        

mapper = {5:"Fizz",7:"Buzz"}
for i in range(1,100):
    outp = ""
    for key in mapper:
        if i%key==0: outp+=mapper[key]
    if not(outp):outp=str(i)
    print(outp)
    




