# Implement hash tables
# Hash tables in Python are implemented via Dictionaries, but it may be nice to implement it on my own. Let's get to it.

# Algorithm for implementing hash tables (hash maps)
# 1. Compute the key's hash code (usually an int or long data type)
# 2. Map the hash code to an index in an array. hash(key) % array_length
# 3. At this index, there exists a list of keys and values. Store the key and value in this index.

import numpy as np

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

def mapToIndex(hash_key,array_length):
    return hash(hash_key) % array_length

# Create a simple test case
key_test = "test"
value_test = "success"
array_test = np.empty(5, dtype=object)

# Create the hash key for the test key
hash_key_test = hash(key_test)

# Compute the index at which to store test value
idx = mapToIndex(hash_key_test,len(array_test))

# Create linked list for storage (to avoid collisions)
linkedlist_test = LinkedList()
linkedlist_test.head = ListNode(value_test)

# In more involved implementations, one would need to check the index idx computed
# to see if a linked list already exists there (this would mean two keys have the same
# hash code or that two different hash codes map to the same index). If this is the case,
# one would need to add a node with the associated data to the existing linked list.
# Note: Implement the above case.

# Store linked list at idx in test array
array_test[idx] = linkedlist_test

# With only a single key corresponding to one hash code, this is a trivial search over a linked list.
print(linkedlist_test.search(value_test))