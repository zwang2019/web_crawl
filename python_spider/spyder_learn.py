import requests




# requests.get
response = requests.get('https://api.github.com')
print('response:', response)
print('response.status_code:', response.status_code)
print('response.text:', response.text)
print('response.content:', response.content)    # download files like videos, pictures and musics...
print('response.content decoded:', response.content.decode('utf-8'))    # using response.content.decode('utf-8') to decode the data    # 处理中文乱码
print('response.headers:', response.headers)
print('response.cookies:', response.cookies)
print('response.encoding:', response.encoding)
response.encoding = 'utf-8'
print('response.text:', response.text)    # using response.encoding to decode the data

try:
    print('response.json:', response.json())    # only for JSON data, it will decode the data to dict
    print(type(response.json()))
except:
    pass
print('response.request.headers:', response.request.headers)




# # requests.post
# data = {
#     "username": "admin",
#     "password": "123456",
# }
# response = requests.post('https://api.github.com', data=data)
# print(response)
#
