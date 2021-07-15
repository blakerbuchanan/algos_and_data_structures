# Implement Dijkstra's algorithm
import sys
sys.path.insert(1, '/Users/blake/Dropbox/Job Preparation/algosdatastructs/datastructures')
import graphs
import priorityqueues as PQ
import numpy as np
import math
Inf = math.inf
# import ipdb

def relax(u,v,w,dist,pred):
    
    if dist[u] > dist[u] + w:
        dist[v] = dist[u] + w
        pred[v] = u
        v.priority = dist[v]

def dijkstra(G,s):
    # Initialize (G,s)
    # Initialize distance from s -> s
    # G.dist = np.zeros((len(G.nodes),len(G.nodes)))
    # dist = np.zeros(len(G.nodes))
    # pred = np.zeros(len(G.nodes))
    dist = {s.key: 0}
    pred = {}

    S = []
    Q = PQ.PriorityQueue()
    # Populate priority queue
    for key in G.nodes:
        node = G.getNode(key)
        if node != s:
            # Initialize priority values
            dist[node.key] = Inf
            pred[node.key] = None
            node.priority = dist[node.key]
        Q.insert(node)

    while Q:
        # print(Q.Q)
        u = Q.pullMin()
        
        S.append(u)
        # import ipdb; ipdb.set_trace()
        for v in u.neighbors:
            w = v.getWeight(u)
            relax(u.key,v.key,w,dist,pred) # need to write this function
    
    return dist, pred

# How should I store the distances between nodes?
# Test out the above code
g = graphs.Graph()
nodeLabels = ['G','Y','R','P','B']
nodeLabels = [0, 1, 2, 3, 4]
for label in nodeLabels:
    g.addNode(graphs.Node(label))

# print(g.nodes['G'])
# print(g.nodes)
#    Y -- R
#   /|  / |
# G  | /  |
#   \|/   |
#    P -- B

# g.addEdge('G','Y',19)
# g.addEdge('G','P',7)
# g.addEdge('Y','P',11)
# g.addEdge('Y','R',4)
# g.addEdge('P','R',15)
# g.addEdge('P','B',5)
# g.addEdge('B','R',13)

g.addEdge(0,1,19)
g.addEdge(0,4,7)
g.addEdge(1,4,11)
g.addEdge(1,2,4)
g.addEdge(4,2,15)
g.addEdge(4,3,5)
g.addEdge(3,2,13)
source = g.nodes[0]
# print(g.nodes)
dijkstra(g,source)