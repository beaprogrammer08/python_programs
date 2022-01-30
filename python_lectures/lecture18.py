# -*- coding: utf-8 -*-
"""
Created on Thu Sep 23 14:00:41 2021

@author: hp
"""


n=int(input())
for i in range(0,n+1):
    for a in range(0,n-i):
        print(" ",end="")
    for b in range(1,i+1):
        print(b,end="")
    print("\n")
      
    
    

n=int(input())
for i in range(0,n+1):
    for a in range(0,n-i):
        print(" ",end="")
    for b in range(1,i+1):
        print(b,end="")
    for c in range(i-1,0,-1):
        print(c,end="")
    print("\n")
    
    
    
    
    
    
    
    


n=int(input())
for i in range(0,n+1):
    for a in range(0,n-i):
        print(" ",end="")
    for b in range(1,i+1):
        print("*",end="")
    for c in range(i-1,0,-1):
        print("*",end="")
    print("\n")
    
    
    
    
    

n=int(input())
for i in range(0,n+1):
    for a in range(0,n-i):
        print(" ",end="")
    for b in range(1,i+1):
        print(b+i-1,end="")
    for c in range(i-1,0,-1):
        print(c+i-1,end="")
    print("\n")

    
    
    

n=int(input())
for i in range(0,n+1):
    for a in range(0,n-i):
        print(" ",end="")
    
    for b in range(1,i+1):
        print(i-b+1,end="")
        
    for c in range(i-1,0,-1):
        print(i-c+1,end="")
            
    print("\n")
                 



n=int(input())
for i in range(0,n+1):
    for a in range(0,n-i):
        print(" ",end="")
        
    for b in range(1,i+1):
        print(i-b+1,end="")
        
    print("\n")
     
    

n=int(input())
for i in range(0,n+1):
    for c in range(1,i+1):
        print(c,end="")
        
    for a in range(0,n-i):
        print(" ",end="")
        
    for b in range(1,i+1):
        print(i-b+1,end="")
        
    print("\n")
