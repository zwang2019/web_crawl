import hashlib

def md5(text):
    m = hashlib.md5()
    m.update(text.encode('utf-8'))
    return m.hexdigest()



text = '123456'
print(f'md5 of {text} is {md5(text)}')