# -*- coding: utf-8 -*-
"""
Created on Sat Nov  6 00:14:31 2021

@author: hp
"""
# class and objects 

class Person():
    pass
karan=Person()
dupesh=Person()
print(karan)
print(dupesh)
karan.rollno="76372632"
dupesh.rollno="777777775675"
print(karan.rollno)
print(dupesh.rollno)
karan.__dict__
dupesh.__dict__












class Person():
    city="bathinda"
    standard="10"
karan=Person()
dupesh=Person()
print(karan)
print(dupesh)
karan.rollno="76372632"
dupesh.rollno="777777775675"
print(karan.rollno)
print(dupesh.rollno)
karan.__dict__
dupesh.__dict__
Person().__dict__    
dupesh.standard





class Dupesh():
    city="bathinda"
    def __init__(self,name,empid,number):
        self.name=name
        self.empid=empid
        self.number=number
        
dupesh=Dupesh("dupesh",123456789,6239701320)
dupesh.__dict__
        

class Dupesh():
    city="bathinda"
    def __init__(self,name,empid,number):
        self.name=name
        self.empid=empid
        self.number=number
    def printdesc(self):
        print(self.name,self.empid,self.number)
        
        
dupesh=Dupesh("dupesh",123456789,6239701320)
dupesh.__dict__
dupesh.printdesc()



class Dupesh():
    city="bathinda"
    def __init__(self,name,empid,number):
        self.name=name
        self.empid=empid
        self.number=number
    def printdesc(self):
        print(self.name)
    @staticmethod
    def printdata():
        print("static")
        
        
dupesh=Dupesh("dupesh",123456789,6239701320)
dupesh.__dict__
dupesh.printdesc()
dupesh.printdata()

        













