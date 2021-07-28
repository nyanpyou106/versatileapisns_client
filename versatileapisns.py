import urllib.request
import json
import datetime

def utc_to_jst(timestamp_utc):
    # 時間は2021-07-28T04:54:27.869+00:00の形で表示されるのでJSTに変換する
    # https://dev.classmethod.jp/articles/python-time-string-timezone/
    datetime_utc = datetime.datetime.strptime(timestamp_utc, "%Y-%m-%dT%H:%M:%S.%f%z")
    datetime_jst = datetime_utc.astimezone(datetime.timezone(datetime.timedelta(hours=+9)))
    timestamp_jst = datetime.datetime.strftime(datetime_jst, '%Y-%m-%d %H:%M:%S')
    return timestamp_jst

def print_all_userinformation():
    request = urllib.request.Request("https://versatileapi.herokuapp.com/api/user/all")
    all_users_binary = urllib.request.urlopen(request)
    all_users = json.load(all_users_binary)
    for i in all_users:
        name = ""
        user_id = ""
        created_at = ""
        updated_at = ""
        description = ""

        if("name" in i):
            name = i["name"]
        if("_user_id" in i):
            user_id = i["_user_id"]
        if("_created_at" in i):
            created_at = i["_created_at"]
        if("_updated_at" in i):
            updated_at = i["_updated_at"]
        if("description" in i):
            description = i["description"]
        
        
        user_data = "アカウント名:{}\nuser_id:{}\n作成日時:{} 更新日時:{}\n自己紹介:{}".format(
            name, user_id, created_at, updated_at, description
        )
        print("************************")
        print(user_data)
        print("************************\n")

def get_userid_name():
    request = urllib.request.Request("https://versatileapi.herokuapp.com/api/user/all")
    all_users_binary = urllib.request.urlopen(request)
    all_users = json.load(all_users_binary)
    userid_name_dic = {}
    for i in all_users:
        name = ""
        user_id = ""

        if("name" in i):
            name = i["name"]
        if("_user_id" in i):
            user_id = i["_user_id"]
        
        userid_name_dic[user_id] = name
    return userid_name_dic

def post_message(MESSAGE):
    # 投稿内容はjsonにしてPOSTする
    post_json = {"text" : MESSAGE}
    # bytesに変換
    post_json = json.dumps(post_json).encode("utf-8")
    request = urllib.request.Request("https://versatileapi.herokuapp.com/api/text", data=post_json, headers={"Authorization":"HelloWorld"})
    response = urllib.request.urlopen(request)
    print("*投稿完了*")
    USERID_NAME_DIC = get_userid_name()
    print_posted_text(5, USERID_NAME_DIC)

def print_posted_text(GET_MESSAGE_NUM, USERID_NAME_DIC):
    # 最新GET_MESSAGE_NUM件を取得
    request = urllib.request.Request("https://versatileapi.herokuapp.com/api/text/all?$orderby=_created_at%20desc&$limit={}".format(GET_MESSAGE_NUM))
    all_text_binary = urllib.request.urlopen(request)
    all_text = json.load(all_text_binary)
    for i in reversed(all_text):
        message_id = ""
        name = ""
        user_id = ""
        created_at = ""
        updated_at = ""
        text = ""

        if("id" in i):
            message_id = i["id"]
        if("_user_id" in i):
            user_id = i["_user_id"]
        if("_created_at" in i):
            created_at = i["_created_at"]
            created_at = utc_to_jst(created_at)
        if("_updated_at" in i):
            updated_at = i["_updated_at"]
            updated_at = utc_to_jst(updated_at)
        if("text" in i):
            text = i["text"]
        
        # 辞書からアカウント名を持ってくる
        name = "UNKNOWN"
        if (user_id in USERID_NAME_DIC):
            name = USERID_NAME_DIC[user_id]
        
        posted_message_information = "\
   ACCOUNT_NAME: {}\n\
   user_id:      {}\n\
   message_id:   {}\n\
   created_time:   {}\n\
   updated_time:   {}\n\
   message:\n\
{}".format(
            name, user_id, message_id, created_at, updated_at, text
            )

        print("*"*70)
        print(posted_message_information)
        print("*"*70)
        print("\n")

while True:
    INPUT = input("投稿:p, 読み込み:r, 件数を指定して読み込み:r2, 終了:q\n")
    if INPUT == "p":
        INPUT_MESSAGE = input("投稿内容を入力\n")
        post_message(INPUT_MESSAGE)
    if INPUT == "r":
        USERID_NAME_DIC = get_userid_name()
        print_posted_text(40, USERID_NAME_DIC)
    if INPUT == "r2":
        READ_MESSAGE_NUMBER = int(input("読み込み件数を入力\n"))
        USERID_NAME_DIC = get_userid_name()
        print_posted_text(READ_MESSAGE_NUMBER, USERID_NAME_DIC)
    if INPUT == "q":
        break