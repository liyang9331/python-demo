import requests
from bs4 import BeautifulSoup
import os

dir = "/Users/macosx/Desktop/项目文档/-demo/Crawlmages/app_logos"
# 创建保存图片的文件夹
if not os.path.exists(dir):
    os.makedirs(dir)

# 请求商店页面
url = 'https://pc.qq.com/category/c0.html'
response = requests.get(url)

# 解析页面HTML
soup = BeautifulSoup(response.text, 'html.parser')

# 获取最热门应用元素并遍历
apps = soup.find_all('li', class_='category-item bottom-shadow J_cat_item')
for app in apps[:100]:
    # 获取应用名称和Logo URL
    app_name = app.find('h2', class_='category-name ellipsis').value
    logo_url = 'https:' + app.find('img', class_='')['src']
    # newName = app_name.encode('utf-8')
    # 下载Logo图片并保存到本地文件夹
    response = requests.get(logo_url)
    with open(f'{dir}/{app_name}.jpg', 'wb') as f:
        f.write(response.content)

    print(f'{app_name} 的Logo已保存')
