import ctypes

class MeraList:
    def __init__(self):
        self.size = 1 #size of array
        self.n = 0  #n will tell how many items are there in array
        #create a ctype array with size=self.size
        def __make_array(self,capacity):
            #this create a ctype array with size capacity
            return(capacity*ctypes.py_object)()

