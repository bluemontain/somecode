import itchat
from itchat.content import *

@itchat.msg_register(TEXT, isFriendChat=True) # 监听私聊消息
def reply_text(msg):
    if msg.text == 'hello':
        return '你好啊，我是机器人！'
    else:
        return '这个问题太高深了，我还不会回答...'

itchat.auto_login(hotReload=True)
itchat.run()