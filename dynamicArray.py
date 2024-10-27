import ctypes
class DynamicArray:
    def __init__(self):
        self.arraySize=1
        self.numOfElements=0
        self.arrayA=self.__makeArray(self.arraySize)

    def __len__(self):
        return self.numOfElements

    def __makeArray(self,capacity):
        # create a static and referential type array with size of capacity
        return (capacity*ctypes.py_object)()

    def append(self,item):
        if self.numOfElements==self.arraySize:
            #make another array that is double in size
            self.__resize(self.arraySize*2)

        #append element at end of array
        self.arrayA[self.numOfElements]=item
        self.numOfElements+=1

    def __resize(self, new_size):
        # create new array with new size
        arrayB=self.__makeArray(new_size)
        self.arraySize=new_size
        #copy content of arrayA to arrayB
        for i in range(self.numOfElements):
            arrayB[i]=self.arrayA[i]
        self.arrayA=arrayB

    # print function
    def __str__(self):
        result=""
        for i in range(self.numOfElements):
            result=result+str(self.arrayA[i])+","
        return "["+result[:-1]+"]"
    
        # Indexing
    def __getitem__(self, index):
        if 0<=index<self.numOfElements:
            print(self.arrayA[index]) 
            return self.arrayA[index]
        else:
            print("Index error-Index out of range")
            return "Index error-Index out of range"

    def insert(self,pos,item):
        if 0<=pos<=self.numOfElements:
            if self.numOfElements==self.arraySize:
                self.__resize(self.arraySize*2)

            for i in range(self.numOfElements,pos,-1):
                self.arrayA[i]=self.arrayA[i-1]

            self.arrayA[pos]=item
            self.numOfElements+=1
        else:
            print("Index Error-index out of range")
            return
      #del function  
    def __delitem__(self,pos):
        if 0<= pos< self.numOfElements:
            for i in range(pos,self.numOfElements-1):
                self.arrayA[i]=self.arrayA[i+1]
            
            self.numOfElements-=1

        
    def pop(self):
        if self.numOfElements==0:
            # return "Empty list-Can pop  element"
            print("Empty list-Can pop  element")
            return
        print("Element to be popped: ",self.arrayA[self.numOfElements-1])
        self.numOfElements=self.numOfElements-1
    
    def remove(self,item):
        pos=self.find(item)
        if type(pos) == int:
            self.__delitem__(pos)
            return True
        return False

    def find(self,item):
        for i in range(self.numOfElements):
            if self.arrayA[i]==item:
                print("Value found at index: ",i)
                return i
                
        print("Value Error-Value not found")
        return 

    def clear(self):
        self.arraySize=1
        self.numOfElements=0
           



L=DynamicArray()
L.insert(0,0)
L.insert(1,1)
L.insert(2,2)
L.insert(3,3)
L.insert(4,4)
L.insert(5,5)
L.insert(6,6)
L.append("Bye")
del L[5]
L.remove(0)
print(L)
L.find("Hello")
# L.clear()
L.pop()
print(L)


