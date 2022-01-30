# -*- coding: utf-8 -*-
"""
Created on Tue Sep 28 09:57:28 2021

@author: hp
"""

n=int(input())
x=2*n+2
for i in range(1,n+1):
    for j in range(1,x):
        if j==i or j==x-i or j==x/2:
            print("*",end="")
        else:
            print(0,end="")
    print("\n")        


n=int(input())
if n%2==0:
    x=int(n/2)
else:
    x=int(n/2+1)
for i in range(1,x+1):
    for k in range(1,i):
        print(" ",end="")
    for j in range(1,i+1):
        print("* ",end="")
    print("\n")
x=n-x
for i in range(x,0,-1):
    for k in range(i-2,-1,-1):
        print(" ",end="")
    for j in range(i,0,-1):
        print("* ",end="")
    print("\n")
    
    
    
    
    
def getsum():
    x=34
    y=12
    return(x+y,x-y)
z=getsum() #return key is used to return from the function  
print(z)
# you can return multiple values in the form of tuple


















































   
    
    
    
    
    
    