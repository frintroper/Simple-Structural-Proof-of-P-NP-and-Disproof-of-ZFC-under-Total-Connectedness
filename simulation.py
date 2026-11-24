import networkx as nx

def connectedness_score(G: nx.Graph) -> float:
    n = G.number_of_nodes()
    if n < 2:
        return 1.0
    max_edges = n * (n - 1) / 2
    return G.number_of_edges() / max_edges

def complexity_score(G: nx.Graph) -> float:
    return 1.0 - connectedness_score(G)

if __name__ == "__main__":
    K = nx.complete_graph(5)
    P = nx.path_graph(5)
    print("Complete:", connectedness_score(K), complexity_score(K))
    print("Path:", connectedness_score(P), complexity_score(P))
