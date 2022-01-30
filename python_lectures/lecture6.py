# -*- coding: utf-8 -*-
"""
Created on Wed Aug 25 17:41:46 2021

@author: hp
"""

my_var="Hello world"

my_var2=my_var.upper()
my_var3=my_var.lower()

print(my_var2)
my_var2.isupper()


my_string="hello world"

my_string2=my_string.title()
my_string3=my_string.capitalize()

print(my_string2)
print(my_string3)

my_var="1093726382738"
my_var.isdigit()

my_var="898 79798"
my_var.isdigit()


my_var="787545323446hjgvbn b*&^"
my_var.isdigit()


my_var="86479486095klmvoij569i m"
my_var.isalpha()

my_var="nrkvfmd"
my_var.isalpha()

my_var="kjdikhb652mfg"
my_var.isalnum()



my_var="hi9fhdghghfdh786hjhjfjfkhhjkmbdg"

my_var.count("h")


my_var="hello world in the earth"

my_var.find("d")





my_var="Py1th2o3n"
for i in my_var:
    if i.isalpha()==True:
         print(i,end="")
    

my_var="Py1th2o3n"
for i in my_var:
    if i.isdigit()==True:
         print(i,end="")
        
        
my_string="HeLLo World"
for i in my_string:
    if i.islower()==True:
        a=i.upper()
    elif i.isupper()==True:
        a=i.lower()
    print(a,end="")
    
    
    
    
        
my_string="HeLLo World"
for i in my_string:
    if i.isupper()==True:
        print(i,end="")
       
       
               
 
my_string="HeLLo World"
out=0
b=0
for i in my_string:
    if i.islower()==True:
        out=out+1
        print(f"lower case={out}")
    elif i.isupper()==True:
        b=b+1
        print(f"upper case={b}")
       
             
               
print(out)
print(b)
        
my_var="hello world"
my_var.find("h")        