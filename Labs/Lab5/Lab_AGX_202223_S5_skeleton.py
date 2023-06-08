import networkx as nx
import pandas as pd
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.preprocessing import MinMaxScaler
import numpy as np
from Lab_AGX_202223_S1_skeleton import *
from Lab_AGX_202223_S2_skeleton import *
from Lab_AGX_202223_S3_skeleton import *
from Lab_AGX_202223_S4_skeleton import *
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
auth_manager = SpotifyClientCredentials(client_id='778ae223cf3a4a0cb5ecabff86c97888',client_secret='dbf631d78bae4f2c85aaba5110fb2a06')
sp = spotipy.Spotify ( auth_manager = auth_manager )


def recommend_tracks(track_df, track_name, top_n=10):
    """
    This function recommends tracks based on a given track id.
    """

    # Normalize the track features so that all the features have equal importance
    scaler = MinMaxScaler()
    track_df_scaled = scaler.fit_transform(track_df.drop(columns=['track_id', 'name', 'artist_id', 'artist_name', 'album_name', 'album_id', 'album_release_date']))

    # Calculate cosine similarity between track features
    cosine_sim = cosine_similarity(track_df_scaled, track_df_scaled)

    # Get the index of the track that matches the track id
    idx = track_df[track_df['name'] == track_name].index[0]

    # Get the pairwsie similarity scores of all tracks with that track
    sim_scores = list(enumerate(cosine_sim[idx]))

    # Sort the tracks based on the similarity scores
    sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)

    # Get the scores of the top-n most similar tracks
    sim_scores = sim_scores[1:top_n+1]

    # Get the track indices
    track_indices = [i[0] for i in sim_scores]
    track_df=track_df.loc[track_indices]

    # Get the column indices
    track_df=track_df[['name', 'artist_name']]
    

    # Return the top-n most similar tracks
    return track_df
