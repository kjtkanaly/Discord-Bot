# Discord Music Bot: OwO

## Purpose
Go through a Discord text channel and search for every Spotify link and then add those individual songs/albums/playlists to a master playlist. 

## Modules
-	*Discord.py*
-	*Spotipy*
-	*CSV*
-	*Datetime*


## Workflow

### Discord Phase
The initial phase utilizes the Discord API to scrape through a single channel for all the messages that contain Spotify links. The bot will begin this process upon hearing the command `!GatherSpotifyLinks`. The Spotify links are then stored into a CSV file, *DiscordSpotifyLinks.csv*, along with the name of the member who sent the message and the date/time it was sent.

### Spotify Phase
The second phase utilizes the Spotify API to add the tracks/albums/playlists to the master playlist, ‘Loser Bar Jams’. The tracks are added using their unique URIs, which are obtained from the links in the DiscordSpotifyLinks CSV.
URI Example
-	LINK: https://open.spotify.com/track/5lXNcc8QeM9KpAWNHAL0iS?si=a64fc4b428be4e0e
-	URI: 5lXNcc8QeM9KpAWNHAL0iS

## Results

### Playlist
- [Loser Bar Jams](https://open.spotify.com/playlist/3gO4hYyClvG858lBveOkyh?si=cd1fb5a59fc84203)

### Statistics
In additon to the playlist, I can also see a breakdown of spotify links per user,

<p align="center">
  <img src="https://user-images.githubusercontent.com/54219067/201409390-13ec3a30-35f6-4d46-a103-d8692933a0ad.png" width="750">
</p>
