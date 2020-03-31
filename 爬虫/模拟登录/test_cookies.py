import requests

# 使用cookie保持登录
# cookies拼装成json
Cookie = "_site_id_cookie=1; clientlanguage=zh_CN; uniqueVisitorId=93e5ebf5-b764-86f7-e506-08e706b90144; " \
         "__qc_wId=465; pgv_pvid=9254292048; username=18182737073; JSESSIONID=5E13362ECD165AB70BD3CAD8628F3633; " \
         "JSESSIONID=5E13362ECD165AB70BD3CAD8628F3633 "
Cookies = {}
for i in Cookie.split(';'):
    key, value = i.split('=')
    Cookies[key] = value
print(Cookies)
url = 'http://www.tipdm.org/member/index.jspx'
head = {
    "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 "
                  "Safari/537.36"}
rq = requests.get(url=url, cookies=Cookies, headers=head)
print(rq.content.decode('utf8'))
