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
        v = Q.pop(0)
        # If v is goal state then return v
        for u in v.neighbors:
            # print(u)
            if u not in visited:
                u.explored = 1
                visited.append(u)
                visitSeq.append(u.key)
                Q.append(u)
    
    return visited

# Test out the above code
g = graphs.Graph()
for i in range(6):
    g.addNode(graphs.Node(i))

# print(g.nodes)

g.addEdge(0,1,1)
g.addEdge(0,2,1)
g.addEdge(1,3,1)
g.addEdge(1,4,1)
g.addEdge(2,5,1)
g.addEdge(4,5,1)

print('------START BFS------')
print(breadthFirstSearch(g,g.nodes[0]))
print('------END BFS------')


