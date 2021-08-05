# Implement a breadth-first search algorithm for tree or graph search 
# This implementation will utilize adjacency lists (probably in the form of a Dictionary)

from datastructures import graphs

def breadthFirstSearch(G, root):
    Q = [] # Let Q be a queue in the form of a list (lists are slow due to pop operations)
    visited = [] # visited tracks what nodes have been visited
    visitSeq = [] # sequence of visitation
    
    visited.append(root)
    visitSeq.append(root.key)
    root.explored = 1
    Q.append(root)

    while Q:
        print([[node.d,node.key] for node in Q])
        v = Q.pop(0)
        # If v is goal state then return v
        for u in v.neighbors:
            if u not in visited:
                u.explored = 1
                u.d = v.d + 1
                visited.append(u)
                visitSeq.append(u.d)
                Q.append(u)
    
    return visited

g = graphs.Graph()

nodeNames = ['r','s','t','u','v','w','x','y']
for i in nodeNames:
    new_node = graphs.Node(i)
    new_node.key = i
    g.addNode(new_node)

# Consider the following graph from Introduction to Algorithms by Cormen given in Fig. 22.3
# 
#      r --- s   t ----- u
#      |     | /  \      |
#      v     w --- x --- y
# 
# Beginning at node 's', do breadth-first search on the graph to compute the 
# distances from 's' to every other node in the graph.

g.addEdge('s','w',1)
g.addEdge('s','r',1)
g.addEdge('r','v',1)
g.addEdge('w','t',1)
g.addEdge('w','x',1)
g.addEdge('t','x',1)
g.addEdge('t','u',1)
g.addEdge('x','y',1)
g.addEdge('u','x',1)
g.addEdge('u','u',1)

print('------START BFS------')
BFS = breadthFirstSearch(g,g.nodes['s'])
print('------END BFS------')



