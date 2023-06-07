import networkx as nx
import pandas as pd

# ------- IMPLEMENT HERE ANY AUXILIARY FUNCTIONS NEEDED ------- #
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
auth_manager = SpotifyClientCredentials(client_id='04861c6a3a184ab29403dcdf74848158',client_secret='6f8b0da3c7e2496c9a421469d96a379d')
sp = spotipy.Spotify ( auth_manager = auth_manager )


playlists = sp.user_playlists ('spotify')
while playlists :
    for i , playlist in enumerate ( playlists ['items']) :
        print ("%4d %s %s" % ( i + 1 + playlists ['offset'] , playlist ['uri'] ,playlist ['name']) )
    if playlists ['next']:
        playlists = sp . next ( playlists )
    else :
        playlists = None

# --------------- END OF AUXILIARY FUNCTIONS ------------------ #


def search_artist(artist_name: str) -> str:
    """
    Search for an artist in Spotify.

    :param artist_name: name to search for.
    :return: spotify artist id.
    """
    # ------- IMPLEMENT HERE THE BODY OF THE FUNCTION ------- #
    
    # Search for the artist
    result = sp.search(artist_name, type='artist')

    # Return the first artist id from the search results
    return result['artists']['items'][0]['id']
    
    # ----------------- END OF FUNCTION --------------------- #


def crawler(seed: str, max_nodes_to_crawl: int, strategy: str = "BFS", out_filename: str = "g.graphml") -> nx.DiGraph:
    """
    Crawl the Spotify artist graph, following related artists.

    :param seed: starting artist id.
    :param max_nodes_to_crawl: maximum number of nodes to crawl.
    :param strategy: BFS or DFS.
    :param out_filename: name of the graphml output file.
    :return: networkx directed graph.
    """
    # ------- IMPLEMENT HERE THE BODY OF THE FUNCTION ------- #
    
    #Initializing first variables
    G = nx.DiGraph()
    expanded_nodes = set()
    expanded_counter = 0 # Number of nodes expanded
    nodes2expand = [seed]
    
    # DFS Strategy
    if strategy=="DFS":
      
      # Start loop that lasts until we meet the target of nodes to crawl or we run out of nodes
      while (expanded_counter <= max_nodes_to_crawl) and nodes2expand:
        #print(expanded_counter)
        current_artist = nodes2expand.pop()# The id from which we are taking related artists right now
        
        if current_artist not in expanded_nodes: #If they are not expanded already we can add them.
            expanded_nodes.add(current_artist) #update nodes
            expanded_counter += 1 #update counter

            # Get the related artists of the current node
            related_artists = sp.artist_related_artists(current_artist)['artists'] #Take related artists
            for related_artist in related_artists:
                artist_id = related_artist['id']
                G.add_edge(current_artist, artist_id)
                if artist_id not in expanded_nodes:
                        nodes2expand.append(artist_id) #extend the list of nodes to expand.

            if expanded_counter > max_nodes_to_crawl: #If we exceed the max, no need to continue, break the loop.
                break

    #BFS STRATEGY
    elif strategy == "BFS":
        #The loop lasts until we run out of nodes to expand or we meet our max of nodes to crawl
        while expanded_counter <= max_nodes_to_crawl and nodes2expand:
            current_artist = nodes2expand.pop(0)        
            # If the current node was already expanded, skip it
            if current_artist in expanded_nodes: # If it already has been expanded, pass to the next iteration.
                continue
            expanded_nodes.add(current_artist) #update nodes list
            expanded_counter+=1 #Update counter
            if expanded_counter>max_nodes_to_crawl: # If we reached max nodes, break the loop, no need to go further.
              break
            related_artists = sp.artist_related_artists(current_artist)['artists'] #We take the related artists
            for related_artist in related_artists:
                artist_id = related_artist['id']
                G.add_edge(current_artist, artist_id)
                if artist_id not in expanded_nodes:
                        nodes2expand.append(artist_id)
            
    else: #We should put this, just in case.
      print("ERROR: PLEASE USE BFS OR DFS. Returned empty graph")
      return nx.DiGraph()

    for artist in G.nodes: #Add all the relevant info
        artist_data = sp.artist(artist)
        G.nodes[artist]["name"]=artist_data["name"]
        G.nodes[artist]["id"]=artist_data["id"]
        G.nodes[artist]["followers"]=artist_data["followers"]['total']
        G.nodes[artist]["popularity"]=artist_data["popularity"]
        G.nodes[artist]["genres"]=str(artist_data["genres"])

    nx.write_graphml(G, out_filename)
    
    return G

    # ----------------- END OF FUNCTION --------------------- #


def get_track_data(graphs: list, out_filename: str) -> pd.DataFrame:
    """
    Get track data for each visited artist in the graph.

    :param graphs: a list of graphs with artists as nodes.
    :param out_filename: name of the csv output file.
    :return: pandas dataframe with track data.
    """
    # ------- IMPLEMENT HERE THE BODY OF THE FUNCTION ------- #
    track_data = []
    
    for G in graphs:
        for node in G.nodes():
            # Get the top tracks of the artist in Spain
            top_tracks = sp.artist_top_tracks(node, country='ES')

            for track in top_tracks['tracks']:
                # Get the audio features of the track
                audio_features = sp.audio_features(track['id'])[0]

                track_data.append({
                    'track_id': track['id'],
                    'duration': track['duration_ms'],
                    'name': track['name'],
                    'popularity': track['popularity'],
                    'danceability': audio_features['danceability'],
                    'energy': audio_features['energy'],
                    'loudness': audio_features['loudness'],
                    'speechiness': audio_features['speechiness'],
                    'acousticness': audio_features['acousticness'],
                    'instrumentalness': audio_features['instrumentalness'],
                    'liveness': audio_features['liveness'],
                    'valence': audio_features['valence'],
                    'tempo': audio_features['tempo'],
                    'album_id': track['album']['id'],
                    'album_name': track['album']['name'],
                    'album_release_date': track['album']['release_date'],
                    'artist_id': node,
                    'artist_name': G.nodes[node]['name']
                })
    
    top_tracks_df = pd.DataFrame(track_data)
    top_tracks_df.to_csv(out_filename, index=False)
    
    return top_tracks_df
    # ----------------- END OF FUNCTION --------------------- #


if __name__ == "__main__":
    # ------- IMPLEMENT HERE THE MAIN FOR THIS SESSION ------- #
    
    ## Exercises to test the functions:

    ''' 
    a) A graph of related artists starting with the artist Drake
       and exploring 200 artists with BFS (we will call this graph gB).
    '''
    gB = crawler(search_artist('Drake'), max_nodes_to_crawl=200, strategy='BFS', out_filename='gB_graph.graphml')

    '''this code is to plot the graph gB
    # Set up layout and draw the graph
    pos = nx.spring_layout(gB)

    labels = nx.get_node_attributes(gB, "name")  # Extract the "name" attribute as labels

    # Process labels to escape "$" characters
    labels = {k: r'{}'.format(v.replace("$", "\$")) for k, v in labels.items()}

    # Display the graph
    nx.draw(gB, pos, with_labels=True, labels=labels, node_color='lightblue', edge_color='gray')
    '''
    
    # getting the order and size of gB for the report questions:
    print('gB order: {}\ngB size: {}\n'.format(gB.order(), gB.size()))

    '''
    b) A graph of related artists starting with the artist Drake
       and exploring 200 artists with DFS (we will call this graph gD).
    '''

    gD = crawler(search_artist('Drake'), max_nodes_to_crawl=200, strategy='DFS', out_filename='gD_graph.graphml')

    '''this code is to plot the graph gD
    # Set up layout and draw the graph
    pos = nx.spring_layout(gD)

    labels = nx.get_node_attributes(gD, "name")  # Extract the "name" attribute as labels
    # Process labels to escape "$" characters
    labels = {k: r'{}'.format(v.replace("$", "\$")) for k, v in labels.items()}
    
    # Display the graph
    nx.draw(gD, pos=pos, with_labels=True, labels=labels, node_color='lightblue', edge_color='gray')
    '''
    
    # getting the order and size of gB for the report questions:
    print('gD order: {}\ngD size: {}\n'.format(gD.order(), gD.size()))

    '''
    c) A dataset of songs from all the explored artists that appear 
       in any of the previous graphs (we will call this dataset D).
    '''
    
    songs_data = get_track_data([gB, gD], 'top_track.csv')

    '''
    d) A graph of related artists starting with the artist French Montana
       and exploring 200 artists with BFS (we will call this graph hB).
    '''
    
    hB = crawler(search_artist('French Montana'), max_nodes_to_crawl=200, strategy='BFS', out_filename='graph_HB.graphml')

    '''
    e) A graph of related artists starting with the last crawled artist from 
       gD and exploring 200 artists with BFS (we will call this graph fB).
    '''

    last_crawled_node_in_gD = list(gD.nodes())[-1]

    fB = crawler(last_crawled_node_in_gD, max_nodes_to_crawl=200, strategy='BFS', out_filename='graph_FB.graphml')

    # ------------------- END OF MAIN ------------------------ #
