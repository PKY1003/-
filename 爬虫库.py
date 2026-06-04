import random
from bs4 import BeautifulSoup
import requests
import urllib.request
from urllib.parse import urljoin

def get_html(urls):#访问网站，抓取HTML等数据
    user_agent = [
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/42.0.2311.135 Safari/537.36 Edge/12.246",
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML like Gecko) Chrome/46.0.2486.0 Safari/537.36 Edge/13.10586",
        "Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/537.36 (KHTML like Gecko) Chrome/46.0.2486.0 Safari/537.36 Edge/13.9200"]
    headers = {"User_Agent": random.choice(user_agent)}
    request = urllib.request.Request(urls, headers=headers)  # 访问链接
    response = urllib.request.urlopen(request)  # 获取响应
    return response

def parse_andz_download(response,goofish_path,name):#解析数据并下载
    n = 1
    i = ".jpg"
    bsObj = BeautifulSoup(response, "lxml")  # 解析HTML文档,"html.parser"是python自带的解析器，换成"lxml"后效率翻倍
    t1 = bsObj.find_all('img')  # 查找所有<img>标签
    base_url=r"https://www.goofish.com/search"
    for t2 in t1:
        t3 = t2.get('src')
        pathfile = goofish_path + r'/' + str(n) + i  # 创建文件路径，路径+编号+后缀
        if t3:
            full_url=urljoin(base_url,t3)#补全相对地址
            print(f'正在下载：{full_url}')
            imgData=requests.get(full_url).content#发出一个新的请求，进行下载
            with open(pathfile, 'wb') as f:  # 打开文件
                f.write(imgData)  # 将图片数据写入文件中
                print(f"thread{name}write:{pathfile}")
                n=n+1
