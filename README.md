# Slackbot  
=====  
## Overview  
you can make announce bot in slack.  
slackでアナウンスができるbotの作成. (自動化する際は時間を指定すればOK)  

## Usage  
please git clone this repository.

.  
├── README.md  
├── run.py  
├── slackbot_manager.py  
└── slackbot_settings.py  

`pip install slacker`  

After that, please ramake ***slackbot_manager.py*** & ***slackbot_settings.py*** scripts.  

<dl>
  <dt>slackbot_manager.py</dt>
  <dd>
  1. input user_names & user_ids  
  these use for mention in slack. Please check user_profile.  
  click user_icon -> view profile-> clicl "・・・" button -> use member ID  
  2. change attachment title,text,color  
  3. change channel name  l24
  </dd>
  <dt>slackbot_settings.py</dt>
  <dd>
  1. please get your channel API TOKEN. [how to](https://qiita.com/ykhirao/items/0d6b9f4a0cc626884dbb )
  /dd>
</dl>

In the your shell,
`$ python slackbot_manager.py`

**Finish!!**

##Requirements  
you need python3 or pyenv.
