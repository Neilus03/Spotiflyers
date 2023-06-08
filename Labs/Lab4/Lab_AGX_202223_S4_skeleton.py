import pandas as pd
import networkx as nx
import matplotlib.pyplot as plt
import random
from sklearn.metrics.pairwise import *
import seaborn as sns 
impor numpy as np

from Lab_AGX_202223_S1_skeleton import *
from Lab_AGX_202223_S2_skeleton import *
from Lab_AGX_202223_S3_skeleton import *

# ------- IMPLEMENT HERE ANY AUXILIARY FUNCTIONS NEEDED ------- #


# --------------- END OF AUXILIARY FUNCTIONS ------------------ #

def plot_degree_distribution(degree_dict: dict, normalized: bool = False, loglog: bool = False) -> None:
    """
    Plot degree distribution from dictionary of degree counts.

    :param degree_dict: dictionary of degree counts (keys are degrees, values are occurrences).
    :param normalized: boolean indicating whether to plot absolute counts or probabilities.
    :param loglog: boolean indicating whether to plot in log-log scale.
    """
    # ------- IMPLEMENT HERE THE BODY OF THE FUNCTION ------- #

    # Extract degrees and their counts from the dictionary
    degrees = list(degree_dict.keys())
    counts = list(degree_dict.values())

    # If normalized is True, convert counts to probabilities
    if normalized:
        total_count = sum(counts)
        counts = [count / total_count for count in counts]

    # Create the plot
    plt.figure()
    if loglog:
        # Plot in log-log scale
        plt.loglog(degrees, counts, 'bo', markersize=4, c='red')
        plt.xlabel('Degree (log scale)')
        plt.ylabel('Probability' if normalized else 'Count (log scale)')
    else:
        # Plot in linear scale
        plt.plot(degrees, counts, 'bo', markersize=4, c='green')
        plt.xlabel('Degree')
        plt.ylabel('Probability' if normalized else 'Count')

    plt.title('Degree Distribution')
    plt.show()
    # ----------------- END OF FUNCTION --------------------- #

def plot_audio_features(artists_audio_feat: pd.DataFrame, artist1_id: str, artist2_id: str) -> None:
    """
    Plot a (single) figure with a plot of mean audio features of two different artists.

    :param artists_audio_feat: dataframe with mean audio features of artists.
    :param artist1_id: string with id of artist 1.
    :param artist2_id: string with id of artist 2.
    :return: None
    """
    # ------- IMPLEMENT HERE THE BODY OF THE FUNCTION ------- #
    
    # Assuming the dataframe is indexed by artist_id and columns represent audio features
    artist1_features = artists_audio_feat.loc[artist1_id]
    artist2_features = artists_audio_feat.loc[artist2_id]

    # Create the plot
    plt.figure()
    x = range(len(artist1_features))
    plt.bar(x, artist1_features, width=0.4, label=artist1_id, color='b', align='center')
    plt.bar(x, artist2_features, width=0.4, label=artist2_id, color='r', align='edge')
    plt.xlabel('Features')
    plt.ylabel('Mean Value')
    plt.title('Audio Features Comparison')
    plt.xticks(x, artist1_features.index, rotation='vertical')
    plt.legend()
    plt.tight_layout()
    plt.show()
    # ----------------- END OF FUNCTION --------------------- #

    
def plot_similarity_heatmap(artist_audio_features_df: pd.DataFrame, similarity: str, out_filename: str = None) -> None:
    """
    Plot a heatmap of the similarity between artists.

    :param artist_audio_features_df: dataframe with mean audio features of artists.
    :param similarity: string with similarity measure to use.
    :param out_filename: name of the file to save the plot. If None, the plot is not saved.
    """
    # ------- IMPLEMENT HERE THE BODY OF THE FUNCTION ------- #
    
    # Assuming a similarity matrix where each cell (i,j) contains the similarity between artist i and j
    if similarity not in ['cosine', 'euclidean', 'manhattan']:
        raise ValueError('Invalid similarity measure. Choose between "cosine", "euclidean", "manhattan".')

    # Compute similarity matrix
    if similarity == 'cosine':
        similarity_matrix = cosine_similarity(artist_audio_features_df.values)
    elif similarity == 'euclidean':
        similarity_matrix = euclidean_distances(artist_audio_features_df.values)
    else:
        similarity_matrix = manhattan_distances(artist_audio_features_df.values)

    # Create the plot
    plt.figure(figsize=(10, 10))
    sns.heatmap(similarity_matrix, xticklabels=artist_audio_features_df.index, yticklabels=artist_audio_features_df.index, cmap='viridis')
    plt.title('Artists Similarity Heatmap')
    
    # Save the plot
    if out_filename is not None:
        plt.savefig(out_filename)
    plt.show()
    # ----------------- END OF FUNCTION --------------------- #

if __name__ == "__main__":
    # ------- IMPLEMENT HERE THE MAIN FOR THIS SESSION ------- #
    
    degree_dict_gB = dict(gB.degree())
    degree_dict_gD = dict(gD.degree())
    degree_dict_gwB = dict(gwB.degree())
    degree_dict_gwD = dict(gwD.degree())
    
    '''
    (a) Generate the plots of the degree distribution of the graphs g'B, g'D, and gwB.
        Configure the normalized and loglog parameters to generate the best possible
        visualization according to your criteria.
    '''
    print('Degree distribution of gB:\n')
    plot_degree_distribution(degree_dict_gB, normalized=True, loglog=False)
    print('Degree distribution of gD:\n')
    plot_degree_distribution(degree_dict_gD, normalized=True, loglog=False)
    print('Degree distribution of gwB:\n')
    plot_degree_distribution(degree_dict_gwB, normalized=True, loglog=False)

    
    '''
    (b) Select the artist that is most similar to Drake from gB and generate a comparison
        using the plot audio features function.
    '''
    drake_index = artists_audio_feat.index.get_loc(drake_id)
    most_similar_artist_index = np.argmax(similarity_matrix[drake_index])
    most_similar_artist_id = artists_audio_feat.index[most_similar_artist_index]

    # Generate a comparison using the plot audio features function
    plot_audio_features(artists_audio_feat, drake_id='3TVXtAsR1Inumwj472S9r4', most_similar_artist_id)
    
    
    '''
    (c) Select the artist that is less similar to Drake from gB and generate a comparison
        using the plot audio features function.
    '''
    drake_index = artists_audio_feat.index.get_loc(drake_id)
    least_similar_artist_index = np.argmin(similarity_matrix[drake_index])
    least_similar_artist_id = artists_audio_feat.index[least_similar_artist_index]

    # Generate a comparison using the plot audio features function
    plot_audio_features(artists_audio_feat, drake_id='3TVXtAsR1Inumwj472S9r4', least_similar_artist_id)
    
    
    '''
    (d) Generate a heatmap showing the similarity between all artists in your dataset
        using the plot similarity heatmap function.
    '''
    plot_similarity_heatmap(artists_audio_feat, 'cosine')
    

    # ------------------- END OF MAIN ------------------------ #
