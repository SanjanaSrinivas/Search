#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jan  4 21:04:13 2018

@author: Sanjana
"""


#final

import copy
import time
from collections import OrderedDict
from operator import itemgetter


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
    
    if(nod.depth==max_depth or terminal(nod.board) or time_move-(time.time() - start_time) <=0.2  ):    
        
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
    
    if( nod.depth==max_depth or terminal(nod.board) or time_move-(time.time() - start_time) <=0.2  ):   
        
        return (nod.score[0])-(nod.score[1]) 
    
    
    mat=copy.deepcopy(nod.board)
    if (nod==root):
        children=cluster
    else:
        children=successor(mat)
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
with open('input.txt') as f:
    words = [word.strip() for word in f]    
n=int(words.pop(0))
f=int(words.pop(0))
t=float(words.pop(0))
found=False
a = [[''] * n for i in range(n)]

for i in range(0,n):
    for j in range(0,n):
        a[i][j]=words[i][j]
        if(a[i][j]!='*' and found==False):
            x=i
            y=j
            found=True
            
b=copy.deepcopy(a)    
try:
    with open('calibration.txt') as f1:
        nodes_per_second=float(f1.read())
    
except FileNotFoundError:
    nodes_per_second=735.899378739486

f1.close()    
max_depth=0      
cluster=successor(b)
bf=len(cluster)
time_move=t/2
for depth in range(0,51):
        nn=pow(bf,depth)
        if(nn<=time_move*nodes_per_second):
            max_depth=depth
        else:
            break            
            
if(t<0.6 and x!=None and y!=None):
    
    e=[[0] * n for i in range(n)]
    #print ("here 1")
    s=adjacent(a,x,y,a[x][y],e)
    gravity(a)
    m=chr(y+65)+str(x+1)
    f2=open("output.txt","w")
    f2.write(m )
    f2.write("\n")
    for i in range(0,n):
        for j in range(0,n):
            f2.write(str(a[i][j]))
        f2.write("\n")   
    f2.close()             

elif(time_move<=0.5 or max_depth==0):
    #print ("here 2")
    var=list(cluster.items())
    move=var[0][0]
    row=ord(move[0])-65
    col=ord(move[1])-65
    
    e=[[0] * n for i in range(n)]
    r=adjacent(a,row,col,a[row][col],e)
    gravity(a)
    m=chr(col+65)+str(row+1)
    f3=open("output.txt","w")
    f3.write(m )
    f3.write("\n")
    for i in range(0,n):
        for j in range(0,n):
            f3.write(str(a[i][j]))
        f3.write("\n") 
    f3.close()    
else:
    #print ("here 3") 
    A=-float("inf")
    B=float("inf")
    
    initial=node(a,0,[0,0],-1,-1,-1,-1)

    root=initial
    res=max_val(initial,A,B)
    result_matrix
    fo=open("output.txt","w")
    fo.write(str(movey))
    fo.write(str(movex))
    fo.write("\n")
    for i in range(0,n):
        for j in range(0,n):
            fo.write(str(result_matrix[i][j]))
        fo.write("\n")   
    fo.close()         

#print("--- %s seconds ---" % (time.time() - start_time))  
        