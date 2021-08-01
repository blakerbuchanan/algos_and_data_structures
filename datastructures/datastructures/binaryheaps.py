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

    # Produce a max heap from an unordered array
    def buildMaxHeap(self):

        for i in range(math.floor(len(self.nodes)/2)):
            self.maxHeapify(self.nodes,i)

        return None

    # Correct a single violation of the heap property in a subtrees root (do recursively)
    def maxHeapify(self):
        # Heapify starting from the last element in the heap
        index = len(self.nodes)-1
        while self.hasParent(index) and self.getParent(index)[1] > self.nodes[index]:
            self.swap(self.getParent(index)[0], index) # swap the parent node with current node
            index, _ = self.getParent(index)
    
    def peek(self):
        return self.nodes[0]

    def addNode(self, node):
        self.nodes.append(node) # Add node to the end
        # Max Heapify after adding new node

        return None

    def extractMax(self):
        maxElem = self.nodes[0] # Max is at root
        newArr = self.nodes[1:len(self.nodes)] # Array after extraction is just self.nodes but without the root
        
        # Need to max heapify array since extraction of root will unheapify

        return None

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
    heap.nodes.reverse()
    print(heap.nodes)
    heap.maxHeapify()
    print(heap.nodes)