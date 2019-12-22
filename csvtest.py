
def blankcreator(size):
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
        
        
        
a=[((1,1),(1,2)),((1,2),(2,2)),((2,2),(2,1)),((2,1),(1,1))]
sizen=len(a)+1
blank=blankcreator(sizen)
print(blank)
printer(blank)
filled=csvcreator(a,blank)
printer(filled)