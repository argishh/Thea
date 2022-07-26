import spotipy
import webbrowser
import random


def play_random_song():
    username = 'your_spotify_username'                  # Removed for privacy
    clientID = 'your_client_id'                         # Removed for privacy
    clientSecret = 'your_client_secret_id'              # Removed for privacy

    redirect_uri = 'http://google.com/callback/'

    oauth_object = spotipy.SpotifyOAuth(clientID, clientSecret, redirect_uri)
    token_dict = oauth_object.get_access_token()
    token = token_dict['access_token']
    spotifyObject = spotipy.Spotify(auth=token)
    user_name = spotifyObject.current_user()


    playlist = spotifyObject.playlist('https://open.spotify.com/playlist/0oXheeTXFnhb93yCG8mlPn')   # This is my old playlist. You can change the url to your desired playlist.
    songs_dict = playlist['tracks']
    song_items = songs_dict['items']
    # print(song_items[0])

    random_song = random.randint(1,len(song_items)-1)
    song = song_items[random_song]["track"]['external_urls']['spotify']
    webbrowser.open(song)

    return 0


# Understanding the variable 'song_items':                          # Took me a while to figure this out xD it was complicated to read in the terminal output

"""
{'album': 
    
    {'album_type': 'compilation', 
        'artists': [{'external_urls': {'spotify': 'https://open.spotify.com/artist/0LyfQWJT6nXafLPZqxe9Of'}, 'href': 'https://api.spotify.com/v1/artists/0LyfQWJT6nXafLPZqxe9Of', 'id': '0LyfQWJT6nXafLPZqxe9Of', 'name': 'Various Artists', 'type': 'artist', 'uri': 'spotify:artist:0LyfQWJT6nXafLPZqxe9Of'}], 
        'available_markets': ['AE', 'AR', 'AT', 'AU', 'BE', 'BG', 'BH', 'BO', 'BR', 'CA', 'CH', 'CI', 'CL', 'CO', 'CR', 'CW', 'CY', 'CZ', 'DE', 'DK', 'DO', 'DZ', 'EC', 'EE', 'EG', 'ES', 'FR', 'GB', 'GH', 'GR', 'GT', 'HK', 'HN', 'HR', 'HU', 'ID', 'IE', 'IL', 'IN', 'IS', 'IT', 'JP', 'KE', 'KH', 'KR', 'KW', 'LB', 'LK', 'LT', 'LU', 'LV', 'MA', 'MT', 'MX', 'MY', 'NG', 'NI', 'NL', 'NO', 'NZ', 'OM', 'PA', 'PE', 'PH', 'PL', 'PT', 'PY', 'QA', 'RO', 'RS', 'SA', 'SG', 'SI', 'SK', 'SV', 'TH', 'TR', 'TT', 'TW', 'UA', 'US', 'UY', 'VE', 'VN', 'XK', 'ZA'], 
        'external_urls': {'spotify': 'https://open.spotify.com/album/00l07keCeRj9d3WTp4elo2'}, 
        'href': 'https://api.spotify.com/v1/albums/00l07keCeRj9d3WTp4elo2', 'id': '00l07keCeRj9d3WTp4elo2', 
        'images': [{'height': 640, 'url': 'https://i.scdn.co/image/ab67616d0000b273bea614bbb1be9dbfc026dd1e', 'width': 640}, {'height': 300, 'url': 'https://i.scdn.co/image/ab67616d00001e02bea614bbb1be9dbfc026dd1e', 'width': 300}, {'height': 64, 'url': 'https://i.scdn.co/image/ab67616d00004851bea614bbb1be9dbfc026dd1e', 'width': 64}], 
        'name': 'Summer songs 2020 - Best summer music', 
        'release_date': '2020-05-29', 
        'release_date_precision': 'day', 
        'total_tracks': 34, 
        'type': 'album', 
        'uri': 'spotify:album:00l07keCeRj9d3WTp4elo2'
    }, 
    

    'artists': [{'external_urls': {'spotify': 'https://open.spotify.com/artist/1Hsdzj7Dlq2I7tHP7501T4'}, 
                 'href': 'https://api.spotify.com/v1/artists/1Hsdzj7Dlq2I7tHP7501T4', 
                 'id': '1Hsdzj7Dlq2I7tHP7501T4', 
                 'name': 'Niall Horan', 
                 'type': 'artist', 'uri': 
                 'spotify:artist:1Hsdzj7Dlq2I7tHP7501T4'}, 
                 {'external_urls': {'spotify': 'https://open.spotify.com/artist/6WY7D3jk8zTrHtmkqqo5GI'}, 
                 'href': 'https://api.spotify.com/v1/artists/6WY7D3jk8zTrHtmkqqo5GI', 'id': '6WY7D3jk8zTrHtmkqqo5GI', 
                 'name': 'Maren Morris', 'type': 'artist', 'uri': 'spotify:artist:6WY7D3jk8zTrHtmkqqo5GI'}],

    'available_markets': ['AE', 'AR', 'AT', 'AU', 'BE', 'BG', 'BH', 'BO', 'BR', 'CA', 'CH', 'CI', 'CL', 'CO', 'CR', 'CW', 'CY', 'CZ', 'DE', 'DK', 'DO', 'DZ', 'EC', 'EE', 'EG', 'ES', 'FR', 'GB', 'GH', 'GR', 'GT', 'HK', 'HN', 'HR', 'HU', 'ID', 'IE', 'IL', 'IN', 'IS', 'IT', 'JP', 'KE', 'KH', 'KR', 'KW', 'LB', 'LK', 'LT', 'LU', 'LV', 'MA', 'MT', 'MX', 'MY', 'NG', 'NI', 'NL', 'NO', 'NZ', 'OM', 'PA', 'PE', 'PH', 'PL', 'PT', 'PY', 'QA', 'RO', 'RS', 'SA', 'SG', 'SI', 'SK', 'SV', 'TH', 'TR', 'TT', 'TW', 'UA', 'US', 'UY', 'VE', 'VN', 'XK', 'ZA'], 

    'disc_number': 1, 
    'duration_ms': 185280, 
    'episode': False, 
    'explicit': False, 
    'external_ids': {'isrc': 'USUG11701395'}, 

    # This is what we want ("external_urls['spotify']" which is the Link to the song):
    'external_urls': {'spotify': 'https://open.spotify.com/track/4PZryKTHuRWsNasel6MXE7'},
 
    'href': 'https://api.spotify.com/v1/tracks/4PZryKTHuRWsNasel6MXE7', 
    'id': '4PZryKTHuRWsNasel6MXE7', 
    'is_local': False, 
    'name': 'Seeing Blind', 
    'popularity': 8, 
    'preview_url': 'https://p.scdn.co/mp3-preview/3b39920792ab0a341f32ae89b3c74a00e6b73f35?cid=c105241be1354e39ad6649e078a1cd4c', 
    'track': True, 
    'track_number': 18, 
    'type': 'track', 
    'uri': 'spotify:track:4PZryKTHuRWsNasel6MXE7'}

"""