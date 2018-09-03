# -*- coding: utf-8 -*-
import requests
import time
import re
import base64

now_time = str(int(time.time()))
headers= {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36"}
s = requests.Session()
s.get("http://bus.mapbar.com", headers=headers)

def deal_captcha():
    url = "http://bus.mapbar.com/ip/validate.jsp?s=image&" + now_time
    r = s.get(url, headers=headers)
    #获取验证码url
    code = re.findall(r'"/services/code/getCode\?s=(.*?)"',r.text)[0]
    captcha_url = "http://bus.mapbar.com/services/code/getCode?s=" + code
    captcha = s.get(captcha_url, headers=headers).content
    captcha_img64 = base64.b64encode(captcha)
    captcha_code = baidu_ai(captcha_img64)

    #传入验证码url
    post_captcha = re.findall(r'ipValidateObj\.src = "(http://bus\.mapbar\.com:80/ip/validate\.jsp\?kt=.*&code2=)"',r.text)[0]
    post_captcha = post_captcha + captcha_code + "&" + now_time
    r = s.get(post_captcha, headers=headers)
    print("完成验证码验证...")

def baidu_ai(captcha_img64):
    baidu_api = "https://aip.baidubce.com/rest/2.0/ocr/v1/general_basic?access_token=24.ce79e014222dda0b60c0e46f3a440254.2592000.1533546051.282335-11503283"
    headers = {
        "Content-Type":"application/x-www-form-urlencoded"
              }
    data = {"image":captcha_img64}
    r = requests.post(baidu_api, headers=headers, data=data, verify=False)
    captcha_code = re.findall(r'"words": "(\d+)"', r.text)[0]
    return captcha_code

# deal_captcha()