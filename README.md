# Discord Bot: OwO

## Abilities
Currently this bot is equipped to scrape through a Discord text channel and log messages that include Spotify links. The bot can then add songs, albums, and playlists associated with those links to a desired playlist.

## Libraries
-	*Discord.py*
-	*Spotipy*
-	*CSV*
-	*Datetime*
-	*Plotly*

## Commands

### `GatherSpotifyLinks`
When summoned using this command, the bot will scrape through every message in the given channel and log any messages which contain a Spotify link. The Spotify links and their message details are then stored into a CSV file, populating the following fields,
- Message ID
- Message Author
- Date
- Link Type
- Link

### `AddDataBaseToPlaylist`
The bot will index through a *Spotify Messages* CSV file and extract all of the URIs. URIs are unique identifier codes that are assigned to each song, album, and playlist on spotify. The bot uses the codes to add tracks to the desired playlist. 

#### URI Example
-	LINK: https://open.spotify.com/track/5lXNcc8QeM9KpAWNHAL0iS?si=a64fc4b428be4e0e
-	URI: 5lXNcc8QeM9KpAWNHAL0iS

### `UpdatePlaylist`
The bot will take the most recent message in the CSV file and use it's ID to gather all the messages that have been sent since the last update. Equipped with those new messages, the bot will then parse them for Spotify links, update the database, and then add the new Spotify content to the desired playlist.


## Results

### Playlist
- [Loser Bar Jams](https://open.spotify.com/playlist/3gO4hYyClvG858lBveOkyh?si=cd1fb5a59fc84203)

### Statistics
Using the *Spotify Messages* CSV we can see a breakdown of Spotify links per user,

<p align="center">
  <img src="https://user-images.githubusercontent.com/54219067/201409390-13ec3a30-35f6-4d46-a103-d8692933a0ad.png" width="750">
</p>
