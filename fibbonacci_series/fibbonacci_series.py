# -*- coding: utf-8 -*-
"""
Created on Sun Aug 22 17:49:03 2021

@author: hp
"""


#fibbonacci series


i=int(input())

out=0
b=1
for a in range(0,i+1):
    out=out+b
    b=out-b
    if i==out:
        print("true")
        break
else:
        print("false") 
   
    
    
    


        