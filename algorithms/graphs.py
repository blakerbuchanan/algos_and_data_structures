# Implement various graph data structures in Python

# Class representing a node
class Node(object):
    def __init__(self, key, priority=0):
        self.key = key
        self.neighbors = {}
        self.explored = 0
        self.priority = priority

    def addNeighbor(self, neighbor, weight=0):
        self.neighbors[neighbor] = weight

    def getConnections(self):
        return self.neighbors.keys()

    def getWeight(self, neighbor):
        return self.neighbors[neighbor]

# Class representing a graph
class Graph(object):
    def __init__(self, dist=None):
        self.nodes = {}

    def addNode(self, node):
        self.nodes[node.key] = node

    def getNode(self, key):
        try:
            return self.nodes[key]
        except KeyError:
            return None

    def addEdge(self, from_key, to_key, weight = 0):
        if from_key not in self.nodes:
            self.addNode(Node(from_key))
        if to_key not in self.nodes:
            self.addNode(Node(to_key))
        
        self.nodes[from_key].addNeighbor(self.nodes[to_key], weight)
        self.nodes[to_key].addNeighbor(self.nodes[from_key], weight)

    def getNodes(self):
        return self.nodes.keys()

    def __iter__(self):
        return iter(self.nodes.values())


# Test out the above code
g = Graph()
for i in range(6):
    g.addNode(Node(i))

# print(g.nodes)

g.addEdge(0,1,1)
g.addEdge(0,5,1)
g.addEdge(1,2,1)
g.addEdge(2,1,3)
node2 = g.nodes[2]

print(node2.getWeight(g.nodes[1]))

# for n in g:
#     for w in n.getConnections():
#         print('{} -> {}'.format(n.key, w.key))

# print(g.nodes[1].getConnections())

# If one knows the nodes and edges apriori, 
# testGraph = {
#     0: {1:5, 5:2},
#     1: {2:4},
#     2: {3:9},
#     3: {4:7, 5:3},
#     4: {0:1},
#     5: {4:8}
# }

# print(testGraph[0])