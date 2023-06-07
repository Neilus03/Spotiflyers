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
    pass
    # ----------------- END OF FUNCTION --------------------- #


if __name__ == "__main__":
    # ------- IMPLEMENT HERE THE MAIN FOR THIS SESSION ------- #
    
    '''
    1) Indicate the number of nodes shared by the graphs gB and fB (seeds Drake
       and the last crawled artist from the DFS crawl, respectively); and gB and hB 
       (seeds Drake and French Montana, respectively). Use the function num_common_nodes.
       Compare the number of common nodes with the results obtained from calling
       the create similarity graph function.
    '''
    #CODE HERE
    '''
    2) Calculate the 25 most central nodes in the graph g'B using both degree centrality
       and betweenness centrality. How many nodes are there in common between the two sets?
       Explain what information this gives us about the analyzed graph.
    '''
    #CODE HERE
    '''
    3) Find cliques of size greater than or equal to min size clique in the
       graphs g'B and g'D. Thes value of the variable min size clique will depend on the
       graph. Choose the maximum value that generates at least 2 cliques. Indicate the
       value you chose for min size clique and the total number of cliques you found for
       each size. Calculate and indicate the total number of different nodes that are part
       of all these cliques and compare the results from the two graphs.
    '''
    #CODE HERE
    '''
    4) Find cliques of size greater than or equal to min size clique in the graphs g'B and g'D.
       The value of the variable min size clique will depend on the graph. Choose the maximum 
       value that generates at least 2 cliques. Indicate the value you chose for min size clique
       and the total number of cliques you found for each size. Calculate and indicate the total
       number of different nodes that are part of all these cliques and compare the results from
       the two graphs.
    '''
    #CODE HERE
    '''
    5) Choose one of the cliques with the maximum size and analyze the artists that are part
       of it. Try to find some characteristic that defines these artists and explain it.
    '''
    #CODE HERE

    # ------------------- END OF MAIN ------------------------ #
