# 导入依赖库
import requests
from bs4 import BeautifulSoup
# import os
import json

from utils.download_image import download_image

# json 数据
data = []

# 确定要爬取的网址
url = "https://www.bbc.co.uk/search?q=2022&d=news_ps&page="
fileDir = "./news/bbc/"

image_key = 280
for a in range(28):
    print(f'当前进度：{a + 1}')
    _index = a + 1
    response = requests.get(url + str(_index))
    soup = BeautifulSoup(response.content, 'html.parser')
    list_news = soup.find_all('div', {"class": "ssrcss-53phst-Promo ett16tt0"})
    for index, item in enumerate(list_news):
        # print(item)
        # 抓取图片
        image_key = image_key + 1
        url_element = item.find('img', {"class": "ssrcss-evoj7m-Image ee0ct7c0"})
        image_url = url_element['src'] if url_element else ""
        # print(url)
        if image_url:
            # print(url)
            # # 下载图片
            #
            filename = f"{image_key}.jpg"
            # print(filename)
            # sys.exit()
            download_image(url, f'{fileDir}images/{filename}')
            # 抓取文字
            title_element = item.find('div', {"class": "ssrcss-1f3bvyz-Stack e1y4nx260"}).find('p', {
                'class': 'ssrcss-6arcww-PromoHeadline e1f5wbog5'}).find('span')
            introduction_element = item.find('div', {"class": "ssrcss-1f3bvyz-Stack e1y4nx260"}).find('p', {
                'class': 'ssrcss-1q0x1qg-Paragraph eq5iqo00'})
            title = title_element.get_text() if title_element else ""
            introduction = introduction_element.get_text() if introduction_element else ""
            news = {
                "title": title,
                "introduction": introduction,
                "imageName": filename
            }
            data.append(news)
# print(data)
# 将数据保存到文件中
with open(f'{fileDir}data1.json', "w", encoding="utf-8") as file:
    json.dump(data, file, indent=2, ensure_ascii=False)
