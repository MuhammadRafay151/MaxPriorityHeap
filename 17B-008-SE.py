# CS322 : Design and Analysis of Algorithms
# Bonus Assignment - (Max Points: 5)
# Implement the Maximum Priority Queue
# Refer Section 6.5 of the text book to learn about Priority Queue
# Due Date: 20 July 2020

#Instructions:
# Do not change the function name
# You can add more functions if require
# Your file name must be your Roll Number
# Uncompilable file will not be graded
# Plagiarism will not be tolerated at all


### ROLL NUMBER: <17b-008-se>

class MaxPriorityHeap:
    
    def __init__(self, data: list):
        # initialize the heap for given data
        self.data = data
        self.BuildHeap()
        pass
    
    def BuildHeap(self):
        n=len(self.data)//2
        n-=1
        while n>=0:
            self.MaxHeapify(n)
            n-=1
    def MaxHeapify(self, i: int):
        left=self.left(i)
        right=self.right(i)
        largest=i
        if left<len(self.data) and self.data[left]>self.data[i]:
            largest=left
        if right<len(self.data) and self.data[right]>self.data[largest]:
            largest=right
        if largest!=i:
            self.data[i],self.data[largest]=self.data[largest],self.data[i]
            self.MaxHeapify(largest)
    def HeapIncreaseKey(self, i:int , key: int):
        self.data[i]=key
        parent=self.parent(i)
        while i>0 and self.data[i]>self.data[parent]:
            self.data[i],self.data[parent]=self.data[parent],self.data[i]
            i=parent
            parent=self.parent(parent)
        
        # print(self.data)
    def Peek(self):
        return self.data[0]
    def ExtractMaximum(self):
        peek=self.data[0]
        x=self.data[len(self.data)-1]
        self.data[0]=x
        self.data=self.data[:len(self.data)-1]
        self.MaxHeapify(0)
        return peek
    def parent(self,i):
        return (i-1)//2
    def left(self,i):
        return i*2+1
    def right(self,i):
        return (i*2)+2
   
list=[1,2,3,4]
print("orginal Array: ",list)
m1=MaxPriorityHeap(list)
print("Heap: ",m1.data)
print("Peek: ",m1.Peek())
print("Extract Maximum: ",m1.ExtractMaximum())
print("After Extract Maximum: ",m1.data)
m1.HeapIncreaseKey(4,20)
print("After Increase Key: ",m1.data)

