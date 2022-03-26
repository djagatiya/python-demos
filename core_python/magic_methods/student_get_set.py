'''
Created on 04-Dec-2021

@author: divye
'''


class Students:
    
    def __init__(self):
        self.data = {}
    
    def __setitem__(self, key, value):
        self.data[key] = value
    
    def __getitem__(self, key):
        return self.data[key]
    
    def __len__(self):
        return len(self.data)


s = Students()
s[1] = {"name": "kuki", "age":17 }
s[2] = {"name":"dhuni"}
print(s[1])
print(len(s))