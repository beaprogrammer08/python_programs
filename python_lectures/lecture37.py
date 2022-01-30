# -*- coding: utf-8 -*-
"""
Created on Wed Oct 13 16:53:47 2021

@author: hp
"""
   
n=int(input("enter the number:"))
out=0
for i in range(0,n+1):
    i=str(i)
    b=i.count("1")
    out+=b
print(out) 