import bs4
import requests

url= 'http://192.168.75.141/vul/sqli/sqli_str.php'
# id=1&submit=%E6%9F%A5%E8%AF%A2

def requests_function():
    dict = {
        'name': "1",
        'submit':'%E6%9F%A5%E8%AF%A2'
    }
    html = requests.get(url, data=dict).content.decode('utf-8')
    soup = bs4.BeautifulSoup(html,'lxml')
    print(soup.find_all(name='p'))


if __name__ == '__main__':
    requests_function()