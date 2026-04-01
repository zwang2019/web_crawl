# https://spidertools.cn/ convert cURL to python requests

import requests


headers = {
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
    "Accept-Language": "en-US,en;q=0.9,zh-CN;q=0.8,zh;q=0.7",
    "Cache-Control": "no-cache",
    "Connection": "keep-alive",
    "Pragma": "no-cache",
    "Sec-Fetch-Dest": "document",
    "Sec-Fetch-Mode": "navigate",
    "Sec-Fetch-Site": "none",
    "Sec-Fetch-User": "?1",
    "Upgrade-Insecure-Requests": "1",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/146.0.0.0 Safari/537.36",
    "sec-ch-ua": "Chromium;v=146, Not-A.Brand;v=24, Google Chrome;v=146",
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": "Windows"
}
cookies = {
    "https_waf_cookie": "eb6c0e22-0e66-4972ae307d0ef776f3352145e4055622e5fa",
    "Hm_lvt_f9e56acddd5155c92b9b5499ff966848": "1774978634,1775029941",
    "Hm_lpvt_f9e56acddd5155c92b9b5499ff966848": "1775029941",
    "HMACCOUNT": "DF75B59B5EB75318"
}
url = "https://www.89ip.cn/"
response = requests.get(url, headers=headers, cookies=cookies)

print(response.text)
print(response)

