import requests
from retrying import retry


# # requests.get
# response = requests.get('https://api.github.com')
# print('response:', response)
# print('response.status_code:', response.status_code)
# print('response.text:', response.text)
# print('response.content:', response.content)    # download files like videos, pictures and musics...
# print('response.content decoded:', response.content.decode('utf-8'))    # using response.content.decode('utf-8') to decode the data    # 处理中文乱码!!!
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
# To simulate browser operations, need to add request headers. !!!
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
# print('#' * 500)
#
# # redirect
# response_ar = requests.get("https://www.baidu.com", headers=headers, allow_redirects=True)
# cookies_ar = response_ar.cookies
#
# print('cookie: ', cookies_ar)
# print('text: ', response_ar.text)
# print('code: ', response_ar.status_code)
#
# print('#' * 500)
# response_no_ar = requests.get("https://www.bilibili.com", headers=headers, allow_redirects=False)
# cookies_no_ar = response_no_ar.cookies
#
#
# # request with cookie
#
#
# cookies = {
#     '__cfduid': 'dfaedafedasfeas',
# }
#
# response = requests.get("https://www.baidu.com", cookies=cookies)
# print('response with cookies: ', response)
# print('response with cookies: ', response.text)
#
#
# # session: session can save cookies, headers and other data, which can be used for multiple requests. !!!
#
# headers = {
#     "accept" : "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
#     "accept-encoding" : "gzip, deflate, br, zstd",
#     "accept-language" : "en-US,en;q=0.9,zh-CN;q=0.8,zh;q=0.7",
#     "cache-control" : "no-cache",
#     "user-agent" : "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/146.0.0.0 Safari/537.36",
# }
#
# session = requests.session()
# res = session.get('https://www.baidu.com',headers=headers)
# print('session cookies: ', res.cookies)
# res_2 = session.post('https://www.baidu.com',headers=headers)
# print('request headers: ', res_2.request.headers)
#
# print('convert cookies from cookiejar to dict: ', requests.utils.dict_from_cookiejar(res.cookies))
#
# res_3 = session.get('https://www.baidu.com',headers=headers,verify=False)   # verify=False can ignore SSL certificate verification, but it is not recommended to use it in production environment, because it will make your application vulnerable to man-in-the-middle attacks. !!!
#
#
# # session proxy: hide
# proxies = {
#     "http" : "http://8.138.131.110:3128",
#     "https" : "https://8.138.131.110:3128",    # when using https, it returns real ip, because the website only support http, it only matches http proxy, so it will return real ip when using https. !!!
# }
# response = requests.get('http://httpbin.org/ip',proxies=proxies, timeout=5)
# print(response.text)
#

# retry can be implemented in at least four ways.
# 1. if/else
# 2. try and if/else
# 3. retry from requests library
# 4. retrying library, it can retry the function when it raises an exception, and it can also set the number of retries and the delay between retries. !!!

@retry(stop_max_attempt_number=3, wait_fixed=1000)    # stop_max_attempt_number: the maximum number of retries, wait_fixed: the delay between retries in milliseconds
def parse_url(url):
    '''
    When timeout occurs, it will raise a requests.exceptions.Timeout exception, and the retrying library will catch this exception and retry the function.
    :param url: text
    :return: obj, response
    '''
    print('start request...')
    response = requests.post(url, timeout=3)
    assert response.status_code == 200, 'wrong status code'
    return response

res = parse_url('https://www.baidu.com')
print(res.status_code)
















