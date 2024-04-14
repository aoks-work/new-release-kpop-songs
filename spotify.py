import spotipy
from spotipy.oauth2 import SpotifyClientCredentials, SpotifyOAuth
import time
import config
import gsheet
import create_playlist
import outh

sp = outh.sp

print("=======================================")
# アーティストID取得
def get_artist_id(artist_name):
    results = sp.search(q=artist_name, limit=10, type="artist")
    i = 1
    for item in results["artists"]["items"]:
        print(str(i) + ":" + item["name"])
        i += 1
    number = input("アーティスト名番号：")
    id = results["artists"]["items"][int(number)-1]["id"]
    #id = results["artists"]["items"][0]["id"]
    return id

# アルバム情報の取得
def get_artist_albums(artist_id, album_type):
    results = sp.artist_albums(artist_id, album_type=album_type, limit=1)
    print("アルバム情報の取得:" + album_type)
    for item in results["items"]:
        print(item["release_date"] + " : "  + item["name"] + " : " + item["album_type"] + " : " + item["artists"][0]["name"])
        print()
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
    return results

# プレイリストに曲を追加
def add_playlist_track(track):
    print("プレイリストに曲を追加")
    for track_info in track["items"]:
        print(track_info["id"])
        sp.user_playlist_add_tracks(config.USER_NAME, create_playlist.get_playlists_id(), track_info["id"])

# アーティスト名
artist_name = input("アーティスト名：")
# アーティストID
artist_id = get_artist_id(artist_name)
# アルバム情報
album_info = get_artist_albums(artist_id, "album")
# シングル情報
single_info = get_artist_albums(artist_id, "single")

# 最新音源情報
new_release = compare_release_date(album_info, single_info)

track = get_track_info(new_release["uri"])

gsheet.createAlbumInfo(new_release, track)