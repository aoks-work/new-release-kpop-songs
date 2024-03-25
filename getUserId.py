import spotipy
from spotipy.oauth2 import SpotifyClientCredentials, SpotifyOAuth
import time
import config

#spotifyインスタンスを作成
# 認証情報を取得するためのオブジェクトを作成
scope = 'user-read-recently-played playlist-read-private playlist-read-collaborative app-remote-control user-read-playback-state user-library-read user-modify-playback-state playlist-modify-public playlist-modify-private'
redirect_uri="http://localhost:8080"
sp_oauth = SpotifyOAuth(client_id=config.CLIENT_ID,
                        client_secret=config.CLIENT_SECRET,
                          redirect_uri=redirect_uri, scope=scope)

# ユーザーに認証を求めるために認証ページのURLを表示
auth_url = sp_oauth.get_authorize_url()
print(auth_url)

# ユーザーが認証後、自動的にアクセストークンを取得
token_info = sp_oauth.get_cached_token()
if not token_info:
    response = input("Enter the URL you were redirected to: ")
    code = sp_oauth.parse_response_code(response)
    token_info = sp_oauth.get_access_token(code)

# アクセストークンを取得し、認証オブジェクトを作成
token = token_info['access_token']
sp = spotipy.Spotify(auth=token)  # sp変数を定義

#playlists = sp.current_user_playlists()

# results = sp.search(q="LE SSERAFIM", limit=1, type="track")
# print(type(results))
#pprint.pprint(results)
# print(di['items']['name'])


print("=======================================")
# アーティストID取得
def get_artist_id(artist_name):
    results = sp.search(q=artist_name, limit=3, type="artist")
    for item in results["artists"]["items"]:
        print(item["name"])
    #print(results["artists"]["items"])
    id = results["artists"]["items"][0]["id"]
    #print("artist_id:" + id)
    return id

# アルバム情報の取得
def get_artist_albums(artist_id, album_type):
    results = sp.artist_albums(artist_id, album_type=album_type, limit=1)
    for item in results["items"]:
        print(item["name"] + " : " + item["release_date"])
    # リリース形態(アルバム・シングル)が存在しない場合はfalse
    return results["items"][0] if any(results["items"]) else False

# シングルとアルバムのリリース日比較
def compare_release_date(album, single):
  # どちらかのリリース形態(アルバム・シングル)が存在しない場合は比較しない
  if not album:
    return single
  elif not single:
    return album

  # 比較
  formatted_album_date = time.strptime(album["release_date"], "%Y-%m-%d")
  formatted_single_date = time.strptime(single["release_date"], "%Y-%m-%d")
  return album if formatted_album_date >= formatted_single_date else single

# アルバムのトラック名取得
def get_track_info(albums_uri):
    results = sp.album_tracks(albums_uri)
    for item in results["items"]:
        print(item["name"])

# メイン

# # アーティスト名
# artist_name = input("アーティスト名：")
# # アーティストID
# artist_id = get_artist_id(artist_name)
# # アルバム情報
# album_info = get_artist_albums(artist_id, "album")
# # シングル情報
# single_info = get_artist_albums(artist_id, "single")

# # 最新音源情報
# new_release = compare_release_date(album_info, single_info)
# get_track_info(new_release["uri"])

print(sp.user("たしまん"))