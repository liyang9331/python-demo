import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

url = "https://www.ptt.cc/bbs/Gossiping/index.html"

'''
爬取技术方案1:通过url链接爬取
'''


def reptile2url():
    response = requests.get(url)

    # 解析页面HTML
    soup = BeautifulSoup(response.text, 'html.parser')
    print(soup)


# reptile2url()

'''
爬取技术方案2:通过浏览器爬取
'''


def reptile2browser():
    # 创建浏览器驱动对象
    driver = webdriver.Chrome()
    # 打开网页
    driver.get(url)
    button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//button[@class='btn-big']")))
    button.click()
    # time.sleep(2)
    # 获取完整的页面数据
    page_content = driver.page_source
    soup = BeautifulSoup(page_content, 'html.parser')
    print(soup)
    driver.close()
    # 关闭浏览器驱动
    driver.quit()


reptile2browser()
