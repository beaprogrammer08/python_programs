# -*- coding: utf-8 -*-
"""
Created on Tue Sep 28 17:13:34 2021

@author: hp
"""

def prime_number(x):
    for i in range(2,x+1):
        for a in range(2,i):
            if i%a==0:
                print(i,"number is compostite")
                break
    else:
        print(i,"number is prime")

prime_number(7)



def prime_number(x):
    for i in range(2,x):
            if x%i==0:
                print(x,"number is compostite")
                break
    else:
        print(x,"number is prime")

prime_number(7)

prime_number(1)
prime_number(2)
prime_number(3)
prime_number(4)
prime_number(5)
prime_number(6)
prime_number(8)
prime_number(9)
prime_number(10)
prime_number(11)
prime_number(12)
prime_number(13)
prime_number(14)



 