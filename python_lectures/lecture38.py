# -*- coding: utf-8 -*-
"""
Created on Tue Oct 19 17:52:58 2021

@author: hp
"""

# file handling 


f=open("alice.txt")
print(f.read())
f.close()


with open("alice.txt") as f:
    print(f.read())



f=open("alice.txt")
print(f.read())
f.close()

with open("alice3.txt","w") as f:
    f.write("hello world")
    

with open("alice1.txt","a") as f:
    f.write("\nhello world")
    
    
    
    
    
    
    
    
# seek and tell

with open("alice1.txt") as f:
    f.seek(6)
    print(f.read())
    
    
with open("alice3.txt") as f:
    f.seek(2)
    print(f.tell())
    print(f.read())
    print(f.tell())
    
    
    
    
    
    
    
    
    
    
    
    
    