import http.client
import urllib


class SendSMS:
    # 账号初始化
    def __init__(self, account, password):
        self.host = "106.ihuyi.com"
        self.sms_send_uri = "/webservice/sms.php?method=Submit"
        self.account = account
        self.password = password

    # 发送短信
    def send_sms(self, text, mobile):
        params = urllib.parse.urlencode(
            {'account': self.account, 'password': self.password, 'content': text, 'mobile': mobile, 'format': 'json'})
        headers = {"Content-type": "application/x-www-form-urlencoded", "Accept": "text/plain"}
        conn = http.client.HTTPConnection(self.host, port=80, timeout=30)
        conn.request("POST", self.sms_send_uri, params, headers)
        response = conn.getresponse()
        response_str = response.read()
        conn.close()
        return response_str

    # 批量发送
    def send_smss(self, text, mobilelist):
        for mobile in mobilelist:
            print(str(mobile))
            print(self.send_sms(text, str(mobile)))


sender1 = SendSMS("C29408441", "42d111e84be3ca82032dbfea49f36dba")
print(sender1.send_sms("您的验证码是：121254。请不要把验证码泄露给其他人。", "18890506318"))
