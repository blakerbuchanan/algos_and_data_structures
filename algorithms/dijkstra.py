# Dijkstra's algorithm
from datastructures import graphs
from datastructures import priorityqueues as PQ
import numpy as np
import math
Inf = math.inf

def relax(u,v,w,dist,pred):
    
    if dist[v.key] > dist[u.key] + w:

        dist[v.key] = dist[u.key] + w
        pred[v.key] = u

def dijkstra(G,s):
    # Initialize (G,s)
    # Initialize distance from s -> s
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

    while Q.Q:
        
        u = Q.extractMin()
        S.append(u)

        for v in u.neighbors:
            w = v.getWeight(u)
            relax(u,v,w,dist,pred)
    
    return dist, pred

if __name__ == "__main__":

    # Test case
    # Consider the following graph
    # 
    #    Y -- R
    #   /|  / |
    # G  | /  |
    #   \|/   |
    #    P -- B
    #
    # Implement Dijkstra's algorithm to compute the shortest path to 
    # between a specified source node and every other node in the graph.
    
    g = graphs.Graph()
    nodeLabels = ['G','Y','R','P','B']
    
    for label in nodeLabels:
        g.addNode(graphs.Node(label))

    g.addEdge('G','Y',19,False)
    g.addEdge('G','P',7,False)
    g.addEdge('Y','P',11,False)
    g.addEdge('Y','R',4,False)
    g.addEdge('P','R',15,False)
    g.addEdge('P','B',5,False)
    g.addEdge('B','R',13,False)

    source = g.nodes['G']
    dist, pred = dijkstra(g,source)
    goal_key = 'R'
    node = g.nodes[goal_key]

    # Compute shortest path from source to goal
    path = [goal_key]
    while node != source:
        path.append(pred[node.key].key)
        node = pred[node.key]
    path.reverse()
    print(path)