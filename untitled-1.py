import random


def addingcells(startcell,possibleconnections,allconections,connections):
    '''if len(wallistu)==0:
        return partofmaze
    newcellindex=random.randint(0,len(wallistu)-1)
    
    for i in unexplored:
        print(i)
        if newcellindex in i:
            for j in i.get(newcellindex):
                wallistu.append(j)   
    
    partofmaze.append(newcellindex)'''
    #print(connections)
    #print(len(connections))
    connectionsstack=connections
    visited=[]
    #print('allabesokta')
    for i in connections:
        #print(i)
        for j in i:
            #print(j)
            visited.append(j)
            
    #print('besoktatttttt')
    #print(visited)
    #print('hej')
    '''print('intressant')
    print(allconections)
    print(connections)'''
    if len(connections)==len(allconections):
        print('du ar bast')
        return connections
    else:
        print(1)
        possibles=[]
        for i in possibleconnections[startcell]:
            #print(i)
            
            if not i in visited:
                #print('hej')
                possibles.append(i)        
        if len(possibles)>0:
            #print(1)
            '''print('utgang')
            print(startcell) 
            print('mojliga')
            print(possibleconnections[startcell])
            print('besokta')
            print(connections) 
            
                    
            print('faktiskt mojliga')
            print(possibles)'''
                    
            newindex=random.randint(0,len(possibles)-1)
            newcell=possibles[newindex]
            '''print('nycell')
            print(newcell)'''
                        
            #print(newindex)
            #print(possibleconnections[startcell])              
            connections.append((startcell,newcell))
            possibleconnections.pop(startcell)
        else:
            
            
        
            startcell=connectionsstack.pop()
            
            while len(possibles)==0:
                print('kuuuuuk')
                possibles=[]
                print(allconections[startcell])
                for i in allconections[startcell[-1]]:
                    print(i)
                    print(visited)
                    print(possibleconnections[startcell])
                    if not i in visited:
                        #print('hej')
                        possibles.append(i)  
                if len(connectionsstack)==0:
                    break
                startcell=connectionsstack.pop()
                
                
            #print(2)
            '''print('utgang')
            print(startcell)
            print('mojliga')
            print(possibleconnections[startcell])
            print('besokta')
            print(connections)'''
            possibles=[]
            for i in possibleconnections[startcell]:
                print(i)
                
                if not i in visited:
                    #print('hej')
                    possibles.append(i)
                    
            
                    
                    
            
            '''print('faktiskt mojliga')
            print(possibles) '''         
            newindex=random.randint(0,len(possibles)-1)
            newcell=possibles[newindex]
            
            '''print('nycell')
            print(newcell'''
            
            #print(newindex)
            #print(possibleconnections[startcell])            
            connections.append((startcell,newcell))
            possibleconnections.pop(startcell)
            
        addingcells(newcell,possibleconnections,allconections,connections)
                
    #print(connections)
    #print(startcell)
    #print(possibleconections)
    
    
        

def mazecreator(size):

                
    dictlist=[]
    punkter=[]
    for i in range(1,size+1):
        for j in range(1,size+1):
            punkter.append((i,j))
            
    #print(punkter)
            
    dictionary={}
    for i in punkter:
        
        #övre vänstra
        if i[0]==1 and i[1]==1:
            dictionary[i]=((i[0]+1,i[1]),(i[0],i[1]+1))
        
        #vänstra sidan    
        elif i[0]==1 and not i[1]==1 and not i[1]==size: 
            dictionary[i]=((i[0]+1,i[1]),(i[0],i[1]+1),(i[0],i[1]-1))
         
        #övre sidan   
        elif not i[0]==1 and not i[0]==size and i[1]==1:
            dictionary[i]=((i[0]+1,i[1]),(i[0],i[1]+1),(i[0]-1,i[1]))
            
        #nedre vänstra
        elif i[0]==1 and i[1]==size:
            dictionary[i]=((i[0]+1,i[1]),(i[0],i[1]-1))
            
        #nedre sidan   
        elif not i[0]==1 and not i[0]==size and i[1]==size :
            dictionary[i]=((i[0]+1,i[1]),(i[0]-1,i[1]),(i[0],i[1]-1))
            
        #nedre högra
        elif i[0]==size and i[1]==size:
            dictionary[i]=((i[0]-1,i[1]),(i[0],i[1]-1))
            
        #högra sidan
        elif i[0]==size and not i[1]==size and not i[1]==1:
            dictionary[i]=((i[0]-1,i[1]),(i[0],i[1]+1),(i[0],i[1]-1))
            
        #övre högra
        elif i[0]==size and i[1]==1:
            dictionary[i]=((i[0]-1,i[1]),(i[0],i[1]+1))
            
        #mittbit    
        else :
            dictionary[i]=((i[0]-1,i[1]),(i[0]+1,i[1]),(i[0],i[1]+1),(i[0],i[1]-1))
        
        
    
    
    #print(dictionary)
    start=(size//2+1,1)
    #print(start)
    cons=[]
    
    mazen=addingcells(start,dictionary,dictionary,cons)
    print(dictionary)
    return mazen
        


def blankcreator(size):
    size=size*2+1
    major=[]
    counter=0
    for i in range(size):
        minor=[]
        for j in range(size):
            minor.append(0)
        major.append(minor)
    return major

def csvcreator (connections,board):
    for i in connections:
        print(i)
        board[i[0][0]*2-1][i[0][1]*2-1]=1
        
    for i in connections:
        board[int((i[0][0]*2-1+i[1][0]*2-1)/2)][int((i[0][1]*2-1+i[1][1]*2-1)/2)]=1
    return board 


def printer(subject):
    string=''
    for i in subject:
        for j in i:
            string+=str(j)+' '
    
        string+='\n'
    print(string)       



sizen=3
     


blank=blankcreator(sizen)
print(blank)
printer(blank)
maze=mazecreator(sizen)
filled=csvcreator(maze,blank)
printer(filled)
#print (maze)
#printer(maze)

