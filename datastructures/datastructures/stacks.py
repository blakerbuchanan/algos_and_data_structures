# This file implements a stack in Python
# This is really just a list data structure in Python, but I have
# included for completion.

class Stack:
    def __init__(self):
        self.stack = []

    def pop(self):
        try:
            self.stack.pop(-1)
        except:
            print("Error: stack is empty.")

    def push(self, item):
        self.stack.append(item)

    def peek(self):
        return self.stack[-1]

    def isEmpty(self):
        if len(self.stack) == 0:
            return True
        else:
            return False

if __name__ == '__main__':
    newStack = Stack()
    newStack.pop()
    print(newStack.isEmpty())
    newStack.push("bird")
    newStack.push("alligator")
    print(newStack.stack)
    print(newStack.peek())
    print(newStack.isEmpty())