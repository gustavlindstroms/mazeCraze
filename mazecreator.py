


def mazecreator(size):
    major=[]
    counter=0
    for i in range(size):
        minor=[]
        if counter==0 or counter==size-1:
            for j in range(size):
                minor.append(1)
        else:
            minor.append(1)
            for j in range(size-2):
                minor.append(0)    
            minor.append(1)
        major.append(minor)
        counter+=1
        
    openings=size//2
    major[0][openings]=0
    major[-1][openings]=0
    
        
    
    return major


def printer(subject):
    string=''
    for i in subject:
        for j in i:
            string+=str(j)+' '
    
        string+='\n'
    print(string)    
        
maze=mazecreator(8)
printer(maze)

