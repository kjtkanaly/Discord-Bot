import spotipy

#####################################################################
# Compile a URI list of every track assosciated with the passed URIs
def CompileTrackURIS(sp, URIS, LinkTypes):
    Tracks = []
    URI_Count = 0

    for Type in LinkTypes:
        if (Type == 'track'):
            Tracks.append(URIS[URI_Count])

        elif (Type == 'album'):
            AlbumTracks = []
            Results = sp.album_tracks(URIS[URI_Count])
            AlbumTracks.extend(Results['items'])

            for AlbumTrack in AlbumTracks:
                print(AlbumTrack['name'] + ": " + AlbumTrack['id'])
                Tracks.append(AlbumTrack['id'])

        elif (Type == 'playlist'):
            PlaylistTracks = []
            Results = sp.playlist_tracks(URIS[URI_Count])
            PlaylistTracks.extend(Results['items'])

            for PlaylistTrack in PlaylistTracks:
                print(PlaylistTrack['track']['name'] + ": " + PlaylistTrack['track']['id'])
                Tracks.append(PlaylistTrack['track']['id'])

        else:
            print('Unexpected Link type Incountered')
            print(Type + ": " + URIS[URI_Count])

        URI_Count += 1

    return Tracks
    
#####################################################################

#####################################################################
# Extract the unique URI from each passed URl
def ExtractSpotifyURI(URLS):
    URIS = []

    for URL in URLS:
        Split = URL.split('/')
        Split = Split[len(Split)-1].split('?')
        URI = Split[0]
        URIS.append(URI)

    return URIS
#####################################################################


