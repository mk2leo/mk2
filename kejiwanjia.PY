
import requests
import sys
import traceback

login_url = "https://www.kejiwanjia.com/wp-json/jwt-auth/v1/token"

target_url = 'https://www.kejiwanjia.com/wp-json/b2/v1/userMission'

form_data1 = {
    "username": "",
              "password": "",} 

def run(form_data):
    s = requests.Session()
    response = s.post(login_url, data=form_data)
    #print(response.text) 
    print(response.status_code) 
    if response.status_code == 200:
      resp = s.post(target_url)
    print(response.text) 

def main():
    run(form_data1)
    print("run1")    

if __name__ == '__main__':
    try:
        sys.exit(main())
    except Exception as e:
        traceback.print_exc()  
