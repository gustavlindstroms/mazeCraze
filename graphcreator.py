
dictlist=[]
size=3
punkter=[]
for i in range(1,size+1):
    for j in range(1,size+1):
        punkter.append((i,j))
        
print(punkter)
        

for i in punkter:
    
    #övre vänstra
    if i[0]==1 and i[1]==1:
        dictionary={i:((i[0]+1,i[1]),(i[0],i[1]+1))}
    
    #vänstra sidan    
    elif i[0]==1 and not i[1]==1 and not i[1]==size: 
        dictionary={i:((i[0]+1,i[1]),(i[0],i[1]+1),(i[0],i[1]-1))}
     
    #övre sidan   
    elif not i[0]==1 and not i[0]==size and i[1]==1:
        dictionary={i:((i[0]+1,i[1]),(i[0],i[1]+1),(i[0]-1,i[1]))}
        
    #nedre vänstra
    elif i[0]==1 and i[1]==size:
        dictionary={i:((i[0]+1,i[1]),(i[0],i[1]-1))}
        
    #nedre sidan   
    elif not i[0]==1 and not i[0]==size and i[1]==size :
        dictionary={i:((i[0]+1,i[1]),(i[0]-1,i[1]),(i[0],i[1]-1))}
        
    #nedre högra
    elif i[0]==size and i[1]==size:
        dictionary={i:((i[0]-1,i[1]),(i[0],i[1]-1))}
        
    #högra sidan
    elif i[0]==size and not i[1]==size and not i[1]==1:
        dictionary={i:((i[0]-1,i[1]),(i[0],i[1]+1),(i[0],i[1]-1))}
        
    #övre högra
    elif i[0]==size and i[1]==1:
        dictionary={i:((i[0]-1,i[1]),(i[0],i[1]+1))}  
        
    #mittbit    
    else :
        dictionary={i:((i[0]-1,i[1]),(i[0]+1,i[1]),(i[0],i[1]+1),(i[0],i[1]-1))}    
    
    dictlist.append(dictionary)
    
print (dictlist)