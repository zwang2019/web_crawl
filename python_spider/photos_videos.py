import requests


headers = {
    "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
    "accept-language": "en-US,en;q=0.9,zh-CN;q=0.8,zh;q=0.7",
    "cache-control": "no-cache",
    "pragma": "no-cache",
    "priority": "u=0, i",
    "referer": "https://docs.qq.com/",
    "sec-ch-ua": "\"Chromium\";v=\"148\", \"Google Chrome\";v=\"148\", \"Not/A)Brand\";v=\"99\"",
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": "\"Windows\"",
    "sec-fetch-dest": "document",
    "sec-fetch-mode": "navigate",
    "sec-fetch-site": "cross-site",
    "sec-fetch-user": "?1",
    "upgrade-insecure-requests": "1",
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/148.0.0.0 Safari/537.36"
}
cookies = {
    "H_WISE_SIDS_BFESS": "60271_61027_61219_60853_61492_61493_61520_61528_61612_61680_61721",
    "BDUSS": "Ul3WnM4SHFPRXBtTHYzSGN-eTRXY2dlRWEtV2FyU3BxUU1DckZ6NGxhMDZyQlZwRVFBQUFBJCQAAAAAAAAAAAEAAACbKucKdzQ1ODIzMjQ3NQAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAADof7mg6H-5oV",
    "BDUSS_BFESS": "Ul3WnM4SHFPRXBtTHYzSGN-eTRXY2dlRWEtV2FyU3BxUU1DckZ6NGxhMDZyQlZwRVFBQUFBJCQAAAAAAAAAAAEAAACbKucKdzQ1ODIzMjQ3NQAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAADof7mg6H-5oV",
    "BAIDU_WISE_UID": "wapp_1760636682488_504",
    "ZFY": "Ww:A2O8gzGSSnHChFQiK4t8cKUrJPyR0dIDvqCahtNYQ:C",
    "__bid_n": "187f0ca44e974722579ca9",
    "BIDUPSID": "18F223D8CEDDE04B3D1197D7FFC4CCAF",
    "PSTM": "1773568649",
    "BAIDUID": "DFF313A05A96A77E7464D3FCA3A7D507:FG=1",
    "BAIDUID_BFESS": "DFF313A05A96A77E7464D3FCA3A7D507:FG=1",
    "H_PS_PSSID": "63143_67862_68166_68265_68370_68423_68451_68465_68539_68622_68610_68669_68741_68728_68545_68861_68901_68913_68833_68925_68942_68979_68993_69007_69010_69017_69013_69021_69054_69055_68553_69037_69083_69095_69088_69110_69129_69179_69168_69204",
    "H_WISE_SIDS": "68166_68265_68370_68423_68451_68465_68622_68610_68669_68728_68913_68833_68925_68942_68979_68993_69007_69010_69017_69013_69021_69055_68553_69037_69083_69095_69088_69110_69129_69179_69168_69204",
    "newlogin": "1",
    "MCITY": "-58%3A"
}
url = "https://img1.baidu.com/it/u=84005625,1558799787&fm=253&fmt=auto&app=138&f=JPEG"
params = {
    "w": "640",
    "h": "427"
}
response = requests.get(url, headers=headers, cookies=cookies, params=params)

print(response.text)    # Garbled text
print()
print(response)