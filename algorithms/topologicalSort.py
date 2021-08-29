from datastructures import graphs
from datastructures import slinkedlist
from dfs import *

def topologicalSort(G):
    
    G.do_tps = True
    # Call depth-first search to compute finishing times for each node in graph
    # As each vertex is finished, insert it into the front of a linked list
    DFS = depthFirstSearch(G)
    topo_sort = G.tps

    # Return the linked list of vertices
    return topo_sort

if __name__ == "__main__":

    # Consider the example given in Fig. 22.7 of Introduction to Algorithms by Cormen
    # 
    #     undershorts      socks
    #          |       \     |
    #          |        \    |     watch
    #          |         \   |
    #          v          v  v
    #        pants  ---->  shoes
    #          |    shirt
    #          |   /  |
    #          v v    v
    #        belt    tie
    #          \      |
    #           \     v
    #            >  jacket
    # 
    # Return a topological sort of the above graph

    g = graphs.Graph()

    node_names = ['undershorts', 'socks', 'watch', 'pants', 'shoes', 'shirt', 'belt', 'tie', 'jacket']
    for i in node_names:
        new_node = graphs.Node(i)
        new_node.key = i
        g.addNode(new_node)  

    # Build the graph
    g.addEdge('undershorts','pants',1,True)
    g.addEdge('undershorts','shoes',1,True)
    g.addEdge('socks','shoes',1,True)
    g.addEdge('pants','shoes',1,True)
    g.addEdge('pants','belt',1,True)
    g.addEdge('shirt','belt',1,True)
    g.addEdge('shirt','tie',1,True)
    g.addEdge('belt','jacket',1,True)
    g.addEdge('tie','jacket',1,True)

    print('------START TOPOLOGICAL SORT------')
    topo_sort = topologicalSort(g)
    print('------END TOPOLOGICAL SORT------')
    
    # Print topological sort. Note that the resulting topological sort for the example above
    # is valid, but is not the topological sort given in the Cormen example.
    node = topo_sort.head
    while node:
        print('Item: ' + str(node.val.key))
        print('Finish time: ' + str(node.val.fin_time))
        node = node.next