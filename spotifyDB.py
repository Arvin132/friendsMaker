import spotipy as sp
from spotipy.oauth2 import SpotifyOAuth




class spotify_d_b_viewer :
    APP_ID = "c61c9103785e474fa471829cc58cd5dd"
    APP_SECRET = "68841be161b946019c0f0a3fb08f991d"
    redirect_uri : list[str] = [
        "http://example.com/"
    ]
    credential_manager : SpotifyOAuth
    spotify_ref : sp.Spotify

    def __init__(self) :
        self.credential_manager = SpotifyOAuth(client_id= self.APP_ID, client_secret= self.APP_SECRET, redirect_uri= "http://example.com/", scope= "user-library-read")
        self.spotify_ref = sp.Spotify(auth_manager= self.credential_manager)
    
    def print_playlist_of_user(self ,username: str):
        playlists = self.spotify_ref.user_playlist(user= username)

        for playlist in playlists['items']:
            print(playlist['name'])