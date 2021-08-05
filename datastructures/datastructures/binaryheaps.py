# Implement a binary max heap in Python
# Max heap property: The value of a node is >= the values of its children
#
# An array like [16, 14, 10, 8, 7, 9, 3, 2, 4, 1] looks like
#
#              16
#             /   \
#          14       10    Ex. Max Heap
#         /  \     /  \   <-----------  
#       8     7   9    3
#      / \   /
#     2   4 1
#
# This adheres to the representation that the root of the tree is the first element.
# parent[i] = i/2
# left[i] = 2*i, right[i] = 2*i + 1

import math

class MaxHeap:
    def __init__(self):
        self.nodes = []
        self.heapsize = 0

    # Produce a max heap from an unordered array
    def buildMaxHeap(self):
        self.heapsize = len(self.nodes)

        for i in range(math.floor(len(self.nodes)/2),-1,-1):
            self.maxHeapify(i)


    # Correct a single violation of the heap property in a subtrees root (do recursively)
    def maxHeapify(self,index):
        
        # Heapify starting at index "index"
        leftIndex, leftVal = self.getLeftChild(index)
        rightIndex, rightVal = self.getRightChild(index)
        if leftIndex <= self.heapsize-1 and leftVal > self.nodes[index]:
            largest = leftIndex
        else:
            largest = index
        if rightIndex <= self.heapsize-1 and rightVal > self.nodes[largest]:
            largest = rightIndex

        if largest != index:
            self.swap(index, largest)
            self.maxHeapify(largest)
    
    def heapsort(self):
        self.buildMaxHeap()
        for i in range(len(self.nodes)-1,0,-1):
            self.swap(0,i)
            self.heapsize = self.heapsize-1
            self.maxHeapify(0)


    def peekMax(self):
        return self.nodes[0]

    def addNode(self, node):
        self.nodes.append(node) # Add node to the end
        index = self.heapsize - 1
        parentIndex, _ = self.getParent(index)
        # Max Heapify after adding new node
        # self.maxHeapify(parentIndex)
        self.buildMaxHeap()

    def extractMax(self):
        maxElem = self.nodes[0] # Max is at root
        # newArr = self.nodes[1:len(self.nodes)] # Array after extraction is just self.nodes but without the root
        try:
            maxElem = self.nodes[0] # Max is at root
            self.nodes[0] = self.nodes[self.heapsize-1]
            self.heapsize = self.heapsize - 1
            self.maxHeapify(0)
        except:
            print('Heap underflow...')

        return maxElem

    def hasParent(self,index):
        parentIndex = self.getParent(index)[0]
        if parentIndex >= 0:
            return True
        else:
            return False

    def getParent(self,index):
        parentIndex = math.floor((index - 1)/2)
        parentVal = self.nodes[parentIndex]
        return parentIndex, parentVal

    def getLeftChild(self,index):
        leftIndex = 2*index + 1
        if leftIndex <= len(self.nodes)-1:
            leftChild = self.nodes[leftIndex]
        else:
            leftChild = None

        return leftIndex, leftChild

    def getRightChild(self,index):
        rightIndex = 2*index + 2
        if rightIndex <= len(self.nodes)-1:
            rightChild = self.nodes[rightIndex]
        else:
            rightChild = None

        return rightIndex, rightChild

    def swap(self, parentIndex, index):
        parentVal = self.nodes[parentIndex]
        val = self.nodes[index]
        self.nodes[index] = parentVal
        self.nodes[parentIndex] = val

if __name__ == "__main__":
    heap = MaxHeap()
    heap.nodes = [10,15,20,17,25]
    # Test if we can build a max heap from an unordered array
    heap.buildMaxHeap()
    print(heap.nodes)

    # Add a node to the set
    heap.addNode(30)
    # heap.buildMaxHeap()
    # print(heap.nodes)
    # heap.heapsort()
    
    print(heap.nodes)
    heap.extractMax()
    print(heap.nodes)