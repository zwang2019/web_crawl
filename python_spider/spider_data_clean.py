# re module
import re


data = """
abc
ABC
AbC123
hello_world
foo-bar
foo bar

# 🔢 Numbers
0
123
-123
+456
3.14
-0.001
1e10
-2.5E-3

# 📅 Dates
2026-04-01
01/04/2026
04-01-26
2026/4/1
1 Apr 2026
April 1, 2026

# 🕒 Time
23:59
00:00
12:30:45
7:05 AM
11:59 PM
23:59:59.999

# 📧 Emails
test@example.com
user.name+tag@gmail.com
user_name@sub.domain.co.uk
invalid@email
@test.com
user@.com

# 🌐 URLs
https://example.com
http://example.com/path
https://sub.domain.com:8080/query?q=1
ftp://ftp.example.com/file.txt
www.example.com
invalid://url

# 📱 Phone Numbers
1234567890
+1-202-555-0173
(202) 555-0173
+61 412 345 678
020-7946-0958

# 🔑 Password-like Strings
password
Password123
P@ssw0rd!
123456
!@#$%^&*
Aa1!Aa1!

# 🧾 JSON-like
{"key": "value"}
{"id": 123, "active": true}
[1, 2, 3]
{"nested": {"a": 1}}
invalid json

# 📦 UUID / IDs
550e8400-e29b-41d4-a716-446655440000
123e4567-e89b-12d3-a456-426614174000
not-a-uuid

# 💻 IP Addresses
192.168.1.1
255.255.255.255
0.0.0.0
256.256.256.256
::1
2001:0db8:85a3:0000:0000:8a2e:0370:7334

# 🏦 Credit Cards
4111 1111 1111 1111
5500-0000-0000-0004
340000000000009
1234 5678 9012 3456

# 📁 File Paths
C:\\Users\\test\\file.txt
/home/user/file.txt
./relative/path/file.py
../up/one/level

# 🏷️ HTML / XML
<div>Hello</div>
<a href="https://example.com">Link</a>
<img src="image.png" />
<invalid<tag>>

# 🔣 Special Characters
!@#$%^&*()
[]{}<>
~`|\:;"'
,./?

# 🌍 Unicode / Multilingual
你好
こんにちは
안녕하세요
Привет
مرحبا
😊😂🔥

# 🧪 Edge Cases

\t
\n
.
*
^$
aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa

# 🔥 Mixed Real-world Strings
User: john_doe123, Email: john@example.com
Order #12345 placed on 2026-04-01
Visit https://example.com?user=123&id=456
Password=P@ssw0rd!; Valid=true
IP: 192.168.0.1, Port: 8080
"""


res = re.match("\n.*\s*.*", data)
print('re obj: ', res)
print('matched result: ', res.group())



url_test = 'https://example.com/?w=1'
res_1 = re.match('https://(example.com)/', url_test)
print(res_1.group(1))
res_2 = re.match('https?://(.*)/', url_test)
print(res_2.group(1))

# re.I: case-insensitive matching
print(re.match('abc', 'ABC', re.I).group())
# re.M:
# re.M: multi-line matching
print(re.findall('^abc', 'abc\nABC', re.M))
print(re.findall('^ABC', 'abc\nABC', re.M))
# re.S: dot matches all characters, including newlines
print(re.match('.*', 'abc\n123', re.S).group())









