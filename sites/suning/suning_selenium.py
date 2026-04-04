from selenium.webdriver.chrome.webdriver import WebDriver   # using explicit import to solve _LAZY_IMPORTS causing IDE can't recognize the WebDriver class and its methods
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import time
import json
import csv

my_options = Options()
my_options.add_argument('--disable-blink-features=AutomationControlled')
my_options.add_experimental_option('excludeSwitches', ['enable-automation'])
my_options.add_experimental_option('useAutomationExtension', False)



# scroll to the bottom
def scroll_to_the_bottom(browser, bottom_line=10600):
    """
    scroll to the bottom of the page
    :param browser: selenium.webdriver.chrome.webdriver
    :param bottom_line: int
    :return:
    """

    print("scrolling to bottom of the page...")

    counter = 0

    while counter < 1000:
        counter += 1
        scroll_height = 200 * counter
        browser.execute_script(f"window.scrollTo(0,{scroll_height})")
        time.sleep(0.1)
        if scroll_height >= bottom_line:
            break
        if counter == 999:
            print('not reach the end')
    print("reach the end of the page.")

    return


def extract_values(browser):
    """
    extract all values from all elements
    :param browser:
    :return:
    """
    book_list = []

    book_name = browser.find_elements(By.XPATH, '//div[@class="title-selling-point"]/a')
    book_price = browser.find_elements(By.XPATH, '//div[@class="price-box"]/span')
    book_shop = browser.find_elements(By.XPATH, '//div[@class="store-stock"]/a')

    for i in range(len(book_name)):
        temp = {}
        temp['book_name'] = book_name[i].text
        temp['book_price'] = book_price[i].text
        temp['book_shop'] = book_shop[i].text
        book_list.append(temp)

    return book_list



if __name__ == '__main__':

    collect_url = r"https://list.suning.com/0-502282-0.html?safp=d488778a.46602.crumbs.2&safc=cate.0.0&safpn=10006.502282#search-path"
    bottom_line = 10600
    collect_page = 5
    book_id = 0
    field_names = ['book_id', 'book_name', 'book_price', 'book_shop']

    browser = WebDriver(options=my_options)
    browser.get(collect_url)

    # json problem:
    with open('suning_book_list.json', 'a', encoding='utf-8') as f:
        f.write('[' + '\n')

    # csv
    with open('suning_book_list.csv', 'a', encoding='utf-8-sig', newline='') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=field_names)
        writer.writeheader()

    for page in range(collect_page):

        # wait
        wait = WebDriverWait(browser, 5)
        wait.until(EC.presence_of_all_elements_located(('xpath', '//*')))

        # scroll to the bottom of the window
        scroll_to_the_bottom(browser)

        # extracted the value
        page_book_list = extract_values(browser)

        # save the data
        # to JSON
        print('saving to JSON...')
        with open('suning_book_list.json', 'a', encoding='utf-8') as f:
            for item in page_book_list:
                f.write(json.dumps(item, indent=4, ensure_ascii=False) + ',' + '\n')

        # to csv
        print('saving to CSV...')
        with open('suning_book_list.csv', 'a', encoding='utf-8-sig', newline='') as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=field_names)
            for item in page_book_list:
                item['book_id'] = book_id
                writer.writerow(item)
                book_id += 1

        time.sleep(0.5)

        # move to next page
        browser.find_element(By.XPATH, '//a[@id="nextPage"]').click()

    # json problem:
    with open('suning_book_list.json', 'a', encoding='utf-8') as f:
        f.write(']')

    print('program finished...')
    print('ending in 3 seconds...')
    time.sleep(3)




