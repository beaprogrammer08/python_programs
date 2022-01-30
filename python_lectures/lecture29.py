# -*- coding: utf-8 -*-
"""
Created on Fri Oct  1 10:33:41 2021

@author: hp
"""
    
    
def fibbnacci_series(n):    
    out=0
    b=1
    for i in range(0,n):
        print(out,end="")
        out=out+b
        b=out-b
fibbnacci_series(int(input("enter the number:")))    



def armstrong_number(n):
    a=n//10
    b=n//100
    c=n%10
    d=a%10
    if c**3+b**3+d**3==n:
        print("armstrong number")
    else:
        print("not a armstrong number")
armstrong_number(int(input("enter 3 digit number:")))



    
def fibbnacci_series(n):    
    out=0
    b=1
    for i in range(0,n):
        print(out,end="")
        out=out+b
        b=out-b
fibbnacci_series(int(input("enter the number:")))    

