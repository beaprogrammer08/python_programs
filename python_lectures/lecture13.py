# -*- coding: utf-8 -*-
"""
Created on Thu Sep 16 17:13:42 2021

@author: hp
"""


class Solution(object):
    def reverseOnlyLetters(self, S):
        letters = [c for c in S if c.isalpha()]
        ans = []
        for c in S:
            if c.isalpha():
                ans.append(letters.pop())
            else:
                ans.append(c)
        return "".join(ans)    
sol=Solution()
sol.reverseOnlyLetters("Test1ng-Leet=code-Q!")        
                    
            
            
            
def reverseOnlyLetters(S):
        letters = [c for c in S if c.isalpha()]
        ans = []
        for c in S:
            if c.isalpha():
                ans.append(letters.pop())
            else:
                ans.append(c)
        return "".join(ans)    
reverseOnlyLetters("Test1ng-Leet=code-Q!")        
                    
            
                        
            
            
            
        
my_dict={}
type(my_dict)
my_dic=dict()
type(my_dic)