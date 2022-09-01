import requests
import time
import json
import datetime
import random,string

t = time.time()   
    #秒级:

times=int(round(t * 1000))
    #微秒级：

boundary = ''.join(random.sample(string.ascii_letters + string.digits, 16))

def signin():#簽到
  session = requests.Session()

  url = 'https://api-bbs.ztedevices.com/points/home/pointsRegister' 
  headers = {
    'Host':'api-bbs.ztedevices.com',
    'Connection':'keep-alive',
    'accessToken':'102eedc808f',
    
    }
  body = ''


  response = session.post(url=url, headers=headers, data=body)

  if response.json()['status'] == 200:
    print('签到成功')
  else:
    print(response.json()['status'],"TOKEN己過期")
    send_msg("TOKEN己過期")
    

def openbox():#打開寶箱
  session = requests.Session()
  url = 'https://api-bbs.ztedevices.com/points/home/openbox' 
  headers = {
    'Host':'api-bbs.ztedevices.com',
    'Connection':'keep-alive',
    'accessToken':'102eedc80',
    
    }
  body = ''

  response = session.post(url=url, headers=headers, data=body)

  if response.json()['status'] == 200:
      print(response.json())
      stat=response.json()
      energyId=stat['data']["energyId"]
      time.sleep(2)
      url = 'https://api-bbs.ztedevices.com/points/home/havingenergy' #領取寶箱
      headers = {
        'Host':'api-bbs.ztedevices.com',
        'Connection':'keep-alive',
        'accessToken':'102eedc808f',
        'Content-Type':'multipart/form-data; boundary=----WebKitFormBoundary'+boundary,
        'Content-Length':'187',
      }
      body='------WebKitFormBoundary'+boundary+'\nContent-Disposition: form-data; name="energyId"\n\n'+energyId+'\n------WebKitFormBoundary'+boundary+'\nContent-Disposition: form-data; name="v"'
      response = session.post(url=url, headers=headers, data=body)
      print("提取寶箱成功")
     
  else:
      print("寶箱未到時間")  
