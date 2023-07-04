# 导入依赖库
import requests
from bs4 import BeautifulSoup

# 确定要爬取的网址
url = "https://play.google.com/store/apps"

# 发送 HTTP 请求并解析页面内容
response = requests.get(url)
soup = BeautifulSoup(response.content, 'html.parser')

# 找到所有应用的链接并进入详情页
# 列表页面中只包含应用的概要信息，我们需要进入每个应用的详情页面获取 logo 图片。可以通过在列表页面中找到应用的链接来实现这一点

# 找到所有应用的链接
app_links = []
for link in soup.find_all('a', href=True):
    if '/store/apps/details?id=' in link['href']:
        app_links.append(link['href'])

# 进入每个应用的详情页面
for app_link in app_links:
    url = f'https://play.google.com{app_link}'
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')

    # 在详情页面中找到 logo 图片链接
    logo = soup.find('img', {'class': 'T75of nm4vBd arM4bb'})['src']

    # 下载图片
    dir = "/Users/macosx/Desktop/项目文档/python-demo/Crawlmages/app_logos"
    response = requests.get(logo)
    filename = f"{soup.find('h1', {'class': 'Fd93Bb ynrBgc xwcR9d'}).find('span').text}.png"
    with open(f'{dir}/{filename}', 'wb') as f:
        f.write(response.content)
        print(f"Saved {filename}")
