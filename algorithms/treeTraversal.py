# In-order, pre-order, and post-order tree traversal for binary search trees

from typing import List

# Class creating a node with two edges
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# Class containing in-order, pre-order, and post-order binary tree traversals using recursion
class TreeTraversal:
    def inorderTraversal(self, root: TreeNode, nodeList=None) -> List[int]:
        
        if nodeList is None:
            nodeList = []
            
        if root:
            self.inorderTraversal(root.left, nodeList)
            nodeList.append(root.val)
            # print(root.val)
            self.inorderTraversal(root.right, nodeList)

        return nodeList
    
    def preorderTraversal(self, root: TreeNode, nodeList=None) -> List[int]:
        if nodeList is None:
            nodeList = []
            
        if root:
            nodeList.append(root.val)
            self.preorderTraversal(root.left, nodeList)
            
            # print(root.val)
            self.preorderTraversal(root.right, nodeList)

        return nodeList

    def postorderTraversal(self, root: TreeNode, nodeList=None) -> List[int]:
        if nodeList is None:
            nodeList = []
            
        if root:
            self.postorderTraversal(root.left, nodeList)
            # print(root.val)
            self.postorderTraversal(root.right, nodeList)
            nodeList.append(root.val)
            
        return nodeList

# The following code tests a binary search tree from Introduction to Algorithms by Cormen
root = TreeNode(6)
node2 = TreeNode(5)
node3 = TreeNode(2)
node4 = TreeNode(5)
node5 = TreeNode(7)
node6 = TreeNode(8)

root.left = node2
root.right = node5
node2.left = node3
node2.right = node4
node5.right = node6

nodeList = []
newTraversal = TreeTraversal()
nodeSequence = newTraversal.inorderTraversal(root)
# Expect [2, 5, 5, 6, 7, 8] for in-order Traversal
print(nodeSequence)