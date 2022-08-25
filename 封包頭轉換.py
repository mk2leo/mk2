import requests
import re
str = 'egid=DFP7BEA48BA09A1E5F7410C3D633400B40B05ED8F3A8E45906955BA63CE2EBEC&sbh=72&apiInvokeTiming=ON_FOREGROUND&hotfix_ver=&appver=10.6.30.3979&grant_browse_type=AUTHORIZED&userRecoBit=0&socName=MediaTek%20MT6797M&newOc=XIAOMI&max_memory=256&isp=&kcv=1474&boardPlatform=mt6797&did_tag=0&sys=ANDROID_6.0&cold=false&slh=0&sw=1080&oDid=ANDROID_159718fc47b3b628&rdid=ANDROID_4383153355e01fb1&language=zh-cn&ver=10.6&abi=arm64&country_code=CN&kpn=NEBULA&cdid_tag=0&apptype=22&sh=1920&cold_launch_time_ms=1658888548033&nbh=0&androidApiLevel=23&earphoneMode=1&browseType=3&kpf=ANDROID_PHONE&ddpi=480&did=ANDROID_159718fc47b3b628&android_os=0&net=WIFI&app=0&device_abi=&ud=2945349060&c=XIAOMI&bottom_navigation=true&ftt=&keyconfig_state=2&darkMode=false&totalMemory=3727&iuid=&did_gt=1658888548803&__NStokensig=6bbcd70064e9241650c8adedfa23cde5a0e1486924fc4123c3d72301bb582e31&sig=cbce3ce5e01ab3529a789bdade6618cf HTTP/1.1'


def run(str):
    str = re.sub(r'&', '\n', str)
    content = re.findall(r'(.*?)=(.*)', str)
    data = {}
    for i in content:
        key = i[0]
        value = i[1]
        data[key] = value
    print(data)

run(str)
