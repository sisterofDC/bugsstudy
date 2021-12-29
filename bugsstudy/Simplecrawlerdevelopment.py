# re — Regular expression operations
# 读取文件
# Urllib库 requsets库 Xpath beautifulSoup
# mysql mongo redis 操作
import urllib.request
import bs4
import lxml.html
import urllib.parse
import requests


url = 'http://192.168.75.141/vul/burteforce/bf_form.php'


def urllib_request_function():
    dict = {
        'username': 'admin',
        'password': '123456'
    }
    data = bytes(urllib.parse.urlencode(dict), encoding='utf-8')
    req = urllib.request.Request(url=url, data=data, method='POST')
    response = urllib.request.urlopen(req)
    print(type(response))
    # status = response.status
    # header = response.getheaders()
    # print(status, header)
    text = response.read().decode('utf-8')
    selector = lxml.html.fromstring(text)
    info = selector.xpath('//*[@id="main-container"]/div[2]/div/div[2]/div/div/form/*')
    print(info)


def save_html_function(response):
    with open("../savehtml/test.html", "wb") as file:
        file.write(response.read())


def requests_function():
    dict = {
        'username': 'admin',
        'password': '123456',
        'submit':'Login'
    }
    html = requests.post(url, data=dict).content.decode('utf-8')
    print(html)

def beautifulsoup_function(htmlfile):
    soup = bs4.BeautifulSoup(htmlfile,'lxml')




if __name__ == '__main__':
    requests_function()
