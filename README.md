# Discord Music Bot: OwO

## Purpose
Go through a Discord text channel and search for every Spotify link and then add those songs/albums/playlists to a master playlist. 

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
