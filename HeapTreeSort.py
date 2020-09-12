class Heaptree():
    def __init__(self):
        self.heap =[]
        self.size = 0
    
    def buildTree(self,arry):
        self.heap = arry
        i = (len(arry)//2) -1
        self.size = len(arry)
        while i >= 0:
            self.data_down(i)
            i  -=1
            
    def data_down(self,i):
        while i*2+2 <= self.size:
            mi = self.min_index(i)
            if self.heap[i] > self.heap[mi]:
                self.heap[i] , self.heap[mi] = self.heap[mi] , self.heap[i]
            i = mi
            
    def min_index(self,i):
        if i*2+2 >= self.size:
            return i*2+1
        else:
            if self.heap[i*2+2] < self.heap[i*2+1]:
                return i*2+2
            else:
                return i*2+1
    def get_min(self):
        min_ret = self.heap[0]
        self.size -= 1
        self.heap[0] = self.heap[self.size]
        self.heap.pop()
        #self.buildTree(self.heap) //超爛 用data_down來重排順序就可以
        self.data_down(0) #從0開始重排
        return min_ret

import random
num1 = [i*random.randint(1,6) for i in range(100)]
list1 = Heaptree()
list1.buildTree(num1)
print("GET MIN:")
for i in range(len(num1)):
    print(list1.get_min()," ",end="")
    
n = input()    