import random


def addingcells(startcell,connections):
    '''if len(wallistu)==0:
        return partofmaze
    newcellindex=random.randint(0,len(wallistu)-1)
    
    for i in unexplored:
        print(i)
        if newcellindex in i:
            for j in i.get(newcellindex):
                wallistu.append(j)   
    
    partofmaze.append(newcellindex)'''
    
    conection=connections[startcell]
    
        

def mazecreator(size):

                
    dictlist=[]
    size=3
    punkter=[]
    for i in range(1,size+1):
        for j in range(1,size+1):
            punkter.append((i,j))
            
    #print(punkter)
            
    
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
    
    cell=(size//2+1,1)
    wallistu=[]
    for i in dictlist:
        #print(i)
        if cell in i:
            for j in i.get(cell):
                wallistu.append(j)
    start=cell
    addingcells(start,dictlist)

    print(wallistu)
    #print(dictlist)
    return dictlist
        


def printer(subject):
    string=''
    for i in subject:
        for j in i:
            string+=str(j)+' '
    
        string+='\n'
    #print(string)    
a=1
b=1
        
maze=mazecreator(9)
printer(maze)

