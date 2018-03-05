# -*- coding: utf-8 -*-
import re
import requests
import html5lib
from bs4 import BeautifulSoup

if __name__ =="__main__":

    print("hello main ")
    s = requests.session()
    url_login ='https://accounts.douban.com/login'
    formdata ={
        'redir': 'https://www.douban.com',
        'form_email': 'knifecyd',
        'form_password': 'knifecyd',
        'source':'index_nav',
        'login': u'登陆'
    }

     # 'Cookie': 'bid=OMFhlzP4OBY; _pk_ref.100001.8cb4=%5B%22%22%2C%22%22%2C1519459461%2C%22https%3A%2F%2Fwww.baidu.com%2Flink%3Furl%3DZMuhKZ0HdOHxaJRgD7DcCh7CSwVBQAkwz0kvKMlVwlg87l0txqsP1lqnP9w1bgwp%26wd%3D%26eqid%3Dc319fedf0000f47c000000035a8e7984%22%5D; _pk_id.100001.8cb4=4ed3eac8e81d861e.1515597105.22.1519459469.1519457488.; __yadk_uid=5DGXLZvHJOKS4GLJc8NAK6hzoPzc2i6R; __utma=30149280.151511579.1515597107.1519456661.1519459469.20; __utmz=30149280.1519301239.4.3.utmcsr=baidu|utmccn=(organic)|utmcmd=organic; ll="108296"; ap=1; push_noty_num=0; push_doumail_num=0; ps=y; __utmv=30149280.15729; ct=y; __utmc=30149280; _pk_ses.100001.8cb4=*; __utmb=30149280.1.10.1519459469; __utmt=1',
    # 'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:58.0) Gecko/20100101 Firefox/58.0',
    # 'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
    # 'Accept-Language': 'zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2',
    # 'Accept-Encoding': 'gzip, deflate, br',
    # 'Referer': 'https://www.douban.com/',
    # 'Content-Type': 'application/x-www-form-urlencoded',
    # 'Content-Length': '60',
    # 'Proxy-Authorization': 'Basic Y2hlbnl1ZG9uZzpBYTEyMzQ1Ng==',
    # 'Connection': 'keep-alive',
    # 'Upgrade-Insecure-Requests': '1'

    _headers ={
    'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:58.0) Gecko/20100101 Firefox/58.0',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
    'Accept-Language': 'zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2',
    'Accept-Encoding': 'gzip, deflate, br',
    'Referer': 'https://www.douban.com/',
    'Content-Type': 'application/x-www-form-urlencoded',
    'Content-Length': '60',
    'Proxy-Authorization': 'Basic Y2hlbnl1ZG9uZzpBYTEyMzQ1Ng==',
    'Connection': 'keep-alive',
    'Upgrade-Insecure-Requests': '1'
    }

    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36'}

    #r = s.post(url_login,data=formdata, headers=headers)
    #r = s.post(url_login,data=formdata,headers=headers)
    r = s.post(url_login, data=formdata, headers=headers)
    content=r.text
    soup = BeautifulSoup(content, 'html.parser')

    captcha = soup.find('img', id='captcha_image')
    if captcha:
       captcha_url=captcha['src']
       re_captcha_id =r'<input type="hidden" name="captcha-id"'
       captcha_id = re.findall(re_captcha_id,content)
       print(captcha_id)
       print(captcha_url)
       captcha_text  = input("please  input the captcha :")
       formdata['captcha-solution'] = captcha_text
       formdata['captcha-id'] = captcha_id
       r = s.post(url_login,data=formdata,headers=headers)
       print("the result :" + r.text)
       with open('contacet.txt','w+',encoding ='utf-8') as f:
            f.write(r.text)