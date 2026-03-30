import requests


# # requests.get
# response = requests.get('https://api.github.com')
# print('response:', response)
# print('response.status_code:', response.status_code)
# print('response.text:', response.text)
# print('response.content:', response.content)    # download files like videos, pictures and musics...
# print('response.content decoded:', response.content.decode('utf-8'))    # using response.content.decode('utf-8') to decode the data    # 处理中文乱码
# print('response.headers:', response.headers)
# print('response.cookies:', response.cookies)
# print('response.encoding:', response.encoding)
# response.encoding = 'utf-8'
# print('response.text:', response.text)    # using response.encoding to decode the data
#
# try:
#     print('response.json:', response.json())    # only for JSON data, it will decode the data to dict
#     print(type(response.json()))
# except:
#     pass
# print('response.request.headers:', response.request.headers)
#
#
# # requests.post
# data = {
#     "username": "admin",
#     "password": "123456",
# }
# response = requests.post('https://api.github.com', data=data)
# print(response)
#
#
# # To simulate browser operations, need to add request headers.
# headers = {
#     "accept" : "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
#     "accept-encoding" : "gzip, deflate, br, zstd",
#     "accept-language" : "en-US,en;q=0.9,zh-CN;q=0.8,zh;q=0.7",
#     "cache-control" : "no-cache",
#
#
#
#     "user-agent" : "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/146.0.0.0 Safari/537.36",
# }
#
# response = requests.get("https://www.baidu.com")
# print('response without header: ', response)
# print('response without header: ', response.text)
# print('#' * 500)
# response = requests.get("https://www.baidu.com", headers=headers)
# print('response with header: ', response)
# print('response with header: ', response.text)
#
