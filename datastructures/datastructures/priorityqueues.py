# Implement priority queues
import slinkedlist as sll
import math
Inf = math.inf
# Queue utilizes first-in-first-out
# This naive implementation of priority queues currently only works with weighted priorities >= 0. 
# It is naive in the sense that it pulls the highest-priority element in O(n) time

class Node(object):
    def __init__(self, priority=0, data=None):
        self.priority = priority
        self.data = data

class PriorityQueue:
    def __init__(self, Q=[]):
        self.Q = Q # Queue will be a list of nodes

    def isEmpty(self):
        if len(self.Q) == 0:
            return True
        return False
    
    def insert(self, node):
        self.Q.append(node)
    
    def pop(self, node):
        self.Q.remove(node)

    def pull(self):
        
        highest = self.Q[0]
        for node in self.Q:
            if highest.priority < node.priority:
                highest = node

        self.Q.remove(highest)
        return highest

    def peek(self):
        for node in self.Q:
            if highest.priority < node.priority:
                highest = node
        
        return highest

if __name__ == '__main__':
    node1 = Node(10)
    node2 = Node(22)
    node3 = Node(3)
    node4 = Node(30)
    node5 = Node(6)
    node6 = Node(8)

    Q = PriorityQueue()
    print(Q.isEmpty())
    Q.insert(node1)
    Q.insert(node2)
    Q.insert(node3)
    Q.insert(node4)
    Q.insert(node5)
    Q.insert(node6)

    highest = Q.pull()
    print(highest.priority)
    highest = Q.pull()
    print(highest.priority)
    print(Q.isEmpty())
