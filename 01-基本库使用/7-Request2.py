from urllib import request, parse

# 添加构造请求 设置data  headers  method
url = 'https://httpbin.org/post'
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)',
    'Host': 'httpbin.org'
}
data_dict = {
    'name': 'shuishu'
}
data = bytes(parse.urlencode(data_dict), encoding='utf8')
req = request.Request(url=url, data=data, headers=headers, method='POST')
response = request.urlopen(req)
print(response.read().decode('utf-8'))


