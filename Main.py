import discord
from discord.ext import commands

import spotipy
import spotipy.util as util

import csv
from datetime import datetime
from DiscordMessage import *
from SpotifyFunctions import *
from HandleCSVdata import *
from HandleStrings import *
from ConfigHandler import *


###########################################################
### Get Discord/Spotify Account Info from the Config File
###########################################################
ConfigFile          = 'config.txt'
DiscordLinksFile    = 'LoserBarMusic.csv'

DiscordToken        = GrabConfigValue('DISCORD_ID', ConfigFile)

SpotifyUsername     = GrabConfigValue('SPOTIPY_USERNAME', ConfigFile)
SpotifyClientID     = GrabConfigValue('SPOTIPY_CLIENT_ID', ConfigFile)
SpotifyClientSecret = GrabConfigValue('SPOTIPY_CLIENT_SECRET', ConfigFile)
SpotifyRedirectURI  = GrabConfigValue('SPOTIPY_URI', ConfigFile)
SpotifyPlaylist     = GrabConfigValue('SPOTIPY_PLAYLIST',ConfigFile)
SpotifyScope        = "playlist-modify-private"

print('Discord:')
print(' Token: ' + DiscordToken)
print('Spotify:')
print(' Username: ' + SpotifyUsername)
print(' Client ID: ' + SpotifyClientID)
print(' Client Secret: ' + SpotifyClientSecret)
print(' Redirect URI: ' + SpotifyRedirectURI)
print(' Playlist: ' + SpotifyPlaylist)


###########################################################
### Discord Bot Setup/Run
###########################################################
BotPrefix   = "!"
intent      = discord.Intents.all()
bot         = commands.Bot(intents=intent, command_prefix=BotPrefix)

@bot.event
async def on_ready():
    print(f'Logged in as {bot.user.name}!')

@bot.command()
async def test(ctx):
    channel = ctx.channel
    messages = [channel.last_message]
    await channel.delete_messages(messages)

@bot.command()
async def GatherSpotifyLinks(ctx):
    channel = ctx.channel

    commandMessage = [channel.last_message]
    await channel.delete_messages(commandMessage)

    print("Collecting Messages...")

    SpotifyMessages = []
    totalMessageCount = 0
    
    # Grab the discord messages    
    async for message in channel.history(limit=None):
        totalMessageCount += 1
        if ("https://open.spotify.com/" in message.content):
            message.content = remove_emoji(message.content)
            SpotifyMessages.append(message)

            #print(message.content)

    print("Done Collecting!")
    print(f"{totalMessageCount} messages searched")
    print(f"{len(SpotifyMessages)} spotify links found")

    # Extract the URL from each message
    LinkLogs = ParseMessagesForURLS(SpotifyMessages,"https://open.spotify.com/")

    # Update the database with the new link logs
    writeData(LinkLogs, DiscordLinksFile)

    print('All links have been logged!!!')

@bot.command()
async def UpdatePlaylist(ctx):
    channel = ctx.channel

    commandMessage = [channel.last_message]
    await channel.delete_messages(commandMessage)

    # Grab the last message logged
    MostRecentLog = getTopRow(DiscordLinksFile)
    LastMessage   = await channel.fetch_message(int(MostRecentLog[0]))

    # Collect the New Messages
    NewSpotifyMessages = []
    totalMessageCount = 0

    print("Collecting Messages...")

    async for message in channel.history(limit = None, after = LastMessage):
        totalMessageCount += 1

        if ("https://open.spotify.com/" in message.content):
            message.content = remove_emoji(message.content)
            NewSpotifyMessages.append(message)

    print("Done Collecting!")
    print(f"{totalMessageCount} new messages searched")
    print(f"{len(NewSpotifyMessages)} new spotify links found!")

    # Extract the URL from each message
    LinkLogs = ParseMessagesForURLS(NewSpotifyMessages,"https://open.spotify.com/")

    for log in LinkLogs:
        print(log)

    # Update the database with the new link logs
    updateCSV(LinkLogs, DiscordLinksFile)

    # Add the new tracks to the playlist
    SpotifyToken  = util.prompt_for_user_token(SpotifyUsername, SpotifyScope, SpotifyClientID, 
                    SpotifyClientSecret, SpotifyRedirectURI, cache_path=f"__pycache__/.cache-{SpotifyUsername}")

    sp           = spotipy.Spotify(auth=SpotifyToken)

    print("Spotify: signed in as: " + sp.me()['display_name'])

    # Grab the Link types and URLs from the logs
    URLS = []
    LinkTypes = []
    for row in LinkLogs:
        Split = row.split(",")
        URLS.append(Split[4])
        LinkTypes.append(Split[3])

    # Grab the URIs from the URLs
    URIS = ExtractSpotifyURI(URLS)

    # Add the Tracks/Albums/Playlists to the Master Playlist
    print(f'Uploading...')
    for i in range(0,len(LinkTypes)):
        Input = CompileTrackURIS(sp, [URIS[i]], [LinkTypes[i]])
        if len(Input) != 0:
            print(Input)
            sp.user_playlist_add_tracks(SpotifyUsername, SpotifyPlaylist, Input, position=0)
    print('Playlist has been updated')

@bot.command()
async def AddDataBaseToPlaylist(ctx):
    channel = ctx.channel

    commandMessage = [channel.last_message]
    await channel.delete_messages(commandMessage)

    SpotifyToken  = util.prompt_for_user_token(SpotifyUsername, SpotifyScope, SpotifyClientID, 
                    SpotifyClientSecret, SpotifyRedirectURI, cache_path=f"__pycache__/.cache-{SpotifyUsername}")

    sp           = spotipy.Spotify(auth=SpotifyToken)

    print("Spotify: signed in as: " + sp.me()['display_name'])

    # Read in Discord link logs
    Messages = readData(DiscordLinksFile)

    # Grab the Link types and URLs from the logs
    URLS = []
    LinkTypes = []
    for row in Messages:
        URLS.append(row[4])
        LinkTypes.append(row[3])

    # Grab the URIs from the URLs
    URIS = ExtractSpotifyURI(URLS)

    # Add the Tracks/Albums/Playlists to the Master Playlist
    Tracks = CompileTrackURIS(sp, URIS, LinkTypes)

    print(f'{len(Tracks)} Total Songs!!!')
    print(f'Uploading...')

    """ for Track in Tracks:
        Input = [Track]
        sp.user_playlist_add_tracks(SpotifyUsername, SpotifyPlaylist, Input)

    print(f'Playlist Updated!') """

bot.run(DiscordToken)