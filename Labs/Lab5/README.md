# Report on Session 5

## Personal Network Analysis Project

## Idea: Recommender System:

The idea was to implement a content based recommender system that receives a graph annd a song name and provides a list of similar songs that you should like if you liked the given song. 

## Questions Report: 

1. Define the objectives of your study. What question or objectives do you aim to address? 
We are looking at the user side of things and offering a plethora of similar songs so that despite changing songs, it would still retain the mood or vibe that they carried with the last song. 

2. Describe the process of data acquisition and the obtained data. 
(a) Explain how you obtained the data (e.g., search criteria or crawler scheduling algorithm).
We reused the search artist and track ids and the further added the method to get track data from session 1 in order to get the dataframes that we could use for each song. 


(b) Which API endpoints did you use to acquire the data? The same ones we used in session 1.

(c) Describe the obtained data. For graphs, describe the type of graph used, what the nodes and edges represent, and their attributes. For tabular data, describe the collected entities and their attributes.

Each row is a track and the rows are 'track_id', 'duration', 'name', 'popularity', 'danceability', 'energy', 'loudness', 'speechiness', 'acousticness', 'instrumentalness', 'liveness', 'valence', 'tempo', 'album_id', 'album_name', 'album_release_date', 'artist_id' and 'artist_name'
 
(d) Indicate the volume of collected data. For graphs, provide the size and order. For tabular data, provide the number of records. 2 

(e) Detail the format used to store the data. 

3. Describe the data preprocessing tasks. 
We made a normalized version of the dataframe dropping the columns that were strings or dates and then using sklearn min max scaler to normalize it so all values would have the same weight.

4. Describe the data analysis tasks. 
(a) What network analysis algorithms did you use? 

5. Describe the visualization tasks. 
(a) What tools did you use to generate the visualizations? 
(b) What parameters or configurations did you use? 
(c) What problems did you encounter, and how did you solve them? 

6. Answer the initial question using the results of the performed analyses and generated visualizations. 


## Example of Results

| Recommended songs if you liked [Calling (Spider-Man: Across the Spider-Verse)](https://open.spotify.com/track/5rurggqwwudn9clMdcchxT?si=6f92fc189caa4c12) ![maxresdefault](https://github.com/Neilus03/Spotiflyers/assets/87651732/2a037263-1cc1-4e2e-9035-eda7bb59fc89)
| -----------|
| [No Idea, Don Toliver](https://open.spotify.com/track/7AzlLxHn24DxjgQX73F9fU?si=d92ad7280ed64ec4) |
![No Idea](https://github.com/Neilus03/Spotiflyers/assets/122691083/7a8c2ddb-8a0f-4175-8c5c-c4b544de413d)
| [ALL MINE](https://open.spotify.com/track/3U21A07gAloCc4P7J8rxcn?si=6f51abe5d6554e6a) |
![download](https://github.com/Neilus03/Spotiflyers/assets/87651732/91561cd0-aff7-4503-8823-9725e1562679)
| [Love Don't Change](https://open.spotify.com/track/6PmjWl0phNxc0R5OwkDdiZ?si=8feb2d0a357b43b5) |
![maxresdefault1](https://github.com/Neilus03/Spotiflyers/assets/87651732/bae7bbd5-8da6-4bf9-88d5-2010bd0af0f0)
| [Suicidal (feat. Juice WRLD) - Remix](https://open.spotify.com/track/4S2uhQE8L9V6p7rj7SiauJ?si=0d81034d0ec14050) |
![download (1)](https://github.com/Neilus03/Spotiflyers/assets/87651732/a5dec48a-02f5-4e08-ab25-3c7c990875f5)
| [Right My Wrongs](https://open.spotify.com/track/5rgrBsAFYMun6yhtnLKRPz?si=bdfe4ff735c84580) |
![rmo](https://github.com/Neilus03/Spotiflyers/assets/122691083/733179dc-e61d-4ee8-a30e-be25618135a1)
|[ Mixed Personalities (feat. Kanye West)](https://open.spotify.com/track/6vWEAOUSxohKxhp0K1BsxL?si=c9ececee29064e9a) |
![68570943ab5b404ae5dc3ddac7d4118c 1000x1000x1](https://github.com/Neilus03/Spotiflyers/assets/87651732/aff0c431-d881-4ee6-8016-2731b27c54e0)
| [Come Through (feat. Chris Brown)](https://open.spotify.com/track/3krZxyBsWEHfEfJegYaWTd?si=e746387b646f4391) |
![maxresdefault2](https://github.com/Neilus03/Spotiflyers/assets/87651732/0551ea00-88be-42c1-b8b9-de2f47ddda0d)
| [B.S. (feat. H.E.R.)](https://open.spotify.com/track/63wx9vdskaXbYxyDx4oJCZ?si=159cf9fa5dcb4bc0) |
![artworks-cs9wKrxx9Cfw-0-t500x500](https://github.com/Neilus03/Spotiflyers/assets/87651732/81234e15-8183-4672-81f7-43d58e18c698)
| [Annihilate (Spider-Man: Across the Spider-Verse)](https://open.spotify.com/track/39MK3d3fonIP8Mz9oHCTBB?si=338beab264d54ae1) |
![download (2)](https://github.com/Neilus03/Spotiflyers/assets/87651732/ed6238c9-1043-471c-a33c-c8232b757394)


We can clearly see that this songs are actually so related. Afroamerican styles mixed. 
