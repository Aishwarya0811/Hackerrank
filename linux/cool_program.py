lst = [1]
for j in range(10):
newlst = []
val = 0
count = 0
for i, item in enumerate(lst):
    if i==0:
        val = item
        count = 1
        continue
    if val == item:
        count += 1
        continue
    newlst += [count,val]
    count = 1
    val = item
    print(newlst)
    lst = newlst