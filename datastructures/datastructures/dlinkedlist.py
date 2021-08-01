# Definition for node in singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None, prev=None):
        self.val = val
        self.next = next
        self.prev = prev

# Definition for linked list
class DoublyLinkedList:
    def __init__(self,head=None):
        self.head = head

    # Insert a new node at the beginning of the linked list
    def insertNode(self, new_data):
        # Create a new Node
        new_node = ListNode(new_data)

        # Make the "next" of new node the current head
        new_node.next = self.head
 
        # Make the new head the new node "new_node"
        self.head = new_node

    def addNode(self, new_data):
        node = ListNode(new_data)
        node.val = new_data
        
        if self.head == None:
            self.head = node
        else:
            p = self.head # Let p be the head
            # Now traverse the list until the next node is None (find the end of the linked list)
            while p.next != None:
                p = p.next
            
            p.next = node # Set the final node in the list to be the new node

        return None
    
    # Delete head of linked list (stack implementation)
    def pop(self):
        current_node = self.head
        self.head = current_node.next

    def deleteNode(self, node):
        p = self.head
        prevNode = p
        while p != node:
            p = p.next
            if p == node:
                prevNode.next = node.next

            prevNode = p

        return None

    def search(self, search_val):
        currentNode = self.head

        while currentNode != None:
            if currentNode.val == search_val:
                return currentNode.val

        return "Error: Data could not be located in linked list."