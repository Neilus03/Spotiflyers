import networkx as nx
import pandas as pd
import numpy as np

from Lab_AGX_202223_S2_skeleton import *

# ------- IMPLEMENT HERE ANY AUXILIARY FUNCTIONS NEEDED ------- #


# --------------- END OF AUXILIARY FUNCTIONS ------------------ #

def retrieve_bidirectional_edges(g: nx.DiGraph, out_filename: str) -> nx.Graph:
    """
    Convert a directed graph into an undirected graph by considering bidirectional edges only.

    :param g: a networkx digraph.
    :param out_filename: name of the file that will be saved.
    :return: a networkx undirected graph.
    """
    # ------- IMPLEMENT HERE THE BODY OF THE FUNCTION ------- #
    
    # Create an empty undirected graph
    new_g = nx.Graph()

    # Iterate over all edges of the input graph
    for u, v in g.edges():
        # Check if the reverse edge exists in the input graph
        if g.has_edge(v, u):
            # If the reverse edge exists, add an undirected edge to the output graph
            new_g.add_edge(u, v)

    # Save the graph to a file
    nx.write_graphml(new_g, out_filename)

    return new_g
    # ----------------- END OF FUNCTION --------------------- #


def prune_low_degree_nodes(g: nx.Graph, min_degree: int, out_filename: str) -> nx.Graph:
    """
    Prune a graph by removing nodes with degree < min_degree.

    :param g: a networkx graph.
    :param min_degree: lower bound value for the degree.
    :param out_filename: name of the file that will be saved.
    :return: a pruned networkx graph.
    """
    # ------- IMPLEMENT HERE THE BODY OF THE FUNCTION ------- #
    
    # Make a copy of the input graph. This is done to avoid altering the original graph.
    prunned_g = g.copy()

    # List to store the nodes to be pruned
    nodes_to_prune = []

    # Iterate over each node in the graph
    for node in prunned_g:

        # If the degree of the node is less than the specified minimum degree, add it to the list of nodes to be pruned
        if prunned_g.degree(node) < min_degree:
            nodes_to_prune.append(node)

    # Iterate over the list of nodes to be pruned
    for node in nodes_to_prune:

        # Remove each node from the graph
        prunned_g.remove_node(node)

    # Iterate over each node in the pruned graph
    for node in prunned_g:

        # Remove any nodes that have degree 0 after pruning
        if prunned_g.degree(node) == 0:
            prunned_g.remove_node(node)
    
    # Write the pruned graph to a file in the GraphML format
    nx.write_graphml(prunned_g, out_filename)

    # Return the pruned graph
    return prunned_g
    # ----------------- END OF FUNCTION --------------------- #


def prune_low_weight_edges(g: nx.Graph, min_weight=None, min_percentile=None, out_filename: str = None) -> nx.Graph:
    """
    Prune a graph by removing edges with weight < threshold. Threshold can be specified as a value or as a percentile.

    :param g: a weighted networkx graph.
    :param min_weight: lower bound value for the weight.
    :param min_percentile: lower bound percentile for the weight.
    :param out_filename: name of the file that will be saved.
    :return: a pruned networkx graph.
    """
    # ------- IMPLEMENT HERE THE BODY OF THE FUNCTION ------- #
    
    # Check if at least one lower bound is specified
    if (min_weight == None) and (min_percentile == None):

        #if no bound is specified raise an error
        raise ValueError("Unspecified bound, please sepecify either min_weight or min_percentile")

    #Check if both bounds are specified
    elif (min_weight != None) and (min_percentile !=None):

        #If so, raise an error 
        raise ValueError("Too many specified bounds, please sepecify only one of { min_weight, min_percentile}")

    # Make a copy of the input graph. This is done to avoid altering the original graph.
    prunned_g = g.copy()

    # List to store the nodes to be pruned
    edges_to_prune = []

    #List to store weights
    weights = [data['weight'] for u, v, data in prunned_g.edges(data=True)]

    # Check If the argument min_percentile is not None
    if min_percentile !=None:
        #If so use np.percentile to get the threshold weight
        min_weight = np.percentile(weights, min_percentile)

    #iterate over the nodes in the graph
    for u, v, data in prunned_g.edges(data=True):
        
        #get their weight
        weight = data['weight']
        
        #check if the weight of the edge is lower than the threshold
        if weight < min_weight:

            #if so, add the edge to the edges_to_prune list
            edges_to_prune.append((u,v))

    # Iterate over the list of edges to be pruned
    for u,v in edges_to_prune:

        # Remove each edge from the graph
        prunned_g.remove_edge(u,v)

    # Iterate over each node in the pruned graph
    for node in prunned_g:

        # Remove any nodes that have degree 0 after pruning
        if prunned_g.degree(node) == 0:
            prunned_g.remove_node(node)
    
    # Write the pruned graph to a file in the GraphML format
    nx.write_graphml(prunned_g, out_filename)

    # Return the pruned graph
    return prunned_g
   
    # ----------------- END OF FUNCTION --------------------- #


def compute_mean_audio_features(tracks_df: pd.DataFrame) -> pd.DataFrame:
    """
    Compute the mean audio features for tracks of the same artist.

    :param tracks_df: tracks dataframe (with audio features per each track).
    :return: artist dataframe (with mean audio features per each artist).
    """
    # ------- IMPLEMENT HERE THE BODY OF THE FUNCTION ------- #
    pass
    # ----------------- END OF FUNCTION --------------------- #


def create_similarity_graph(artist_audio_features_df: pd.DataFrame, similarity: str, out_filename: str = None) -> \
        nx.Graph:
    """
    Create a similarity graph from a dataframe with mean audio features per artist.

    :param artist_audio_features_df: dataframe with mean audio features per artist.
    :param similarity: the name of the similarity metric to use (e.g. "cosine" or "euclidean").
    :param out_filename: name of the file that will be saved.
    :return: a networkx graph with the similarity between artists as edge weights.
    """
    # ------- IMPLEMENT HERE THE BODY OF THE FUNCTION ------- #
    pass
    # ----------------- END OF FUNCTION --------------------- #


if __name__ == "__main__":
    # ------- IMPLEMENT HERE THE MAIN FOR THIS SESSION ------- #
    pass
    # ------------------- END OF MAIN ------------------------ #
