import networkx as nx
from Lab_AGX_202223_S1_skeleton import *
from Lab_AGX_202223_S2_skeleton import *
# ------- IMPLEMENT HERE ANY AUXILIARY FUNCTIONS NEEDED ------- #


# --------------- END OF AUXILIARY FUNCTIONS ------------------ #

def num_common_nodes(*arg):
    """
    Return the number of common nodes between a set of graphs.

    :param arg: (an undetermined number of) networkx graphs.
    :return: an integer, number of common nodes.
    """
    # ------- IMPLEMENT HERE THE BODY OF THE FUNCTION ------- #
    
    # Check if there is at least one graph
    if len(arg) == 0:
        return 0

    # Collect all nodes from all graphs into a list of sets
    nodes_sets = [set(graph.nodes()) for graph in arg]

    # Find the intersection of all sets, i.e. the common nodes
    common_nodes = set.intersection(*nodes_sets)

    return len(common_nodes)
    # ----------------- END OF FUNCTION --------------------- #

def get_degree_distribution(g: nx.Graph) -> dict:
    """
    Get the degree distribution of the graph.

    :param g: networkx graph.
    :return: dictionary with degree distribution (keys are degrees, values are number of occurrences).
    """
    # ------- IMPLEMENT HERE THE BODY OF THE FUNCTION ------- #
    
    # Calculate the degree of each node in the graph
    degrees = [g.degree(node) for node in g]

    # Initialize a dictionary to count the number of nodes for each degree
    degree_dist = {deg: 0 for deg in set(degrees)}

    # Count the number of nodes for each degree
    for deg in degrees:
        degree_dist[deg] +=1

    # Return the degree distribution
    return degree_dist
    # ----------------- END OF FUNCTION --------------------- # #

def get_k_most_central(g: nx.Graph, metric: str, num_nodes: int) -> list:
    """
    Get the k most central nodes in the graph.

    :param g: networkx graph.
    :param metric: centrality metric. Can be (at least) 'degree', 'betweenness', 'closeness' or 'eigenvector'.
    :param num_nodes: number of nodes to return.
    :return: list with the top num_nodes nodes with the specified centrality.
    """
    # ------- IMPLEMENT HERE THE BODY OF THE FUNCTION ------- #
    
    # Compute the centrality scores for all nodes using the appropriate metric
    if metric == 'degree':
        centrality_scores = nx.degree_centrality(g)
    elif metric == 'betweenness':
        centrality_scores = nx.betweenness_centrality(g)
    elif metric == 'closeness':
        centrality_scores = nx.closeness_centrality(g)
    elif metric == 'eigenvector':
        centrality_scores = nx.eigenvector_centrality(g)
    else:
        raise ValueError("Invalid centrality metric")

    # Sort the nodes by their centrality scores in descending order
    sorted_nodes = sorted(centrality_scores, key=centrality_scores.get, reverse=True)

    # Return the top num_nodes nodes
    return sorted_nodes[:num_nodes]
    # ----------------- END OF FUNCTION --------------------- #


def find_cliques(g: nx.Graph, min_size_clique: int) -> tuple:
    """
    Find cliques in the graph g with size at least min_size_clique.

    :param g: networkx graph.
    :param min_size_clique: minimum size of the cliques to find.
    :return: two-element tuple, list of cliques (each clique is a list of nodes) and
        list of nodes in any of the cliques.
    """
    # ------- IMPLEMENT HERE THE BODY OF THE FUNCTION ------- #
    
    # Find all cliques in the graph using NetworkX's find_cliques function
    all_cliques = list(nx.find_cliques(g))

    # Filter out the cliques that are smaller than min_size_clique
    large_cliques = [clique for clique in all_cliques if len(clique) >= min_size_clique]

    # Get a list of all nodes that are in any of the large cliques
    nodes_in_cliques = list(set(node for clique in large_cliques for node in clique))

    return (large_cliques, nodes_in_cliques)

    # ----------------- END OF FUNCTION --------------------- #



def detect_communities(g: nx.Graph, method: str) -> tuple:
    """
    Detect communities in the graph g using the specified method.

    :param g: a networkx graph.
    :param method: string with the name of the method to use. Can be (at least) 'givarn-newman' or 'louvain'.
    :return: two-element tuple, list of communities (each community is a list of nodes) and modularity of the partition.
    """
    # ------- IMPLEMENT HERE THE BODY OF THE FUNCTION ------- #
 
    if method == "girvan-newman":
        communities = list(nx.community.girvan_newman(g))
    elif method == "louvain":
        partition = community.best_partition(g)
        communities = [[] for _ in range(max(partition.values()) + 1)]
        for node, community_id in partition.items():
            communities[community_id].append(node)
    else:
        raise ValueError("Invalid community detection method. Supported methods: girvan-newman, louvain.")

    modularity = community.modularity(partition, g) if method == "louvain" else None
    return communities, modularity

    # ----------------- END OF FUNCTION --------------------- #

    
#--------AUXILIARIES-----------#
def calculate_advertising_cost(graph):
    """
    This function calculates the cost of advertising 
    on Spotify given a graph of artists.
    """
    # Number of artists in the graph
    num_artists = len(graph.nodes()) 
    cost_per_artist = 100  # The cost of advertising per artist

    # Total cost
    total_cost = num_artists * cost_per_artist

    return total_cost
#----------end of auxiliaries----------#
    
if __name__ == "__main__":
    # ------- IMPLEMENT HERE THE MAIN FOR THIS SESSION ------- #
    
    '''
    1) Indicate the number of nodes shared by the graphs gB and fB (seeds Drake
       and the last crawled artist from the DFS crawl, respectively); and gB and hB 
       (seeds Drake and French Montana, respectively). Use the function num_common_nodes.
       Compare the number of common nodes with the results obtained from calling
       the create similarity graph function.
    '''
    
    gB = nx.read_graphml('/content/gB.graphml')
    hB = nx.read_graphml('/content/hB.graphml')
    fB = nx.read_graphml('/content/fB.graphml')

    common_nodes_gB_fB = num_common_nodes(gB, fB)
    print(f"Number of common nodes between gB and fB: {common_nodes_gB_fB}")

    common_nodes_gB_hB = num_common_nodes(gB, hB)
    print(f"Number of common nodes between gB and hB: {common_nodes_gB_hB}")


    '''
    2) Calculate the 25 most central nodes in the graph g'B using both degree centrality
       and betweenness centrality. How many nodes are there in common between the two sets?
       Explain what information this gives us about the analyzed graph.
    '''

    gB_undirected = nx.read_graphml('/content/g\'B.graphml')
    gD_undirected = nx.read_graphml('/content/g\'D.graphml')

    most_central_nodes_degree = get_k_most_central(gB_undirected, 'degree', 25)
    most_central_nodes_betweenness = get_k_most_central(gB_undirected, 'betweenness', 25)
    common_central_nodes = set(most_central_nodes_degree).intersection(most_central_nodes_betweenness)
    print(f"Number of common nodes between most central nodes (degree and betweenness): {len(common_central_nodes)}")

    '''
    3) Find cliques of size greater than or equal to min size clique in the
       graphs g'B and g'D. Thes value of the variable min size clique will depend on the
       graph. Choose the maximum value that generates at least 2 cliques. Indicate the
       value you chose for min size clique and the total number of cliques you found for
       each size. Calculate and indicate the total number of different nodes that are part
       of all these cliques and compare the results from the two graphs.
    '''
    
    min_size_clique_in_gB = min(len(clique) for clique in list(nx.find_cliques(gB_undirected)))
    min_size_clique_in_gD = min(len(clique) for clique in list(nx.find_cliques(gD_undirected)))
    
    cliques_gB, nodes_in_cliques_gB = find_cliques(gB_undirected, min_size_clique_in_gD)
    print(f"Number of cliques in gB with size >= {min_size_clique_in_gB}: {len(cliques_gB)}")
    print(f"Number of nodes in these cliques in gB: {len(nodes_in_cliques_gB)}")

    cliques_gD, nodes_in_cliques_gD = find_cliques(gD_undirected, min_size_clique_in_gD)
    print(f"Number of cliques in gD with size >= {min_size_clique_in_gD}: {len(cliques_gD)}")
    print(f"Number of nodes in these cliques in gD: {len(nodes_in_cliques_gD)}")

    '''
    4) Choose one of the cliques with the maximum size and analyze the artists that are part
       of it. Try to find some characteristic that defines these artists and explain it.
    '''
    
    # Get the size of the largest clique
    max_size = max(len(clique) for clique in cliques_gB)

    # Get one of the cliques of this size
    max_clique = next(clique for clique in cliques_gB if len(clique) == max_size)

    print("Max size clique in gB:", max_clique)

    # Repeat for gD
    max_size = max(len(clique) for clique in cliques_gD)
    max_clique = next(clique for clique in cliques_gD if len(clique) == max_size)

    print("Max size clique in gD:", max_clique)

    '''
    5. (0.5 points) Detect communities in the graph gD. Explain which algorithm and
    parameters you used, and what is the modularity of the obtained partitioning. Do
    you consider the partitioning to be good?
    '''
    
    communities_gD, modularity_gD = detect_communities(gD_undirected, 'louvain')  # or 'girvan-newman'
    print(f"Communities in gD: {communities_gD}, Modularity: {modularity_gD}")
    
    '''
    6. (1 point) Suppose that Spotify recommends artists based on the graphs obtained by
    the crawler (gB or gD). While a user is listening to a song by an artist, the player
    will randomly select a recommended artist (from the successors of the currently
    listened artist in the graph) and add a song by that artist to the playback queue.
    
    (a) Suppose you want to launch an advertising campaign through Spotify. Spotify
    allows playing advertisements when listening to music by a specific artist. To
    do this, you have to pay 100 euros for each artist to which you want to add
    ads. What is the minimum cost you have to pay to ensure that a user who
    listens to music infinitely will hear your ad at some point? The user can start
    listening to music by any artist (belonging to the obtained graphs). Provide
    the costs for the graphs gB and gD, and justify your answer.
    '''
    
    print(calculate_advertising_cost(gB),'euros for gB')
    print(calculate_advertising_cost(gD), 'euros for gD')
    
    
    '''
    (b) Suppose you only have 400 euros for advertising. Which selection of artists
    ensures a better spread of your ad? Indicate the selected artists and explain
    the reason for the selection for the graphs gB and gD.
    '''
    
    #CODE HERE
    
    '''
    7. (1 point) Consider a recommendation model similar to the previous one, in which
    the player shows the user a set of other artists (defined by the successors of the
    currently listened artist in the graph), and the user can choose which artist to listen
    to from that set. Assume that users are familiar with the recommendation graph,
    and in this case, the gB graph is always used.

    (a) If you start by listening to the artist Young Dro and your favorite artist is
    Travis Porter, how many hops will you need at minimum to reach it? Give an
    example of the artists you would have to listen to in order to reach it.
    '''
    
    # Get the shortest path from Young Dro to Travis Porter

    Young_Dro = '3ZooCJzNMTLpmJaIRUEorI' # ID
    Travis_Porter = '6z1cicLMt9XArxN10q7m8a' #ID
    path = nx.shortest_path(gB, Young_Dro, Travis_Porter)

    print("Shortest path from Young Dro to Travis Porter:", path)
    print("Number of hops:", len(path) - 1)


    # ------------------- END OF MAIN ------------------------ #
