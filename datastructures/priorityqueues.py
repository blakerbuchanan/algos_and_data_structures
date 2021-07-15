# Implement priority queues
import slinkedlist as sll
import math
Inf = math.inf
# Queue utilizes first-in-first-out
# This implementation of priority queues currently only works with weighted priorities >= 0. min-priority queue = (lower priority) -> (higher weight), (higher priority) -> (lower weight)
class Node(object):
    def __init__(self, priority=0, data=None):
        self.priority = priority
        self.data = data

class PriorityQueue:
    def __init__(self, Q=[]):
        self.Q = Q
        self.minimum = Inf
        self.nodeMinimum = []

    def isEmpty(self):
        if len(self.Q) == 0:
            return True
        return False
    
    def insert(self, node):
        # self.Q.append(node)

        if node.priority <= self.minimum:
            self.nodeMinimum.append(self.minimum)
            self.minimum = node.priority
        else:
            self.nodeMinimum.append(self.minimum)
            
        self.Q.append(node)
    
    def pop(self):
        if len(self.Q) != 0: 
            self.Q.pop(0)
            self.minimum = self.nodeMinimum[0]
            return self.nodeMinimum.pop(0)
        else:
            return None
    
    def pullMax(self):
        # highest = 0
        # for i in range(len(self.Q)):
        #     if self.Q[i].priority > highest:
        #         highestIdx = i
        #         highest = self.Q[i].priority
        
        # self.Q.pop(highestIdx)
        # return highestIdx,highest
        return self.maximum

    def pullMin(self):
        # if self.Q:
        #     lowest = Inf
        #     # lowestIdx = 0
        #     for i in range(len(self.Q)):
        #         if self.Q[i].priority < lowest:
        #             print(self.Q[i].priority)
        #             lowestIdx = i
        #             lowest = self.Q[i].priority

        #     # import ipdb; ipdb.set_trace()
        #     self.Q.pop(lowestIdx)
        #     return lowestIdx, lowest
        minReturn = self.minimum
        u = self.pop()
        return u

    def peek(self):
        highest = 0
        for i in range(len(self.Q)):
            if self.Q[i].priority > highest:
                highestIdx = i
                highest = self.Q[i].priority
        
        return highestIdx,highest

# node1 = Node(7)
# node2 = Node(4)
# node3 = Node(10)
# node4 = Node(3)

# pqueue = PriorityQueue()
# print(pqueue.isEmpty())
# pqueue.insert(node1)
# pqueue.insert(node2)
# pqueue.insert(node3)
# pqueue.insert(node4)

# print(pqueue.pull())
# print(pqueue.isEmpty())
