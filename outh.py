import spotipy
from spotipy.oauth2 import SpotifyClientCredentials, SpotifyOAuth
import time
import config

#spotifyインスタンスを作成
# 認証情報を取得するためのオブジェクトを作成
scope = 'playlist-read-private playlist-read-collaborative playlist-modify-private user-library-read playlist-modify-public '
redirect_uri="http://localhost:8080"
sp_oauth = SpotifyOAuth(client_id=config.CLIENT_ID,
                        client_secret=config.CLIENT_SECRET,
                          redirect_uri=redirect_uri, scope=scope)

# ユーザーに認証を求めるために認証ページのURLを表示
auth_url = sp_oauth.get_authorize_url()
#print(auth_url)

# ユーザーが認証後、自動的にアクセストークンを取得
token_info = sp_oauth.get_cached_token()
if not token_info:
    response = input("Enter the URL you were redirected to: ")
    code = sp_oauth.parse_response_code(response)
    token_info = sp_oauth.get_access_token(code)

# アクセストークンを取得し、認証オブジェクトを作成
token = token_info['access_token']
sp = spotipy.Spotify(auth=token)  # sp変数を定義