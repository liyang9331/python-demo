import requests


def download_image(url, save_path):
    response = requests.get(url, stream=True)
    if response.status_code == 200:
        with open(save_path, 'wb') as file:
            for chunk in response.iter_content(1024):
                file.write(chunk)
        # print(f"图片下载成功：{save_path}")
    else:
        print(f"图片下载失败：{url}")
