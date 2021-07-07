# Implement a depth-first search algorithm for tree or graph search 
# This implementation will utilize adjacency lists (probably in the form of a Dictionary)

import graphs 

def depthFirstSearch(G,v,visited,visitSeq):
    # visited = []
    visited.append(v)
    # visitSeq = []
    visitSeq.append(v.key)

    for u in v.neighbors:
        if u not in visited:
            depthFirstSearch(G,u,visited,visitSeq)

    return visitSeq

# Test out the above code
g = graphs.Graph()
for i in range(6):
    g.addNode(graphs.Node(i))

g.addEdge(0,1,1)
g.addEdge(0,2,1)
g.addEdge(1,3,1)
g.addEdge(1,4,1)
g.addEdge(2,5,1)
g.addEdge(4,5,1)

print('------START DFS------')
visited=[]
visitSeq=[]
finalSeq = depthFirstSearch(g,g.nodes[0],visited,visitSeq)
print(finalSeq)
print('------END DFS------')