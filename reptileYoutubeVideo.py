import os
import requests
from bs4 import BeautifulSoup

# 设置保存视频的路径
save_path = '/reptile_data/files/youtube-video'

# 创建保存路径文件夹（如果不存在）
os.makedirs(save_path, exist_ok=True)

# YouTube 页面 URL
url = 'https://www.youtube.com/results?search_query=高清风景'

# 发起 HTTP 请求获取页面内容
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')
print(soup)
# 解析页面获取视频链接
video_links = soup.select('.yt-uix-tile-link')

# 遍历视频链接并下载
for link in video_links:
    video_url = 'https://www.youtube.com' + link['href']
    video_id = link['href'][9:]
    download_url = f'https://www.ssyoutube.com/watch?v={video_id}'

    # 发起 HTTP 请求获取视频下载链接
    response = requests.get(download_url)
    soup = BeautifulSoup(response.text, 'html.parser')

    # 解析页面获取视频下载链接
    download_link = soup.select('.download-box a')[0]['href']

    # 下载视频并保存到指定路径
    video_response = requests.get(download_link, stream=True)
    video_name = link.text.strip() + '.mp4'
    video_path = os.path.join(save_path, video_name)

    with open(video_path, 'wb') as f:
        for chunk in video_response.iter_content(chunk_size=1024):
            if chunk:
                f.write(chunk)

    print(f'已下载保存视频：{video_name}')
