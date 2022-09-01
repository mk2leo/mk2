# -- coding: utf-8 --**
from os import stat
import requests
import time
import random,string
import json
from pumxsned import send_msg

def wawaday():#簽到
    session = requests.Session()
    url = 'https://m.51jiawawa.com/api/sign/insert' 
    headers = {
        'Host':'m.51jiawawa.com',
        'Accept-Encoding':'gzip',
        'User-Agent':'okhttp/3.12.13',
        'Content-Type':'application/x-www-form-urlencoded',
        'Content-Length':'445',
        'Connection':'keep-alive}',
      }
    body='appType=0&auth=d0e9bbc151ea84d8dbadce43b4ac&device=1&deviceInformation=market%3Ddollmain%7CBRAND%3DXiaomi%7CMODEL%3DRedmi%20Note%204X%7CRELEASE%3D6.0%7CSDK_INT%3D23%7CCPU_ABI_%3Darmeabi-v7a%7CCPU_ABI2%3Darmeabi%7CPRODUCT%3Dnikel%7CDISPLAY%3DMRA58K&idfa=78d1c311351522f14f6a646c4151&imei=&market=dollmain&oaid=&packageName=com.meijia.mjzww&sourceId=0&t=1661841523641&token=9a1a2f08-1996-40cd-81d6-c4c9663b9fbId=3566982&version=4.8.5'
    response = session.post(url=url, headers=headers, data=body)
    stat=response.json().get('success')
    print("簽到: ",stat)
    if stat == False:
     print("登入可能過期了")
     send_msg("簽到失敗了","一元抓娃娃")

    

wawaday()
