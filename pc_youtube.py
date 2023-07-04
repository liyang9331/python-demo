from pytube import YouTube

# ssl._create_default_https_context = ssl._create_stdlib_context

url = "https://www.youtube.com/results?search_query=%E6%96%B0%E9%97%BB"

'''
爬取技术方案1:通过url链接爬取
'''


def callback(str):
    print(str)


def main():
    def Download(link):
        yt = YouTube(link)
        yt.register_on_complete_callback(callback)
        yt.streams.filter(progressive=True, file_extension='mp4')
        steam = yt.streams.get_by_itag(22)
        try:
            steam.download()
        except:
            print("下载失败")

    # reptile2url()
    # reptile2browser()
    Download("https://www.youtube.com/watch?v=z-usxjLa-Dc")


main()
