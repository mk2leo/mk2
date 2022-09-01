# -- coding: utf-8 --**
from os import stat
import requests
import time
import random,string
import json

boundary = ''.join(random.sample(string.ascii_letters + string.digits, 16))

session = requests.Session()
url = 'https://api-bbs.ztedevices.com/content/home/index' 
headers = {
        'Host':'api-bbs.ztedevices.com',
        #'Connection':'keep-alive',
        'accessToken':'102eedc808fc',
        'deviceUuid':'247BCC43A1F42C6D6',
        'Content-Length':'18',
        }
body='pageNum='+str(random.randint(1,200))+'&lastId=0'
print(body)
response = session.post(url=url, headers=headers, data=body)
#print(str(response.json()))
st=response.json()
for i in range(5,12):
  sa=st['data'][i]['id']
  print(sa)

  
  url = 'https://api-bbs.ztedevices.com/user/user/contentPraise' #點讚 
  body='type=0&content_id='+sa
  response = session.post(url=url, headers=headers, data=body)
  print(response.json())
  time.sleep(2)

  url = 'https://api-bbs.ztedevices.com/content/content/share' #分享 
  headers = {
        'Host':'api-bbs.ztedevices.com',
        'deviceUuid':'247BCC43A1F42C6D65E50F',
        'Cookie':'SERVERID=02da73db89e8798408|1661482800|1661481259; Path=/',
        'Connection':'keep-alive',
        'accessToken':'102eedc808fcb0db74',
        'Content-Type':'application/x-www-form-urlencoded',
        'Content-Length':'17',
      }
  body='content_id='+sa
  response = session.post(url=url, headers=headers, data=body)
  print(response.json())
  time.sleep(2)


def openlunch():#抽獎
 for i in range(10):
     session = requests.Session()
     url = 'https://api-bbs.ztedevices.com/points/prize/launch' 
     headers = {
        'Host':'api-bbs.ztedevices.com',
        'Connection':'keep-alive',
        'accessToken':'102eedc808fcb0db74de',
        'Content-Type':'multipart/form-data; boundary=----WebKitFormBoundary'+boundary,
        'Content-Length':'187',
      }
     body='------WebKitFormBoundary'+boundary+'\nContent-Disposition: form-data; name="template_id"\n\n2\n------WebKitFormBoundary'+boundary+'\nContent-Disposition: form-data; name="aid"'
     response = session.post(url=url, headers=headers, data=body)
     print("恭喜取得: "+str(response.json()['data']['prize_value']))
     time.sleep(3)

openlunch()
