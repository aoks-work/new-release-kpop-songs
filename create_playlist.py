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
            return
    create(user, name)

# プレイリストのIDを取得
def get_playlists_id():
    user = config.USER_NAME
    name = get_playlist_name()
    my_playlists = outh.sp.user_playlists(user)["items"]
    for playlist in my_playlists:
        if name == playlist["name"]:
            return playlist["id"]
    return False


def get_playlist_name():
    # プレイリスト名
    dt_now = datetime.datetime.now()
    year_month = dt_now.strftime('%Y/%m')
    return const.PLAYLIST_NAME + year_month




# ユーザー名
user = config.USER_NAME
playlist_id = get_playlists_id()


# プレイリストの作成
#check_duplicate(user, get_playlist_name())

# print("playlists_id:" + str(get_playlists_id()))
# #spotify:track:2Xiaplc23BureS4EDeE8xa
# #{'uris': ['spotify:track:2Xiaplc23BureS4EDeE8xa']}
# item_list = ["2Xiaplc23BureS4EDeE8xa"]
# outh.sp.playlist_replace_items(playlist_id="6AFWom5UvD4LgxWiNiEkb8", items=item_list)
#playlists_id = get_playlists_id(user, get_playlist_name())
