import http.client
import json
import sys
import time

import pymysql.cursors
from django.http import HttpResponse
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.chrome.options import Options


def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")


def user(request):
    # Connect to the database
    connection = pymysql.connect(host='10.211.55.34',
                                 user='root',
                                 password='123456',
                                 database='test',
                                 cursorclass=pymysql.cursors.DictCursor)

    with connection:
        # with connection.cursor() as cursor:
        #     # Create a new record
        #     sql = "INSERT INTO `users` (`email`, `password`) VALUES (%s, %s)"
        #     cursor.execute(sql, ('webmaster@python.org', 'very-secret'))
        #
        # # connection is not autocommit by default. So you must commit to save
        # # your changes.
        # connection.commit()
        print("已连接")
        with connection.cursor() as cursor:
            # Read a single record
            sql = "SELECT `id`,`password`,`name` FROM `user`"
            cursor.execute(sql)
            result = cursor.fetchone()
            print(result)
            return HttpResponse(json.dumps(result))
            cursor.close()
            connection.close()


def pc(request):
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
    url = "https://twitter.com/"

    if sys.platform.startswith('linux'):
        # print("当前系统是 Linux")
        # linunx 下加载驱动
        # 加载谷歌浏览器驱动
        chrome_options = Options()
        # linux下运行记得加上这些参数 ----------------------------
        chrome_options.add_argument('--headless')
        chrome_options.add_argument('--no-sandbox')
        chrome_options.add_argument('--disable-gpu')
        chrome_options.add_argument('--disable-dev-shm-usage')
        # -----------------------------------------------------

        # 加载chromedriver -------------------------------------------------
        # windows 下的 chromedriver 默认加载路径是当前路径下的 chromedriver.exe
        # linux 下的 chromedriver 默认加载路径是 /usr/bin/chromedriver
        # 当然也可以通过 executable_path 自定义
        driver = webdriver.Chrome(options=chrome_options)
        # -----------------------------------------------------------------
    else:
        # print("当前系统不是 Linux")
        # 创建浏览器驱动对象
        driver = webdriver.Chrome()
    print(driver)
    # driver = webdriver.Firefox(executable_path='/usr/local/bin/geckodriver')
    # endDate = startDate = startDate + timedelta(days=i)
    # 打开网页
    driver.get(url)

    # WebDriverWait(driver,10).
    # 打开登录窗口
    open_button_login = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "//a[@data-testid='login']")))
    open_button_login.click()
    time.sleep(5)

    # 获取账号密码输入框
    input_email_element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "//input[@autocomplete='username']")))
    # 获取下一步按钮
    buttons = WebDriverWait(driver, 10).until(EC.presence_of_all_elements_located((By.XPATH, "//div[@role='button']")))
    # for item in buttons:
    # print(BeautifulSoup(item, 'html.parser'))
    page_content = driver.page_source
    soup = BeautifulSoup(page_content, 'html.parser')
    driver.close()
    # 关闭浏览器驱动
    # driver.quit()
    print(soup)
    return HttpResponse(soup)
