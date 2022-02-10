import requests
import sys
import traceback



login_url = "https://www.kejiwanjia.com/wp-json/jwt-auth/v1/token"


target_url = "https://www.kejiwanjia.com/wp-json/b2/v1/userMission"

form_data1 = {
    "username": "填",
              "password": "填",} 

def run(form_data):
    s = requests.Session()
    response = s.post(login_url, data=form_data)
    #print(response.text) 
    #rcookies=response.cookies

    print(response.status_code) 
    #print('Cookies', cookies)

    
    #if response.status_code == 200:
     # resp = s.get(target_url2)
    headers = {
     'authorization': '',#抓包
            'origin': 'https://www.kejiwanjia.com',
            'referer': 'https://www.kejiwanjia.com/task',
            'user-agent': 'Mozilla/5.0 (Linux; Android 12; DIPPER) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.52 Mobile Safari/537.36'
     }  # headers的例子，看你的post的headers
    
    resp = s.post(target_url, headers=headers)
    
    print(resp.text) 
    

def main():
    run(form_data1)
    

if __name__ == '__main__':
    try:
        sys.exit(main())
    except Exception as e:
        traceback.print_exc()    
