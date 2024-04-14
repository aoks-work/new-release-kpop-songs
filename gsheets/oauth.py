import gspread
import os

dir_path = os.path.dirname(__file__) # 作業フォルダの取得
gc = gspread.oauth(
                   credentials_filename=os.path.join(dir_path, "client_secret.json"), # 認証用のJSONファイル
                   authorized_user_filename=os.path.join(dir_path, "authorized_user.json"), # 証明書の出力ファイル
                   )