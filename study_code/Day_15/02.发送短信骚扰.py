# 接口类型：互亿无线触发短信接口，支持发送验证码短信、订单通知短信等。
# 账户注册：请通过该地址开通账户http://sms.ihuyi.com/register.html
# 注意事项：
# （1）调试期间，请用默认的模板进行测试，默认模板详见接口文档；
# （2）请使用APIID（查看APIID请登录用户中心->验证码、通知短信->帐户及签名设置->APIID）及 APIkey来调用接口；
# （3）该代码仅供接入互亿无线短信接口参考使用，客户可根据实际需要自行编写；

# !/usr/local/bin/python
# -*- coding:utf-8 -*-
import http.client
import urllib

host = "106.ihuyi.com"
sms_send_uri = "/webservice/sms.php?method=Submit"

# 用户名请登录用户中心->验证码、通知短信->帐户及签名设置->APIID
account = "C56220776"
# 密码 查看密码请登录用户中心->验证码、通知短信->帐户及签名设置->APIKEY
password = "e2a9ca9a4b287da535180a1ec74aaa89"


def send_sms(text, mobile):
    params = urllib.parse.urlencode(
        {'account': account, 'password': password, 'content': text, 'mobile': mobile, 'format': 'json'})
    headers = {"Content-type": "application/x-www-form-urlencoded", "Accept": "text/plain"}
    conn = http.client.HTTPConnection(host, port=80, timeout=30)
    conn.request("POST", sms_send_uri, params, headers)
    response = conn.getresponse()
    response_str = response.read()
    conn.close()
    return response_str


'''
if __name__ == '__main__':
    mobile = "13001087800"
    text = "您的验证码是：121254。请不要把验证码泄露给其他人。"
    print(send_sms(text, mobile))
'''

list = [13295800121, 18503088297, 13810811154, 13419990303, 17090412975, 15210681197, 18774678240, 18630126892,
        17346533310, 17703819995,
        13672169651, 18085637896, 17600364335, 15931269973]
text = "您的验证码是：121254。请不要把验证码泄露给其他人。"
for mobile in list:
    print(str(mobile))
    print(send_sms(text, str(mobile)))
