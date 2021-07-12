# Implement priority queues
import slinkedlist as sll
import math
Inf = math.inf

# This implementation of priority queues currently only works with weighted priorities >= 0
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
        self.Q.append(node)
    
    def pullMax(self):
        highest = 0
        for i in range(len(self.Q)):
            if self.Q[i].priority > highest:
                highestIdx = i
                highest = self.Q[i].priority
        
        self.Q.pop(highestIdx)
        return highestIdx,highest

    def pullMin(self):
        if self.Q:
            lowest = Inf
            # lowestIdx = 0
            for i in range(len(self.Q)):
                if self.Q[i].priority < lowest:
                    print(self.Q[i].priority)
                    lowestIdx = i
                    lowest = self.Q[i].priority

            # import ipdb; ipdb.set_trace()
            self.Q.pop(lowestIdx)
            return lowestIdx, lowest

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
