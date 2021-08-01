# Implement in a Min Stack in Python
import math
Inf = math.inf

# MinStack retrieves minimum in O(1) time
class MinStack:

    def __init__(self, minimum = Inf, nodeMinimum = []):
        self.stack = [] # Initialize stack
        self.minimum = minimum # Initialize the minimum to be infinity
        self.nodeMinimum = nodeMinimum # Initialize a list to track the minimum at a given instance 

    def push(self, val: int) -> None:
        # If the value to be pushed is less than the current minimum,...
        # ...assign val as current minimum and append previous minimum to nodeMinimum 
        if val <= self.minimum:
            self.nodeMinimum.append(self.minimum)
            self.minimum = val
        else: # Otherwise, let current minimum remain 
            self.nodeMinimum.append(self.minimum)
            
        self.stack.append(val)

    def pop(self) -> None:
        if len(self.stack) != 0: 
            self.stack.pop(-1)
            self.minimum = self.nodeMinimum[-1]
            self.nodeMinimum.pop(-1)
        else:
            return None

    def top(self) -> int:
        if len(self.stack) != 0: 
            return self.stack[-1]
        else:
            return None

    def getMin(self) -> int:
        return self.minimum


if __name__ == '__main__':
    # Test out MinStack()
    obj = MinStack()
    obj.push(3)
    obj.push(1)
    obj.push(5)
    obj.push(-3)
    print(obj.getMin())
    obj.pop()
    print(obj.getMin())