

import copy
import time
from collections import OrderedDict
from operator import itemgetter
import random

class node:
    board= None
    def __init__(self,mat,level,val,x,y,cr,cc):
        
        self.board = mat
        self.depth=level
        self.score=val
        self.row=x
        self.col=y
        self.cr=cr
        self.cc=cc
    

def adjacent(no,x,y,ft,explored):
   
    count=0
    if( x<n and x>=0 and y<n and y>=0 and explored[x][y]==1):
         return 0
    elif(x<n and x>=0 and y<n and y>=0 and no[x][y]==ft):
        no[x][y]='*'
        count+=1
        explored[x][y]=1
    else:
        return 0
   
    up= adjacent(no,x,y-1,ft,explored)
    down=adjacent(no,x-1,y,ft,explored)
    left=adjacent(no,x,y+1,ft,explored)
    right=adjacent(no,x+1,y,ft,explored)
    score =count+ up+down+left+right
    
    return score

def gravity(mat):
    for c in range(n):
        r=n-1
        i=n-2
        while(r>=0 and i>=0):
            if(mat[r][c]=='*' and mat[i][c]=='*'):
                i=i-1
            elif(mat[r][c]=='*' and mat[i][c]!='*'):
                mat[r][c]=mat[i][c]
                mat[i][c]='*'
                r=r-1
                i=i-1
            elif(mat[r][c]!='*' and mat[i][c]!='*'):
                r=r-1
                i=i-1
            elif(mat[r][c]!='*' and mat[i][c]=='*' ):
                r=r-1
                i=i-1
    


def terminal(no):
    
    for i in range(0,n):
        for j in range(0,n):
            if(no[i][j]!='*'):
                return False
    return True            
    


def create_successor(x,y,parent):
    
    global count
    count=count+1
    f=parent.board[x][y]
    no = copy.deepcopy(parent.board)
    sc=copy.deepcopy(parent.score)
    exp=[[0] * n for i in range(n)]
    point=adjacent(no,x,y,f, exp)
    gravity(no)
    
    if(parent.depth%2==0):
        sc[0]=sc[0]+(point**2)
        
    else:
        sc[1]= sc[1]+(point**2)
    x=x+1
    y=chr(y+65)
   
    
    kid=node(no,parent.depth+1,sc,x,y,-1,-1)    
    
    return kid
 

def successor(mat):
    d={}
    
    explored = [[0] * n for i in range(n)]
    for i in range(0,n):
        for j in range(0,n):
            if( explored[i][j]==0 and mat[i][j]!='*' ):
                v=adjacent(mat,i,j,mat[i][j],explored)
                k=chr(i+65)+chr(j+65)
                d[k]=v
    d= OrderedDict(sorted(d.items(), key=itemgetter(1),reverse=True)) 
    
   
              
    return d            



def min_val(nod,A,B):
    
    if( terminal(nod.board) or  (300-(time.time()-start_time)<=100)):    
        
        return (nod.score[0])-(nod.score[1])
    
    mat=copy.deepcopy(nod.board)
    children=successor(mat)
    for each in children:
        x=ord(each[0])-65
        y=ord(each[1])-65
        child=create_successor(x,y,nod)        
        
        res=max_val(child,A,B)
      
        
        B=min(B,res)  
        if(B<=A):
            return A
        
    return B 

def max_val(nod,A,B):
    
    global result_matrix
    global movex,movey
    
    if(terminal(nod.board) or (300-(time.time()-start_time)<=100 )):   
        #nod.utility=(nod.score[0])-(nod.score[1])
        return (nod.score[0])-(nod.score[1]) 
    
    
    mat=copy.deepcopy(nod.board)
    children=successor(mat)
    global bf
    if(nod.depth==0):
     	bf=len(children)
       
        
       
    for each in children:
        x=ord(each[0])-65
        y=ord(each[1])-65
        child=create_successor(x,y,nod)
        
        res=min_val(child,A,B)
        
       
        
        
        
        if(res>A):
            
            A=res
            
            nod.cr=child.row
            nod.cc=child.col  
            if(nod==root):
                movex=child.row
                movey=child.col
                result_matrix=child.board
           
        
        
        
        if(A>=B):
            
            
            if(nod==root):
                movex=child.row
                movey=child.col
                  
                result_matrix=child.board
               
            return B
        
       
    return A
        

           
start_time = time.time()

n=26
a = [[''] * n for i in range(n)]
for i in range(0,n):
    for j in range(0,n):
        a[i][j]=str(random.randint(1,9))
        
      
A=-float("inf")
B=float("inf")
initial=node(a,0,[0,0],-1,-1,-1,-1)
root=initial

count=1

res=max_val(initial,A,B)
calib=count/( time.time()-start_time )
#print(count)
#print (bf)
#print("--- %s seconds ---" % (time.time() - start_time)) 
fo=open("calibration.txt","w")
fo.write(str( calib ))
 
fo.close()  

 
