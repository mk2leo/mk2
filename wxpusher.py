import requests
import re
import os, sys
import json

def send_msg(content,title):
    url = 'http://wxpusher.zjiecode.com/api/send/message'
    
    s = json.dumps({
      "appToken":"",#输入自己白白token
      "content":content,
      "summary":title,#消息摘要，显示在微信聊天页面或者模版消息卡片上，限制长度100，可以不传，不传默认截取content前面的内容。
      "contentType":3,#内容类型 1表示文字  2表示html(只发送body标签内部的数据即可，不包括body标签) 3表示markdown 
      "topicIds":[ #发送目标的topicId，是一个数组！！！，也就是群发，使用uids单发的时候， 可以不传。
          2974
      ],
      "uids":[#发送目标的UID，是一个数组。注意uids和topicIds可以同时填写，也可以只填写一个。
          "UID_I4CLy5Zc"#输入自己的UID
      ],
      "url":"http://wxpusher.zjiecode.com" #原文链接，可选参数
    })

    r = requests.post(url,data=s,headers={"Content-Type":"application/json"})
    
    return r
