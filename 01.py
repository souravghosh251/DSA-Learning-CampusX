import ctypes

class MeraList:
    def __init__(self):
        self.size = 1 #size of array
        self.n = 0  #n will tell how many items are there in array
        #create a ctype array with size=self.size
        self.A =  self.__make_array(self.size)

    def __len__(self):
        return self.n

    def __str__(self):
    # [1,2,3]
        result=''
        for i in range(self.n):
            result = result + str(self.A[i]) +  ','
        return '['+ result[:-1] +']'


    def append(self,item):
        if self.n == self.size:
            #resize
            self.__resize(self.size*2)
        self.A[self.n] = item
        self.n = self.n+1

    def __resize(self,new_capacity):
        #create a new array with new capacity
        B= self.__make_array(new_capacity)
        self.size = new_capacity
        for i in range(self.n):
            B[i] = self.A[i]
        #reassign
        self.A = B

    def __make_array(self,capacity):
        #this creates a ctype array with size capacity
        return(capacity*ctypes.py_object)()



L = MeraList()
L.append("hello")
L.append(3.4)
L.append('true')
print(L)
#print(f"Object type: {type(L)}")
#print(f"Length of list: {len(L)}")

