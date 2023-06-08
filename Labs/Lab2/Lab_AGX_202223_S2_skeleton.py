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

import numpy as np

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

    #   We will store the lonely nodes in this list
    nodes_to_prune=[]
    # Iterate over each node in the pruned graph
    for node in prunned_g:
        
        # Append to the Remove list any nodes that have degree 0 after pruning
        if prunned_g.degree(node) == 0:
            nodes_to_prune.append(node)
            
    for node in nodes_to_prune:
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

    audio_features = ['danceability', 'energy', 'loudness', 'speechiness',
                      'acousticness', 'instrumentalness', 'liveness', 'valence', 'tempo']

    # Group tracks by artist and calculate mean audio features for each artist
    artist_means = tracks_df.groupby('artist_id')[audio_features].mean()

    # Merge mean audio features with artist identification data
    artist_audio_features_df = artist_means.merge(tracks_df[['artist_id', 'artist_name']].drop_duplicates(), left_on=None, right_on='artist_id', left_index=True, right_index=False)#, left_index=True)#, right_on='artist')
    
    return artist_audio_features_df
    # ----------------- END OF FUNCTION --------------------- #


from sklearn.metrics import pairwise_distances

def create_similarity_graph(artist_audio_features_df: pd.DataFrame, similarity: str, out_filename: str = 'gw_.graphml') -> nx.Graph:
    """
    Create a similarity graph from a dataframe with mean audio features per artist.

    :param artist_audio_features_df: dataframe with mean audio features per artist.
    :param similarity: the name of the similarity metric to use (e.g. "cosine" or "euclidean").
    :param out_filename: name of the file that will be saved.
    :return: a networkx graph with the similarity between artists as edge weights.
    """
    # ------- IMPLEMENT HERE THE BODY OF THE FUNCTION ------- #
    
    # Compute the pairwise similarity matrix
    similarity_matrix = pairwise_distances(artist_audio_features_df.drop(columns=['artist_id', 'artist_name']).values, metric=similarity)
    
    # Initialize the graph
    G = nx.Graph()
    
    # Add nodes to the graph
    for idx, artist in enumerate(artist_audio_features_df.index):
        G.add_node(artist)
    
    # Add edges to the graph
    for i in range(similarity_matrix.shape[0]):
        for j in range(i+1, similarity_matrix.shape[1]):
            artist_i = artist_audio_features_df.index[i]
            artist_j = artist_audio_features_df.index[j]
            weight = similarity_matrix[i, j]
            
            G.add_edge(artist_i, artist_j, weight=weight)
    
    # Save the graph to a file if out_filename is provided
    if out_filename:
        nx.write_graphml(G, out_filename)
    
    return G
    
    # ----------------- END OF FUNCTION --------------------- #


if __name__ == "__main__":
    # ------- IMPLEMENT HERE THE MAIN FOR THIS SESSION ------- #
    """
    a)Two undirected graphs (g′B and g′D) of artists obtained by applying the programmed function in exercise 1, retrieve 
    bidirectional edges, to the graphs obtained by the crawler in session 1, gB and gD.
    """
    
    # First we load the graph gB and gD from previous session:
    gB = nx.read_graphml('./gB_graph.graphml')
    gD = nx.read_graphml('./gD_graph.graphml')
   
    g_B = retrieve_bidirectional_edges(gB, "g\'B.graphml")
    g_D = retrieve_bidirectional_edges(gD, "g\'D.graphml")
    
    print(f"gB' order = {gB_.order()} \tgB' size = {gB_.size()}\ngD' order = {gD_.order()}\tgD' size = {gD_.size()}")
    
    '''
    b) Two undirected graphs with weights (gwB and gwD) obtained from the similarity between the artists.
    To obtain them, it will be necessary to calculate the vector of average audio features for each artist (compute mean audio features),
    create a similarity graph with these features (create similarity graph), and prune the resulting graph
    (prune low weight edges) to achieve the desired size. Specifically, the size of the graph should be as
    similar as possible to the size of graphs g′B and g′D, respectively.
    '''
    
    # we load the dataframes of gB and gD with track data from previous session:
    gB_track_data = pd.read_csv('./gB_track_data.csv')
    gD_track_data = pd.read_csv('./gD_track_data.csv')
    
    # we get the mean audio features for both dataframes:
    gB_mean_audio_features = compute_mean_audio_features(gB_track_data)
    gD_mean_audio_features = compute_mean_audio_features(gD_track_data)
    
    # now we compute the similarity graph gB and gD that are weighted graphs:
    gB_similarity_graph = create_similarity_graph(gB_mean_audio_features, out_filename='gB_similarity_graph.graphml')
    gD_similarity_graph = create_similarity_graph(gD_mean_audio_features, out_filename='gD_similarity_graph.graphml')
    
    threshold = 0.0035 # we set this threshold to get a graph with similar size to the ones obtained in exercise a)
    
    # we compute the graphs gwB and gwD that are the similarity graphs but prunned with the threshols given.
    gwB = prune_low_weight_edges(gB_similarity_graph, min_weight=threshold, out_filename= 'gwB.graphml')
    gwB = prune_low_weight_edges(gB_similarity_graph, min_weight=threshold, out_filename= 'gwD.graphml')
    
    pass
    # ------------------- END OF MAIN ------------------------ #
