# -*- coding: utf-8 -*-
"""
Created on Wed Nov 10 00:59:53 2021

@author: hp
"""

# iterator and generator

num=[1,2,3,4,5,6,7]
it=iter(num)
print(it.__next__())

print(it.__next__())
print(it.__next__())
print(it.__next__())
print(it.__next__())
print(it.__next__())


class Topten():
    def __init__(self):
        self.num=1
    def __iter__(self):
        return(self)
    def __next__(self):

        if self.num<=10:
            val=self.num
            self.num+=1
            
            return val
        else:
            raise StopIteration
values=Topten()



for i in values:
    print(i)









def cube(n=10):
    print(f"Generating cube from 1 to {0}")
    for i in range(1,n+1):
        yield i**3
gen=cube()
for x in gen:
    print(x)
    
    
    