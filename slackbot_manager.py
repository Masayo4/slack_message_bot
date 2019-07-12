from slacker import Slacker
import slackbot_settings
import time
import random
#pip install slacker


def announce():
    user_names = ["hogehoge","fugafuga"]
    user_ids = ["@~","@~"]
    #these use for mention in slack. Please check user_profile.
    #click user_icon -> view profile-> clicl "・・・" button -> use member ID
    #ex UXIA01(member ID) -> @UXIA01

    attachment = {
        'title': '被験者の皆様へ',
        #message title
        'text': str(user_names[0])+'>です.\n <'+str(user_ids[0])+'>さん,'+str(user_ids[1])+'>さん,実験お願いします.',
        #text is massage. you can use mention function when you find memberID.
        'color': '#1e2c5b'
        #contents bar
    }

    slack.chat.post_message(
    'your_channel_name',
    #channel name
    as_user = True,
    attachments = [attachment]
    )


if __name__ =='__main__':
    slack =Slacker(slackbot_settings.API_TOKEN)
    print("start")
    haefeli_announce()
    print("End")
