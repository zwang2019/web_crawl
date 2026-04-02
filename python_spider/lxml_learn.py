from lxml import etree

text = '''
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Title</title>
</head>
<body>
<table class="layui-table">
    <tbody class="ips">
    <tr class="zone">>
        <td class="ip" type="1">
            111.225.152.47
        </td>
        <td class="port">
            8089
        </td>
        <td class="zone">河北省张家口市</td>
        <td>
            电信
        </td>
        <td class="time">
            2024/04/07 16:30:09
        </td>
    </tr>
    <tr>
        <td class="ip" type="2">
            36.6.145.113
        </td>
        <td class="port">
            8089
        </td>
        <td class="zone">安徽省亳州市</td>
        <td>
            电信
        </td>
        <td class="time">
            2024/04/07 16:30:09
        </td>
    </tr>
    </tbody>
</table>

<a name="a2 a3" class="a a1" names="qbd" href="http://www.baidu.com">去百度</a>
<a name="a2 a3" href="http://www.baidu1.com">去百度1</a>

<img width="100" alt="星际穿越"
     src="https://img3.doubanio.com/view/photo/s_ratio_poster/public/p2614988097.webp" class="">

</body>
</html>
'''

html_obj = etree.HTML(text)
print('get a html obj as etree: ', html_obj)
# print('decode the html obj', etree.tostring(html_obj).decode('utf-8'))

# xpath
# nodename:Select all child nodes of this node
# /: Select direct child nodes from the current node
# //: Select descendant nodes (all levels below the current node)
# .: Select the current node
# ..: Select the parent node of the current node
# @: Select attributes

print(html_obj.xpath('//*'))
print(html_obj.xpath('//tr/td[1]/text()'))
print(html_obj.xpath('//tr[@class="zone"]/td[1]/text()'))
print('*' * 500)
print(html_obj.xpath('//a/@href'))
print(html_obj.xpath('//img/@src'))
# contains()
print(html_obj.xpath('//a[contains(@name, "a2")]/text()'))
# condition:
print(html_obj.xpath('//tr/td[3][text()="河北省张家口市"]/text()'))
print(html_obj.xpath('//a[@href="http://www.baidu.com"]/@names'))
# multiple contains
print(html_obj.xpath('//a[contains(@name, "a2") and not(contains(@class, "a"))]/text()'))    # and/or/not
# reverse:
print(html_obj.xpath('//tr/td[last()-1]/text()'))
# positon:
print(html_obj.xpath('//tr/td[position()>1 and position()<4]/text()'))






