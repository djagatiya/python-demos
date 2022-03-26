'''
Created on 03-Dec-2021

@author: divye
'''


class DBOps:
    
    def __init__(self):
        print("DB Connection Initialized...") 
    
    def __enter__(self):
        # return our DB_OPS object for operations.
        print("__ENTER__ called...")
                            
    def __exit__(self, exc_type, exc_val, exc_tb):
        # close our DB connection
        print("__EXIT__ called...")
        
 
with DBOps() as db:
    print("DB Operations...")
    # raise AssertionError("Db_ops exception..")

