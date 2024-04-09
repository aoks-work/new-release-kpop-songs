import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
import config
import outh
import datetime
import oauth
from create_playlist import playlist_id

# プレイリストに曲を追加
def add_playlist_track(track_list):
    print("プレイリストに曲を追加")
    sp.playlist_replace_items(playlist_id=playlist_id, items=track_list)

sp = outh.sp
gc = oauth.gc

sheet_id = config.SHEET_ID

# ワークシート名
dt_now = datetime.datetime.now()
new_ws_name = str(dt_now.month) + "月"

# スプレッドシートに書き込み
wb = gc.open_by_key(sheet_id) # test02のファイルを開く(キーから)
ws = wb.worksheet(new_ws_name)
all_data = ws.get_all_values()
total_track = len(all_data)
track_list = []

for i in range(2, total_track):
    print(all_data[i][5])
    track_list.append(all_data[i][5])

# プレイリスト追加
add_playlist_track(track_list)
#print(len(ws.get_all_values()))

