# versatileapisns_client
Qiitaで話題になってた[エンジニア・プログラマにしか使えないSNS](https://qiita.com/HawkClaws/items/599d7666f55e79ef7f56)  
のクライアントをPythonで作ってみました。  

標準ライブラリしか使っていないので、Pythonさえ用意すれば動作します。  
最低限の機能として、メッセージの投稿と投稿されたメッセージの閲覧が可能です。  
見た目がしょぼいのは許してや城之内

# 使い方
```
python versatileapisns.py
```
コマンドライン上で動作します。

# 参考にした資料
[クエリ パラメーターを使用して応答をカスタマイズする](https://docs.microsoft.com/ja-jp/graph/query-parameters)  
ODataクエリがよくわからなかったので書き方の参考に。

[javaboy-github/only-programer-sns-client](https://github.com/javaboy-github/only-programer-sns-client)  
Goで作られたクライアントだが、メッセージの投稿が400でうまくいかなかった際の参考に。