'''
Created on 03-Dec-2021

@author: divye
'''


class Vector:
    
    def __init__(self, data):
        self.data = data
        
    def __add__(self, v):
        """
        Here __add__() is magic method, 
        it will call when we use (binary +) operator 
        """
        return [(e1 + e2) for e1, e2 in zip(self.data, v.data)]


a = Vector([1,2,3])
b = Vector([1,2,3])
print(a + b)