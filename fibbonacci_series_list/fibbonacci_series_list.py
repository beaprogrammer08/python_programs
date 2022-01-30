# -*- coding: utf-8 -*-
"""
Created on Sun Sep  5 15:57:17 2021

@author: hp
"""

# list of fibbonacci series 


i=input("enter the number:")
i=int(i)
fibbonacci_list=[]
out=0
b=1
for a in range(0,i+1):
    fibbonacci_list.append(out)
    out=out+b
    b=out-b

print("fibbonacci_series_list=",fibbonacci_list)    