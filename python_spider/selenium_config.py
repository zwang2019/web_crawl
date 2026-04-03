from distutils.core import extension_keywords

from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.chrome.options import Options

import time

my_options = Options()
my_options.add_argument('--headless')    # headless mode, without opening the browser window, using --headless=new to use the new headless mode in Chrome 109 and above
# my_options.add_argument('--proxy-server=http://127.0.0.1:8118')    # use proxy, you can use a proxy to hide your IP address or access blocked websites, replace with your own proxy server address and port
my_options.add_argument('--window-size=1920,1080')    # set the window size, which can help some websites that detect headless mode by checking the window size, and also can improve the rendering of the page in headless mode
my_options.add_argument('--disable-notifications')    # disable notifications
my_options.add_argument('--disable-extensions')    # disable extensions
ua = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/146.0.0.0 Safari/537.36'
my_options.add_argument('--user-agent={}'.format(ua))
my_options.add_argument('--lang=ja-JP')    # set the language, which can help some websites that detect headless mode by checking the language settings
my_options.add_argument('--auto-open-devtools-for-tabs')    # automatically open the developer tools for each tab, which can help you debug the page and see the network requests and responses

my_options.add_experimental_option('excludeSwitches', ['enable-automation'])    # remove the "Chrome is being controlled by automated test software" infobar, which can help some websites that detect headless mode by checking the presence of the infobar
my_options.add_experimental_option('useAutomationExtension', False)    # disable the automation extension, which can help some websites that detect headless mode by checking the presence of the automation extension

my_options.add_argument('--disable-blink-features=AutomationControlled')    # very important # disable the blink features that can reveal the automation, which can help some websites that detect headless mode by checking the blink features

prefs = {"profile.managed_default_content_settings.images": 2}
my_options.add_experimental_option("prefs", prefs)    # no pictures, which can speed up the page loading and reduce the bandwidth usage in headless mode

extension_path = './extension_1_0_0_0.crx'
my_options.add_extension(extension_path)    # add extension, you can use an extension to bypass some anti-crawling measures or add some functionalities, replace with your own extension file path




browser = WebDriver(options=my_options)
browser.get("https://httpbin.org/")
print(browser.page_source)


browser.close()
time.sleep(45)