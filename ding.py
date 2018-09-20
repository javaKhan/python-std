# -*- coding: UTF-8 -*-
import urllib.request
import urllib.parse
import ssl


#
# def parseMarkDownJson(title, text):
#     print(strMsg)
#     return strMsg
#

def parseLinkMsg():
    str = '{"msgtype": "link","link": {"text":"Java11 的新消息", "title": "JDK 11 将于本月25日发布，新特性一览", "picUrl": "https://ss2.baidu.com/6ONYsjip0QIZ8tyhnq/it/u=3833796983,747899399&fm=173&app=25&f=JPEG?w=640&h=356&s=1EC7985EC091A9DA46836FAF0300700A", "messageUrl": "https://baijiahao.baidu.com/s?id=1601527671757756322&wfr=spider&for=pc"}}'
    return str


if __name__ == '__main__':
    ssl._create_default_https_context = ssl._create_unverified_context
    title = '这是一个远古测试'
    text = "## markdown 厉害了  ``` System.out.println(hello word) ```"
    # text = "早上好"
    url = 'https://oapi.dingtalk.com/robot/send?access_token=2b1317c6073bbc508d716589c063f5aac39a1073cfe9c20a0af44b8f03404aca12'
    headers = {
        'Content-Type': 'application/json;charset=utf-8',
    }
    strMsg = parseLinkMsg()
    print(strMsg)
    req = urllib.request.Request(url, headers=headers, data=bytes(strMsg, encoding='utf-8'))  # POST方法
    page = urllib.request.urlopen(req).read()
    print(page.decode('utf-8'))
