import requests




#ldygo=os.getenv("loseprivacy")
ldygo=loseprivacy

session = requests.Session()
url = 'https://loseprivacy.icu/checkin' 
headers= {          
            ':authority':'loseprivacy.icu',
            ':scheme':'https',
            ':path':'/checkin',
            'x-requested-with':'XMLHttpRequest',
            #'accept':'application/json, text/javascript, */*; q=0.01',
            'user-agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.198 Safari/537.36',
            #'referer':'https://loseprivacy.icu/ucenter',
            #'accept-encoding':'gzip, deflate, br',
            #'accept-language':'zh-CN,zh;q=0.9,zh-TW;q=0.8',
            'cookie':ldygo
            }
    #body=''
    
response = session.post(url=url, headers=headers)#, #data=body)
print(response.json())
if response.json()['err']==0:
    print('签到成功')
else:
    print(response.json()['msg'],"TOKEN己過期")
