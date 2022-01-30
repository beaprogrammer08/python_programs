# -*- coding: utf-8 -*-
"""
Created on Mon Aug 23 10:08:10 2021

@author: hp
"""

i=0

while i<16:
    print(i)
    if i==9:
        break
    i+=1
    
    
for i in range(0,18):
    print(i)
    if i==6:
        break
    i+=1
    
    
    

i=0

while i<16:
    i+=1
    if i==9:
        continue
    print(i)
    
    
for i in range(0,18):
    i+=1
    if i==6:
        continue
    print(i)
    
    
    
my_var='hello world'

for i in my_var[-1:-13:-1]:
    print(i,end="")
    
    


for i in range(10,0,-1):
    print(i,end="")  
    

var_1="0110101001"


for i in var_1[-1:-11:-1]:
    print(i,end="")
    
    
    
    
i=input("enter the number:-")
i=int(i) 
out=1

for a in range(1,i+1):     
    out=out*a
    print(out)