# Implement a breadth-first search algorithm for tree or graph search 
# This implementation will utilize adjacency lists (probably in the form of a Dictionary)
import graphs 

# def BFS1(s, G):
#     level = {s:0}
#     parent = {s:None}
#     i = 1
#     frontier = [s] # level i-1 (invariant)
#     while frontier:
#         next = [] # level i
#         for u in frontier:
#             for v in G[u]:
#                 if v not in level:
#                     level[v] = i
#                     parent[v] = u
#                     next.append(v)
        
#         frontier = next
#         i += 1

def BFS2(G, root):
    # Let Q be a queue
    Q = []
    visited = []
    visitSeq = []
    visited.append(root)
    visitSeq.append(root.key)
    root.explored = 1
    Q.append(root)
    while Q:
        v = Q.pop(0)
        # print(v)
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
print(BFS2(g,g.nodes[0]))
print('------END BFS------')


