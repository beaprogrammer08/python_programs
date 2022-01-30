# -*- coding: utf-8 -*-
"""
Created on Tue Oct  5 00:05:30 2021

@author: hp
"""

#pascal triangle :
    
    
    

out=[]
count=1
c=int(input("enter the column:"))
r=int(input("enter the row:"))
for j in range(0,r):
    row=[]
    for i in range(0,c):
        row.append(count)
        count+=1
    out.append(row)    
print(out)   





out=[]
count=1
r=int(input("enter the column:"))
for j in range(1,r+1):
    row=[]
    for i in range(0,j):
        if i==0 or i==j-1:
            count=1
            

        else:
            count=j-1
        row.append(count)
        
    out.append(row)
    count=1    
print(out)   



  