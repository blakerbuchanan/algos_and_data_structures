# Implement hash tables
# Hash tables in Python are implemented via Dictionaries, but it may be nice to implement it on my own. Let's get to it.

# Algorithm for implementing hash tables (hash maps)
# 1. Compute the key's hash code (usually an int or long data type)
# 2. Map the hash code to an index in an array. hash(key) % array_length
# 3. At this index, there exists a list of keys and values. Store the key and value in this index.

import numpy as np

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def mapToIndex(hash_key,array_length):
    return hash(hash_key) % array_length

def findKeyValuePair(hash_key,linked_list):
    # Need to implement search through a linked list to find value corresponding to hash_key
    return linked_list.val, linked_list.next.val
    # while linked_list.val != key_test:


key_test = "test"
value_test = "success"
array_test = np.empty(5, dtype=object)
hash_key_test = hash(key_test)
idx = mapToIndex(hash_key_test,len(array_test))
linkedlist_test = ListNode(key_test,ListNode(value_test))
array_test[idx] = linkedlist_test

print(findKeyValuePair(key_test,linkedlist_test))