import networkx as nx
import doctest

#IMPLEMENTED BY: BAR GOLDENBERG

def get_path(G, source, target):
    path = nx.shortest_path(G, source, target, weight='weight')
    path_with_weights = [(path[i], path[i+1], G[i][i+1]['weight']) for i in range(len(path)-1)]
    return path_with_weights

def get_path_cost(G, source, target):
    path_cost = nx.shortest_path_length(G, source, target, weight='weight')
    return path_cost

def get_sum_without_person(path, source, target):
    ans = 0
    for edge in path:
        if edge[0] == source and edge[1] == target:
            continue
        ans += edge[2]
    return ans

def remove_edge(G, edge):
    G_without_edge = G.copy(as_view=False)
    G_without_edge.remove_edge(edge[0], edge[1])
    return G_without_edge

def calulate_cost(G, source, target, edge, path_with_weights):
    path_cost_without_edge = get_path_cost(G, source, target)
    return -(path_cost_without_edge - get_sum_without_person(path_with_weights, edge[0], edge[1]))
    
def vcg_cheapest_path(G, source, target):
    """
    >>> G = nx.complete_graph(4)
    >>> G[0][1]['weight'] = 3
    >>> G[0][2]['weight'] = 5
    >>> G[0][3]['weight'] = 10
    >>> G[1][2]['weight'] = 1
    >>> G[1][3]['weight'] = 4
    >>> G[2][3]['weight'] = 1
    >>> vcg_cheapest_path(G, 0, 3)
    edge ( 0 , 1 ) cost -4
    edge ( 0 , 2 ) cost 0
    edge ( 0 , 3 ) cost 0
    edge ( 1 , 2 ) cost -2
    edge ( 1 , 3 ) cost 0
    edge ( 2 , 3 ) cost -3

    >>> G = nx.complete_graph(3)
    >>> G[0][1]['weight'] = 3
    >>> G[0][2]['weight'] = 5
    >>> G[1][2]['weight'] = 1
    >>> vcg_cheapest_path(G, 0, 2)
    edge ( 0 , 1 ) cost -4
    edge ( 0 , 2 ) cost 0
    edge ( 1 , 2 ) cost -2
    """
    path_with_weights = get_path(G, source, target)
    edges = G.edges()
    for edge in edges:
        G_without_edge = remove_edge(G, edge)
        cost = calulate_cost(G_without_edge, source, target, edge, path_with_weights)
        print('edge (', edge[0], ",", edge[1], ")", "cost", cost)

if __name__ == "__main__":
    doctest.testmod()
