# -*- coding: utf-8 -*-
"""
Created on Mon Nov 22 17:48:38 2021

@author: hp
"""
n=int(input())
orignal_n0=n
Armstrong=0

while n>0:
    a+=1
    n=n//10
    while org_n>0:
        Last_Digit = org_n % 10
        Armstrong  = Armstrong  + ((Last_Digit)**(a))
        org_n = (org_n //10)
if orginal_no==Armstrong:
        print("true")
else:
        print("false")

        
