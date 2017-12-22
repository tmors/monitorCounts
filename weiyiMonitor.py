import json
import re
from time import sleep

import requests
from twilio.rest import Client

session = requests.Session()
test = '脱敏'
cookiesList = test.split(";")
cookies = {}
for i in cookiesList:
    key = re.findall(r".*?(?=\=)", i)[0]
    value = re.findall(r"(?<=\=).*", i)[0]
    print(key, value)
    cookies[key] = value

while (True):
    page = session.get(
        "脱敏",
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
                account_sid = "脱敏"
                auth_token = "脱敏"
                client = Client(account_sid, auth_token)

                message = client.messages.create(to="+86脱敏",  # 区号+你的手机号码
                                                 from_="+1脱敏",  # 你的 twilio 电话号码
                                                 body="脱敏")

                break
            else:
                print("脱敏")

    sleep(60)

print()
