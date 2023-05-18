# 导入依赖库
import requests
from bs4 import BeautifulSoup
# import os
import sys


def download_image(url, save_path):
    response = requests.get(url, stream=True)
    if response.status_code == 200:
        with open(save_path, 'wb') as file:
            for chunk in response.iter_content(1024):
                file.write(chunk)
        print(f"图片下载成功：{save_path}")
    else:
        print(f"图片下载失败：{url}")

# 确定要爬取的网址
url = "https://www.xvideos.com/"

# print(url+"/"+str(i))
# 发送 HTTP 请求并解析页面内容
response = requests.get(url)
soup = BeautifulSoup(response.content, 'html.parser')
# print(soup)
# continue
# 找到所有应用的链接并进入详情页
# 列表页面中只包含应用的概要信息，我们需要进入每个应用的详情页面获取 logo 图片。可以通过在列表页面中找到应用的链接来实现这一点

# 找到所有应用的链接
labelList = soup.find_all('div' ,{"class" : "thumb-block","data-is-channel":"1"})
print(labelList)
# sys.exit()
fileDir = "/home/liyang/桌面/images/xvideos"

# 进入每个应用的详情页面
for item in labelList:
    # print(item)
    url = item.find('div',{"class":"thumb"}).find('img')['data-src']
    # print(url)
    # # 下载图片
    #
    filename = f"{item['data-id']}.jpg"
    # print(filename)
    # sys.exit()
    download_image(url,f'{fileDir}/{filename}')