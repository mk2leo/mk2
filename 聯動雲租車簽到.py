# -- coding: utf-8 --**
from os import stat
import requests
import time
import random,string
import json
from pumxsned import send_msg

t = time.time()   
    #秒级:

times=int(round(t * 1000))



def carday():#簽到
    session = requests.Session()
    url = 'https://m.ldygo.com/los/zuche-intf-union.signIn' 
    headers={
            'cookie':'UFO-SESSION-ID=d5cfc4a9f76f4f13ae839c; SSO-SESSION-ID=d5cfc4a9f76f4f13ae8',
            }
    body='{"_channel_id":"09","_client_version_no":"2.11.0","timestamp":"'+ str(times) +'"}'
    
    response = session.post(url=url, headers=headers, data=body)
    print(response.json())
    if response.status_code == 200:
     print('签到成功')
    else:
     print(response.json()['responseMsg'],"TOKEN己過期")
     send_msg(response.json()['responseMsg'],"联动云")
    

    

carday()
