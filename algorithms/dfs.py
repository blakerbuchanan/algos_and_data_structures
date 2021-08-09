# Implement a depth-first search algorithm for tree or graph search 
# This implementation will utilize adjacency lists (probably in the form of a Dictionary)

from datastructures import graphs
from datastructures import slinkedlist

def depthFirstSearchRec(G,v,visited,visitSeq):
    # visited = []
    visited.append(v)
    # visitSeq = []
    visitSeq.append(v.key)

    for u in v.neighbors:
        if u not in visited:
            depthFirstSearchRec(G,u,visited,visitSeq)

    return visitSeq

def depthFirstSearchVisit(G,u,time):
    time += 1
    u.d = time
    u.explored = -1
    for v in u.neighbors:
        if v.explored == 0:
            v.pi = u
            depthFirstSearchVisit(G,v,time)
    
    u.explored = 1
    if G.do_tps == True:
        G.tps.insertNode(u.key)

    print(u.key)
    time += 1

def depthFirstSearch(G):
    
    for node in G:
        node.explored = 0
        node.pi = None
    time = 0

    if G.do_tps == True:
        topo_sort = slinkedlist.LinkedList()
        G.tps = topo_sort

    for node in G:
        if node.explored == 0:
            depthFirstSearchVisit(G,node,time)

    if G.do_tps == True:
        return G.tps
    else:
        return None

if __name__ == "__main__":

    # Consider the following example in Introduction to Algorithms by Cormen (Fig. 22.4)
    #
    #    u --> v     w
    #    |    ^|    ^|
    #    |   / |   / |
    #    |  /  |  /  |
    #    v /   v /   v
    #    x <-- y     z <-|
    #                 \__| 
    #                 
    #                 
    # Do depth-first search on the graph and print the order of node visitation.
    # We expect the order of vistation for depth-first search to be x, y, v, u, z, w

    g = graphs.Graph()

    nodeNames = ['u','v','w','x','y','z']
    for i in nodeNames:
        new_node = graphs.Node(i)
        new_node.key = i
        g.addNode(new_node)

    g.addEdge('u','v',1,True)
    g.addEdge('u','x',1,True)
    g.addEdge('x','v',1,True)
    g.addEdge('y','x',1,True)
    g.addEdge('v','y',1,True)
    g.addEdge('w','y',1,True)
    g.addEdge('w','z',1,True)

    print('------START DFS------')
    DFS = depthFirstSearch(g)
    print('------END DFS------')

    # print('------START DFS------')
    # visited=[]
    # visitSeq=[]
    # finalSeq = depthFirstSearchRec(g,g.nodes[0],visited,visitSeq)
    # print(finalSeq)
    # print('------END DFS------')