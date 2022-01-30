# -*- coding: utf-8 -*-
"""
Created on Fri Oct  1 17:38:03 2021

@author: hp
"""
n=int(input("enter the number:"))
i=1
out=0
a=5645645545
while a!=0:
    a=n//(5**i)
    i+=1
    out=out+a
print(out)
    
def count_number(n):
    i=1
    out=0
    a=1
    while a!=0:
        a=n//(5**i)
        i+=1
        out=out+a
    print(out)
count_number(int(input("enter the number:")))    