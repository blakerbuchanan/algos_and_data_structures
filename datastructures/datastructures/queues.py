# Impelement a queue in Python
# Makes use of the list data structure inherent to Python

class Queue:
    def __init__(self):
        self.Q = []

    def remove(self):
        try:
            self.Q.pop(0)
        except:
            print("Error: queue is empty.")

    def add(self, item):
        self.Q.append(item)

    def peek(self):
        return self.Q[0]

    def isEmpty(self):
        if len(self.Q) == 0:
            return True
        else:
            return False

if __name__ == '__main__':
    queue = Queue()
    queue.remove()
    print(queue.isEmpty())
    queue.add("bird")
    queue.add("alligator")
    print(queue.Q)
    print(queue.peek())
    print(queue.isEmpty())