# # 导入依赖库
import time

from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

# 工具函数-下载图片

'''
打开指定网页，并使用 Selenium 模拟点击 "GDPR-accept" 按钮，然后循环点击 "search-show-more-button" 按钮来加载更多数据，直到按钮不再可点击为止。最后，获取完整的分页数据并关闭浏览器驱动。
'''

# # json 数据
data = []
image_key = 0
fileDir = "./reptile_data/news/nytimes/"
# year = datetime(2021, 1, 1)
# startDate = datetime(2020, 12, 31)  # 初始日期
# endDate = datetime(2020, 12, 31)  # 结束日期
url = "https://www.facebook.com/"
# 创建浏览器驱动对象
driver = webdriver.Chrome()

# endDate = startDate = startDate + timedelta(days=i)
# 打开网页
driver.get(url)

# 获取账号密码输入框
input_email_element = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.XPATH, "//input[@name='email']")))
input_pwd_element = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//input[@name='pass']")))
# 获取登录按钮
button_login = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//button[@name='login']")))

input_email_element.send_keys("liyang19970814@gmail.com")
input_pwd_element.send_keys("xn89kiPT/^Kaeg#")
button_login.click()
# print("---------------")
# print(input_email_element)
# print(input_pwd_element)
# print(button_login)
# logger.debug(button)
# 模拟点击按钮多次加载更多数据
# while button.is_enabled():
#     time.sleep(2)  # 等待一段时间，确保页面加载完毕
#     try:
#         button.click()
#         button = WebDriverWait(driver, 5).until(
#             EC.element_to_be_clickable((By.XPATH, "//button[@data-testid='search-show-more-button']")))
#     except:
#         break
time.sleep(3)
# 获取完整的分页数据
page_content = driver.page_source
soup = BeautifulSoup(page_content, 'html.parser')
print("----------")
print(soup)
# list_news = soup.find_all('li', {"class": "css-1l4w6pd"})

# for index, item in enumerate(list_news):
#     logger.debug(item)
#     # 抓取图片
#     image_key = image_key + 1
#     url_element = item.find('img', {"class": "css-rq4mmj"})
#     image_url = url_element['src'] if url_element else ""
#     # logger.debug(url)
#     if image_url:
#         # logger.debug(url)
#         # # 下载图片
#         #
#         filename = f"{image_key}.jpg"
#         # logger.debug(filename)
#         # sys.exit()
#         download_image(image_url, f'{fileDir}images/{filename}')
#         # 抓取文字
#         title_element = item.find('h4', {"class": "css-2fgx4k"})
#         introduction_element = item.find('p', {"class": "css-16nhkrn"})
#         title = title_element.get_text() if title_element else ""
#         introduction = introduction_element.get_text() if introduction_element else ""
#         news = {
#             "title": title,
#             "introduction": introduction,
#             "imageName": filename
#         }
#         data.append(news)
# logger.debug(data)
# 将数据保存到文件中
# with open(f'{fileDir}data.json', "w", encoding="utf-8") as file:
#     json.dump(data, file, indent=2, ensure_ascii=False)

driver.close()
# 关闭浏览器驱动
driver.quit()
