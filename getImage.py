import requests
from bs4 import BeautifulSoup

# 设置要爬取图片的 URL
url = 'https://www.woyaogexing.com/touxiang/'

# 发送 HTTP 请求并解析页面内容
response = requests.get(url)
soup = BeautifulSoup(response.content, 'html.parser')

# 获取所有图片链接
img_links = []
# print(soup)
for img in soup.find_all('img'):
    img_links.append("https:" + img.get('src'))

# 创建保存图片的文件夹
# if not os.path.exists('images'):
#     os.makedirs('images')
# print(img_links)
# 下载图片并保存到本地
dir = "/Users/macosx/Desktop/项目文档/python-demo/Crawlmages/avatar"
for link in img_links:
    response = requests.get(link)
    filename = link.split('/')[-1]
    with open(f'{dir}/{filename}', 'wb') as f:
        f.write(response.content)
