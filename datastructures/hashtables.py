# Implement hash tables
# Hash tables in Python are implemented via Dictionaries, but it may be nice to implement it on my own. Let's get to it.

# Algorithm for implementing hash tables (hash maps)
# 1. Compute the key's hash code (usually an int or long data type)
# 2. Map the hash code to an index in an array. hash(key) % array_length
# 3. At this index, there exists a list of keys and values. Store the key and value in this index.

import numpy as np
import slinkedlist as sll

def mapToIndex(hash_key,array_length):
    return hash(hash_key) % array_length

# Create a simple test case
key_test = "test"
value_test = "success"
array_test = np.empty(5, dtype=object)

# Create the hash key for the test key
hash_key_test = hash(key_test)

# Compute the index at which to store test value
idx = sll.mapToIndex(hash_key_test,len(array_test))

# Create linked list for storage (to avoid collisions)
linkedlist_test = sll.LinkedList()
linkedlist_test.head = sll.ListNode(value_test)

# In more involved implementations, one would need to check the index idx computed
# to see if a linked list already exists there (this would mean two keys have the same
# hash code or that two different hash codes map to the same index). If this is the case,
# one would need to add a node with the associated data to the existing linked list.
# Note: Implement the above case.

# Store linked list at idx in test array
array_test[idx] = linkedlist_test

# With only a single key corresponding to one hash code, this is a trivial search over a linked list.
print(linkedlist_test.search(value_test))