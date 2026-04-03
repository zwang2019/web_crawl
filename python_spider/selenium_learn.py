# current webdriver.exe moved into PATH:D:\Program\PyCharm 2025.3.3\bin
# when Chrome update to a new version, download the corresponding version of webdriver.exe from https://googlechromelabs.github.io/chrome-for-testing/ and replace the old one in PATH

# from selenium.webdriver.chrome.service import Service
# CHROMEDRIVER_PATH = r'D:\Program\PyCharm 2025.3.3\bin\chromedriver.exe'
# svc = Service(executable_path=CHROMEDRIVER_PATH)
# browser = webdriver.Chrome(service=svc)

from selenium.webdriver.chrome.webdriver import WebDriver   # using explicit import to solve _LAZY_IMPORTS causing IDE can't recognize the WebDriver class and its methods
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

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

# wait
wait = WebDriverWait(browser, 5)
wait.until(EC.presence_of_all_elements_located(('xpath', '//*')))


res = browser.find_element(By.XPATH, "//div[1]/a[1]")
print('element found...', res.text)
print(res.text, ' href: ', res.get_attribute('href'))

res_2 = browser.find_elements(By.XPATH, "//div/a[1]")
print('elements found...', res_2)
for item in res_2:
    print(item.text)


# click
browser.find_element(By.XPATH, "//div[1]/a[1]").click()
time.sleep(5)
# switch windows:
print(browser.window_handles)
browser.switch_to.window(browser.window_handles[0])
time.sleep(3)
browser.switch_to.window(browser.window_handles[1])

# scroll in JS
# window.scrollBy(0,1000) # scroll down 1000 pixels, using -1000 to scroll up
# window.scrollTo(0,window.document.body.scrollHeight) # scroll to the bottom of the page, using 0,0 to scroll to the top of the page
time.sleep(1)
browser.execute_script("window.scrollBy(0,1000)")
time.sleep(1)
browser.execute_script("window.scrollTo(0,window.document.body.scrollHeight)")

# screenshot
time.sleep(5)
browser.get_screenshot_as_file('screenshot.png')

# cookies
browser.get("https://www.baidu.com/")
web_cookies = browser.get_cookies()  # get all cookies and using https://spidertools.cn/#/formatJSON to format the cookies into a list of dicts, then you can use the cookies in other tools like Postman or Python requests
cookie_dict = {web_cookies[i]['name']: web_cookies[i]['value'] for i in range(len(web_cookies))}  # convert the list of dicts into a dict of name-value pairs, which can be used in Python requests
print(cookie_dict)
zfy = browser.get_cookie('ZFY')    # get a specific cookie by name, which can be used in Python requests
print(zfy)
browser.delete_all_cookies()
time.sleep(5)
print(browser.get_cookies())
browser.add_cookie({'name': 'test_cookie', 'value': 'test_value'})
time.sleep(5)
print(browser.get_cookies())

# page source
time.sleep(5)
page_source = browser.page_source.encode('utf-8')
print(page_source)

# run JS code
js_code = "alert(navigator.webdriver)"
browser.execute_script(js_code)
time.sleep(3)

browser.switch_to.window(browser.window_handles[0])
time.sleep(1)

# back and forward
browser.get("https://www.baidu.com/")
time.sleep(3)
res_post = browser.find_element(By.ID, "chat-textarea")
res_post.send_keys("selenium test")
res_post.send_keys("\n")
time.sleep(5)
browser.back()
time.sleep(3)
browser.forward()
time.sleep(3)


browser.close()
time.sleep(45)