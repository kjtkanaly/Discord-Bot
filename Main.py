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

            print(message.content)

            SpotifyMessages.append(message)

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

    # First Grab the top link in the database

    # Iterate through the discord messages until you find that link

    # Once you find it 


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
    URLS = []
    LinkTypes = []

    # Grab the Link types and URLs from the logs
    for row in Messages:
        URLS.append(row[3])
        LinkTypes.append(row[2])

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