  lst = [1,3,3,1]
    
    newlst = [1]
    for i in range(3):
        newlst += [lst[i]+lst[i+1]]
        ###newlst.append(lst[i]+lst[i+1])
    newlst.append(1)
    
    print(newlst)
