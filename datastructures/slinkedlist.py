# Definition for node in singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# Definition for linked list
class LinkedList:
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

    # Delete head of linked list (stack implementation)
    def pop(self):
        current_node = self.head
        self.head = current_node.next

    def deleteNode(self, key):
        return None

    def search(self,search_val):
        currentNode = self.head

        while currentNode != None:
            if currentNode.val == search_val:
                return currentNode.val

        return "Error: Data could not be located in linked list."