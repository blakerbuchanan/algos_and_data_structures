# Implement various graph data structures in Python

# Class representing adjacency list of the node, i.e., what 
class AdjNode:
    def __init__(self,data):
        self.vertex = data
        self.next = None

# A class representing a class as a list of adjacency lists. Size of array is the number of vertices
class Graph:
    def __init__(self,vertices):
        self.V = vertices
        self.graph = [None] * self.V

# A class representing a graph as a dictionary
class dictGraph:
    def __init__(self,nodes=None):
        self.nodes = None