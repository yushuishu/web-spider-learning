# -------------------------------
# @Author : 谁书-ss
# @Time   : 2020/1/12 18:03
# -------------------------------

'''

它是 URLError 的子类，专门用来处理 HTTP 请求错误，比如认证请求失败
如下属性
  code：返回 HTTP 状态码
  reason：同父类一样，用于返回错误的原因
  headers：返回请求头

'''

from urllib import request, error

try:
    response = request.urlopen('https://cuiqingcai.com/index.htm')
except error.HTTPError as e:
    print(e.reason, e.code, e.headers, sep='\n')

# 因为 URLError 是 HTTPError 的父类，
# 所以可以先选择捕获子类的错误，再去捕获父类的错误。
# 如果不是 HTTPError 异常，就会捕获 URLError 异常，最后用else处理正常逻辑
try:
    response = request.urlopen('https://cuiqingcai.com/index.htm')
except error.HTTPError as e:
    print(e.reason, e.code, e.headers, spe='\n')
except error.URLError as e:
    print(e.reason)
else:
    print('Request Successfully')
