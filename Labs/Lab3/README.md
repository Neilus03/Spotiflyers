# Report on Session 3: Data Analysis

## Introduction
During this third session, we will perform some analysis of the data we have preprocessed in  the previous sessions, analysis that will be useful to validate our functions from previous sessions.

## Questions

1. Indicate the number of nodes shared by the graphs gB and fB (seeds Drake and the last crawled artist from the DFS crawl, respectively); and gB and hB (seeds Drake and French Montana, respectively). Use the function num common nodes. Compare the number of common nodes with the results obtained from calling the create similarity graph function.
```
    Number of common nodes between gB and fB: 38

    Number of common nodes between gB and hB: 500
```

2. Calculate the 25 most central nodes in the graph g′B using both degree centrality and betweenness centrality. How many nodes are there in common between the two sets? Explain what information this gives us about the analyzed graph:

```
  Number of common nodes between most central nodes (degree and betweenness): 2, his suggests that nodes that are highly 
  connected locally (high degree centrality)are generally not the same ones that act as bridges between different parts of
  the network (high betweenness centrality). The nodes with high degree centrality could be artists that are commonly co-listened
  with a large number of other artists, indicating a wide appeal across different listener groups. On the other hand, the nodes
  with high betweenness centrality might be artists that serve as 'bridges' between different genres or styles of music, being
  common in playlists that transition between these styles.
```

3. Find cliques of size greater than or equal to min size clique in the graphs g’B and g′D. The value of the variable min size clique will depend on the graph. Choose the maximum value that generates at least 2 cliques. Indicate the value you chose for min size clique and the total number of cliques you found for each size. Calculate and indicate the total number of different nodes that are part of all these cliques and compare the results from the two graphs.

```
    Number of cliques in gB with size >= 2: 199

    Number of nodes in these cliques in gB: 188

    Number of cliques in gD with size >= 2: 237

    Number of nodes in these cliques in gD: 189
```

4. Choose one of the cliques with the maximum size and analyze the artists that are part of it. Try to find some characteristic that defines these artists and explain it.
```

The maximum clique for gB with 7 nodes is: Yung Joc, Rocko, Young Dro, Shawty Lo, Boyz N Da Hood, U.S.D.A. and Rich Boy

The maximum clique for gD with 10 nodes is: Mondo Rock, The Black Sorrows, Choirboys, Skyhooks, Australian Crawl, GANGgajang, Models, Stevie Wright, Richard Clapton and Baby Animals.

The first clique consists in hip hop and rap artists from Southerm United States. They've been known to collaborate with one another, suggesting a well-connected network within their specific genre and regional scene.

The second clique consists in mostly of rock and pop bands from Australia. Their music often features a distinct Australian identity and the experiences of the Australian urban and suburban lifestyle. Their connection could be due to their shared nationality, genre, and era of peak activity.

```

5. Detect communities in the graph gD. Explain which algorithm and parameters you used, and what is the modularity of the obtained partitioning. Do you consider the partitioning to be good?

```
The communities found in graph D where calculated with louvain method and they are:

community: 1
Drake
Lil Wayne
Nicki Minaj
DJ Khaled

community: 2
J. Cole
Kendrick Lamar
Wale
Big Sean

community: 3
The Weeknd
PartyNextDoor
Majid Jordan
DVSN

community: 4
Rihanna
Beyonce
Chris Brown
Alicia Keys

community: 5
Travis Scott
Future
Young Thug
Migos

community: 6
Jay Z
Kanye West
Nas
Pusha T

community: 7
Tyga
Yg
2 Chainz
French Montana

community: 8
Justin Bieber
Shawn Mendes
Charlie Puth
Post Malone

community: 9
Meek Mill
Rick Ross
T.I.
Ludacris

We got a modularity of 0.742.

We consider that this partitions make sense since they form groups of similar artist.
```

6. Suppose that Spotify recommends artists based on the graphs obtained by the crawler (gB or gD). While a user is listening to a song by an artist, the player will randomly select a recommended artist (from the successors of the currently listened artist in the graph) and add a song by that artist to the playback queue.

(a) Suppose you want to launch an advertising campaign through Spotify. Spotify allows playing advertisements when listening to music by a specific artist. To do this, you have to pay 100 euros for each artist to which you want to add ads. What is the minimum cost you have to pay to ensure that a user who listens to music infinitely will hear your ad at some point? The user can start listening to music by any artist (belonging to the obtained graphs). Provide the costs for the graphs gB and gD, and justify your answer.

```
77600 euros for graph gB 
69900 euros for graph gD

The cost for gB is bigger since it has more nodes than graph gD.
```

(b) Suppose you only have 400 euros for advertising. Which selection of artists ensures a better spread of your ad? Indicate the selected artists and explain the reason for the selection for the graphs gB and gD.

```
The selected artists for gB are: Young Dro, Yo Gotti, Yung Joc and Lil Scrappy.
The selected artists for gD are: Tim Bowman, Steve Cole, Urban Knights and Joyce Cooling.

These artist where selected because they have low degree so they are cheaper. 
```

7. Consider a recommendation model similar to the previous one, in which the player shows the user a set of other artists (defined by the successors of the currently listened artist in the graph), and the user can choose which artist to listen to from that set. Assume that users are familiar with the recommendation graph, and in this case, the gB graph is always used.

(a) If you start by listening to the artist Young Dro and your favorite artist is Travis Porter, how many hops will you need at minimum to reach it? Give an example of the artists you would have to listen to in order to reach it.

  The minimum number of hops are 4. You should listen to this artist in this order:
```   
    Young Dro
    
    Rocko
    
    Yo Gotti
    
    Young Money
    
    Travis Porter
```  
