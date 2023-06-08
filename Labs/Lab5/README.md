# Report on Session 5

## Personal Network Analysis Project

Welcome to the readme file for the Personal Network Analysis Project, specifically focusing on the implementation of a content-based recommender system. This system aims to provide a list of similar songs based on a given song name, creating a seamless music experience that retains the mood or vibe from the previous song.

## Questions Report

### 1. Define the objectives of your study. What question or objectives do you aim to address?

The objective of this study is to analyze the user's preferences and recommend a variety of similar songs that align with their musical tastes. By addressing this objective, we aim to enhance the music listening experience by providing relevant song suggestions.

### 2. Describe the process of data acquisition and the obtained data.

(a) To obtain the data, we utilized the search artist and track IDs, along with the method for retrieving track data from Session 1. By combining these approaches, we obtained the necessary dataframes for each song.

(b) The API endpoints used for data acquisition are the same ones employed in Session 1.

(c) The obtained data consists of a dataframe with rows representing individual tracks. The columns include attributes such as 'track_id', 'duration', 'name', 'popularity', 'danceability', 'energy', 'loudness', 'speechiness', 'acousticness', 'instrumentalness', 'liveness', 'valence', 'tempo', 'album_id', 'album_name', 'album_release_date', 'artist_id', and 'artist_name'.

(d) The volume of collected data consists of 2 records in the dataframe.

(e) The data is stored in a structured format, specifically within a dataframe, allowing for efficient processing and analysis.

### 3. Describe the data preprocessing tasks.

For data preprocessing, we used the same prepocessing we have done in previous sessions. We used the preprocessed dataframe and the preprocessed graphs.

### 4. Describe the data analysis tasks.

(a) The network analysis algorithms utilized in this project include:

- Content-based filtering: This algorithm analyzes the attributes of songs to determine their similarity and generate recommendations based on those similarities.

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
