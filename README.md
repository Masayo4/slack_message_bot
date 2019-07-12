# Slackbot   
## Overview  
you can make announce bot in slack.  
slackでアナウンスができるbotの作成. (自動化する際は時間を指定すればOK)  

## Usage  
please git clone this repository.  
リポジトリをクローンする.  
そして以下のように配置する.  

this is file tree example  
.  
├── README.md  
├── run.py  
├── slackbot_manager.py  
└── slackbot_settings.py  

please install slacker.  
pip で必要な slacker をインストール  
`pip install slacker`  

After that, please ramake ***slackbot_manager.py*** & ***slackbot_settings.py*** scripts.  
インストール後, ***slackbot_manager.py*** と ***slackbot_settings.py*** を書き換える.  



1. slackbot_manager.py
    1. input user_names & user_ids  
      these use for mention in slack. Please check user_profile.  
      click user_icon -> view profile-> clicl "・・・" button -> use member ID  
    1. change attachment title,text,color
    1. change channel name  l24
1. slackbot_settings.py
    1. please get your channel API TOKEN.  
    [how to](https://qiita.com/ykhirao/items/0d6b9f4a0cc626884dbb ) (in Japanese)

2. slackbot_manager.py
    2. ユーザーの名前(任意)とユーザーid(マスト)を取得する.  
    ユーザーiconをクリックして,プロフィールを開ける. ・・・ボタンを押すと確認可能  
    2. attachmentの中を変更する
    2. チャンネルの名前を変更する

2. slackbot_settings.py
    2. APIトークンを取得する.参照は上記


In the your shell,
`$ python slackbot_manager.py`

**Finish!!**

## Requirements  
you need python3 or pyenv.
