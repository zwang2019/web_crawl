# current webdriver.exe moved into PATH:D:\Program\PyCharm 2025.3.3\bin
# when Chrome update to a new version, download the corresponding version of webdriver.exe from https://googlechromelabs.github.io/chrome-for-testing/ and replace the old one in PATH

# from selenium.webdriver.chrome.service import Service
# CHROMEDRIVER_PATH = r'D:\Program\PyCharm 2025.3.3\bin\chromedriver.exe'
# svc = Service(executable_path=CHROMEDRIVER_PATH)
# browser = webdriver.Chrome(service=svc)

from selenium.webdriver.chrome.webdriver import WebDriver   # using explicit import to solve _LAZY_IMPORTS causing IDE can't recognize the WebDriver class and its methods
from selenium.webdriver.common.by import By
import time



"""
By
ID: ByType = "id"
XPATH: ByType = "xpath"
LINK_TEXT: ByType = "link text"
PARTIAL_LINK_TEXT: ByType = "partial link text"
NAME: ByType = "name"
TAG_NAME: ByType = "tag name"
CLASS_NAME: ByType = "class name"
CSS_SELECTOR: ByType = "css selector"
"""


browser = WebDriver()
browser.get("https://httpbin.org/")
res = browser.find_element(By.XPATH, "//div[1]/a[1]")
print('element found...', res.text)
res_2 = browser.find_elements(By.XPATH, "//div/a[1]")
print('elements found...', res_2)
for item in res_2:
    print(item.text)
# click
browser.find_element(By.XPATH, "//div[1]/a[1]").click()

time.sleep(5)
browser.get_screenshot_as_file('screenshot.png')




browser.close()
time.sleep(15)