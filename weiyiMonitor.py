import json
import re
from time import sleep

import requests
from twilio.rest import Client

session = requests.Session()
test = ' _sid_=1495815378470018725013181; _e_m=1495815378480; _fp_code_=0962a11d219a45f2440ee9bdc5660caf; _ipgeo=province%3A%E6%B9%96%E5%8D%97%7Ccity%3A%E9%95%BF%E6%B2%99; searchHistory=%E6%B9%96%E5%8D%97%E7%9C%81%E8%82%BF%E7%98%A4%E5%8C%BB%E9%99%A2%2Chos%7C%2Cclear; _sh_ssid_=1495818141451; monitor_sid=2; mst=1495818135054; JSESSIONID=az7q41jhxxw11oue2tu82o3b1; _ci_=U8sJgy/gzBks0CMpGZq5mL6fwGQgcAlHkqkKXZth7w54h0doUWt5OJyHLkorBdjX; __i__="hlULi6bu4k/i9hTFCs7xnJCbDzub4aD3t36CkI5v6x0="; __usx__="j/8m8ruGyqroqmoZuLvNxToTwc9P6EIdb1YXYV8CK4w="; __up__="Ya0E0tUuPeSx1lIn3DoZSj3Ns+MUBGLqZtRoQ86HWbs="; _exp_="mDgz101CtjfVycTYNZBnjx1S9Uz8aViO7NaJ42JEj+I="; __ut__="NIl15ssYIUsJXoGYggHocCLvVhMNZFzJl+q3in0f8Bg="; __p__="tE6SqxPrw8dgSKjklY5jv27WXPmeOh7anHtqI58Nau6dXlUHF41cyA=="; __un__="r+Zejm4geYvMefiJEewaLQiVNkyR3tnLJ449vut2pTdFwXv88jpzS3ngoBKaBsn6SwQHPbcCgTM="; __wyt__=!P8kuXUui_7P1DQODTTivlT2q01DRHaykOIbpFa9IKirmBbJMFx0t4774OrM4cu7JgwnWxq8G5jxifQ8py7DtC14Xi1iolwirSWKUo88ujSHoBXUMJG-6ChkCHOE2AKqRBSdeUo_XMq6ZMK_3WIbg61upmqqHHXfIuNtYVYnBXS-fk; __rf__="salqosXOO8OULi4jXn5cFCm/235ogtX8bh7Q8+hxZz7pfAnGIz8/4MNgkVG/i2WZwDKrOCFYKWrESo1G6NnjxuqnIxHTGYNlv1q/hx6tD0t7U4QFvjG4aaKNbiU6525y"; Hm_lvt_66fcb71a7f1d7ae4ae082580ac03c957=1495815369,1495815378; Hm_lpvt_66fcb71a7f1d7ae4ae082580ac03c957=1495818218; monitor_seq=4; mlt=1495818217914; _fmdata=C32673C3133DCB1E372F67A5BAE0DEB3E67A59634F76278C1AE41254AEC7545EF55053795B7244EFA76E8C1D8E2AFA92846C05964A4609FC'
cookiesList = test.split(";")
cookies = {}
for i in cookiesList:
    key = re.findall(r".*?(?=\=)", i)[0]
    value = re.findall(r"(?<=\=).*", i)[0]
    print(key, value)
    cookies[key] = value

while (True):
    page = session.get(
        "https://www.guahao.com/expert/new/shiftcase/?expertId=8b9a58a6-7aa3-4616-8c9c-44b95decb38f000&hospDeptId=75a5dd41-e7b3-4412-baa6-0722460ead67000&hospId=7663df01-c594-4a2e-83ca-1c708ef870c1000&_=1495819326159",
        verify=False, cookies=cookies)
    try:
        jdata = json.loads(page.text)
    except:
        continue
    print(page.text)
    for i in jdata["data"]["shiftSchedule"]:

        if (i["date"] == "2017-05-31"):
            if (i["status"] == 4):
                # send sms
                # 下面认证信息的值在你的 twilio 账户里可以找到
                account_sid = "公开删除"
                auth_token = "公开删除"
                client = Client(account_sid, auth_token)

                message = client.messages.create(to="+86公开删除d",  # 区号+你的手机号码
                                                 from_="+1公开删除",  # 你的 twilio 电话号码
                                                 body="杨农05-31有位置")

                break
            else:
                print("yang nong 05-31not enough")

    sleep(60)

print()
