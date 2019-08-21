
import itchat
import json
import requests
import codecs
import time
from threading import Timer

# 技术宅可以哄女友
sex_dict = {}
sex_dict['0'] = "其他"
sex_dict['1'] = "男"
sex_dict['2'] = "女"

message_dict = {
    "楠":"：大数据前沿（id:bigdataqianyan）",
    "你好":"你好啊，这条消息是小哥哥回复的。",
    "备忘录":"早上10.30参加产品发布会\n今晚隔壁王总找你开会"
}

KEY = '07f07ce1ceb94eb5bae8d3fe4b98'  #需要去图灵注册一个

def sleep(mytime=''):
        time.sleep(mytime)

def isMsgFromMyself(msgFromUserName):
    # 检查消息发送方是否为自己
    global myName
    return myName == msgFromUserName

def get_response(msg):
    # 构造发送给图灵机器人服务器的数据
    apiUrl = 'http://www.tuling123.com/openapi/api'
    data = {
        'key'    : KEY,
        'info'   : msg,
        'userid' : 'wechat-robot',
    }
    try:
        r = requests.post(apiUrl, data=data).json()
        # 字典的get方法在字典没有'text'值的时候会返回None而不会抛出异常
        return r.get('text')
    # 为了防止服务器没有正常响应导致程序异常退出，这里用try-except捕获了异常
    # 如果服务器没能正常交互（返回非json或无法连接），那么就会进入下面的return
    except:
        # 将会返回一个None
        return


#下载好友头像
def download_images(frined_list):
    image_dir = "./images/"
    num = 1
    for friend in frined_list:
        image_name = str(num)+'.jpg'
        num+=1
        img = itchat.get_head_img(userName=friend["UserName"])
        with open(image_dir+image_name, 'wb') as file:
            file.write(img)

def save_data(frined_list):
    out_file_name = "./data/friends.json"
    with codecs.open(out_file_name, 'w', encoding='utf-8') as json_file:
        json_file.write(json.dumps(frined_list,ensure_ascii=False))

@itchat.msg_register(itchat.content.TEXT)
def print_content(msg):
    NickName = msg['User']['NickName']
    print(NickName)
    if isMsgFromMyself(msg['FromUserName']):
        return
#做了特殊处理可以筛选你指定回复的人，自己回复不会触发机器人回复
    if NickName != '💛王大哈' and NickName != '芳🐾' and NickName != 'tobeluckyone':
        return

    s = Timer(3,sendBusyStatus,(NickName,msg))
    s.start()

def sendBusyStatus(NickName,msg):
    user = itchat.search_friends(name=NickName)[0]
    text = get_response(msg['Text'])

    if text:
        user.send(text)
    else:
        user.send(u"小可爱,我不太理解"%NickName)


if __name__ == '__main__':
    itchat.auto_login()
    
    friends = itchat.get_friends(update=True)[0:]#获取好友信息
    friends_list = []

    for friend in friends:
        item = {}
        item['NickName'] = friend['NickName']
        item['HeadImgUrl'] = friend['HeadImgUrl']
        item['Sex'] = sex_dict[str(friend['Sex'])]
        item['Province'] = friend['Province']
        item['Signature'] = friend['Signature']
        item['UserName'] = friend['UserName']

        friends_list.append(item)
        #print(item)

    # save_data(friends_list)
    # download_images(friends_list)

    
    # user = itchat.search_friends(name=u'bb')[0]
    # user.send(u'hello,这是一条来自小哥哥的消息')
    myName = itchat.get_friends(update=True)[0]['UserName']
    itchat.run()
