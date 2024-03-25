import outh
import config
import const
import datetime


# プレイリストの作成
def create(user, name):
    print("新規プレイリスト:「" + name + "」を作成します。")
    outh.sp.user_playlist_create(user, name, public=False)

# プレイリストの重複チェック
def check_duplicate(user, name):
    my_playlists = outh.sp.user_playlists(user)["items"]
    for playlist in my_playlists:
        if name == playlist["name"]:
            print("既に「" + name + "」が存在しています")
    create(user, name)

# プレイリストのIDを取得
def get_playlists_id(user, name):
    my_playlists = outh.sp.user_playlists(user)["items"]
    for playlist in my_playlists:
        if name == playlist["name"]:
            return playlist["id"]
    return False

# ユーザー名
user = config.USER_NAME

# プレイリスト名
dt_now = datetime.datetime.now()
year_month = dt_now.strftime('%Y/%m')
name = const.PLAYLIST_NAME + year_month

check_duplicate(user, name)
playlists_id = get_playlists_id(user, name)
