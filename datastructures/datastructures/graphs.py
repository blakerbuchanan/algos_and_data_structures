# Implement various graph data structures in Python
import math
Inf = math.inf

# Class representing a node
class Node(object):
    def __init__(self, key, priority=0, d=0):
        self.key = key
        self.neighbors = {}
        self.explored = 0
        self.d = d
        self.fin_time = 0
        self.priority = priority
        
    def addNeighbor(self, neighbor, weight=0):
        self.neighbors[neighbor] = weight

    def getConnections(self):
        return self.neighbors.keys()

    def getWeight(self, neighbor):
        return self.neighbors[neighbor]

# Class representing a graph
class Graph(object):
    def __init__(self, do_tps=False):
        self.nodes = {}
        self.do_tps = do_tps
        self.tps = None

    def addNode(self, node):
        self.nodes[node.key] = node

    def getNode(self, key):
        try:
            return self.nodes[key]
        except KeyError:
            return 'Error: No node associated with key ' + str(key)

    def addEdge(self, from_key, to_key, weight = 0, directed=True):
        if from_key not in self.nodes:
            self.addNode(Node(from_key))
        if to_key not in self.nodes:
            self.addNode(Node(to_key))
        
        # If edge is directed, add neighbor for nodes[from_key] 
        if directed:
            self.nodes[from_key].addNeighbor(self.nodes[to_key], weight)
        else: # Otherwise, add neighbors for both nodes[from_key] and nodes[to_key]
            self.nodes[to_key].addNeighbor(self.nodes[from_key], weight)
            self.nodes[from_key].addNeighbor(self.nodes[to_key], weight)

    def getNodes(self):
        return self.nodes.keys()

    def __iter__(self):
        return iter(self.nodes.values())


if __name__ == "__main__":
    # Test out the above code
    g = Graph()
    nodeNames = ['r','s','t','u','v','w','x','y']
    for i in nodeNames:
        g.addNode(Node(i))

    # print(g.nodes)

    g.addEdge('s','w',1,False)
    g.addEdge('s','r',1,False)
    g.addEdge('r','v',1,False)
    g.addEdge('w','t',1,False)
    g.addEdge('w','x',1,False)
    g.addEdge('t','x',1,False)
    g.addEdge('t','u',1,False)
    g.addEdge('x','y',1,False)
    g.addEdge('u','x',1,False)
    g.addEdge('u','y',1,False)