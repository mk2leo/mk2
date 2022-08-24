import requests




session = requests.Session()

url = 'https://api-bbs.ztedevices.com/points/home/pointsRegister' 
headers = {
    'Host':'api-bbs.ztedevices.com',
    'Connection':'keep-alive',
    'accessToken':'',
    
    }
body = ''
#body = '{"id":"202203142235442699324"}'

response = session.post(url=url, headers=headers, data=body)

print (response.text)
