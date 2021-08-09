# 
# Implement hash tables
# Hash tables in Python are implemented via Dictionaries, but it may be nice to implement it on my own. Let's get to it.

# Algorithm for implementing hash tables (hash maps)
# 1. Compute the key's hash code (usually an int or long data type)
# 2. Map the hash code to an index in an array. hash(key) % array_length
# 3. At this index, there exists a list of keys and values. Store the key and value in this index.

import numpy as np
import slinkedlist as sll

class HashTable:
    def __init__(self, table = None):
        self.table = table
    
    def mapToIndex(hash_key, array_length):
        return hash_key % array_length

    def addKeyValuePair(self, key, value):
        # Create the hash key
        hash_key = hash(key)

        # Compute the index at which to store test value
        # idx = self.mapToIndex(hash_key, np.size(self.table))
        idx = hash_key % np.size(self.table)

        # Create linked list for storage (to avoid collisions)
        linkedlist = sll.LinkedList()
        linkedlist.head = sll.ListNode(value)
        linkedlist.head.key = key
        
        # In more involved implementations, one would need to check the index idx computed
        # to see if a linked list already exists there (this would mean two keys have the same
        # hash code or that two different hash codes map to the same index). If this is the case,
        # one would need to add a node with the associated data to the existing linked list.
        # Note: Implement the above case.

        # Store linked list at idx in test array
        self.table[idx] = linkedlist

    def getValue(self, key):
        hash_key = hash(key)
        
        # idx = self.mapToIndex(hash_key,np.size(self.table))
        idx = hash_key % np.size(self.table)
        linkedlist = self.table[idx]

        return linkedlist.searchKeyValue(key)
    
    def deleteItem(self):
        return None

if __name__ == "__main__":
    # Note: Works, but there currently exists an issue with searching through a linked list. Likely due to collision of key-value pairs.
    # Create a simple test case
    key_test = "test"
    value_test = "success"
    HT = HashTable()
    HT.table = np.empty(5, dtype=object)
    
    HT.addKeyValuePair(key_test, value_test)
    HT.addKeyValuePair("socks","shoes")
    HT.addKeyValuePair("hello","goodbye")

    print(HT.getValue(key_test))
    print(HT.getValue("socks"))
    print(HT.getValue("hello"))