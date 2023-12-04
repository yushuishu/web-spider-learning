# -*- coding: utf-8 -*-
"""
@Time ：2020-01-30 17:51
@Auth ：谁书-ss
@IDE  ：PyCharm
@Motto：ABC(Always Be Coding)
"""

import requests

# 调用cookies属性即可得到cookies、使用items()方法将其转化为元组的列表
# 遍历输出每一个cookie的名称和值

r = requests.get("https://www.baidu.com")
print(r.cookies)
for key, value in r.cookies.items():
    print(key + '=' + value)

print('==============================================')
# 也可以直接使用 cookie 来维持登录状态
headers = {
    'Cookie': '_zap=de23013b-c83a-4475-a7b3-20d986869ff0; d_c0="AHCjU40ojBCPTtyADhNt'
              'RRB9Rb-MdvTY4OI=|1577063778"; _xsrf=bu87ENgoCSpoQZQsPNK7fTWwfNWJnYiS; '
              'capsion_ticket="2|1:0|10:1578187300|14:capsion_ticket|44:ZTcxMWNhYjYz'
              'M2E0NDJjYTk4NGJiYjgxN2Q5ZTNlMDU=|b38d78c688743567631fe8b15831b0354b67'
              'af852a436dbf327ba2333a09a5f4"; r_cap_id="NDc4MTdhZTY3MzE1NDgwZWEwZTQ3OTg'
              '0ZTA5YjAyMGI=|1578187311|85514897932f5e979fa6965dc88def9a0f8d80ce"; '
              'cap_id="ODlmMDk3NDg3ZjczNDQ0MDkyMzk0NjJlNDFjNTUzNzQ=|1578187311|9ade17e'
              '70755d3e84e80f74836f8b631168afcfb"; l_cap_id="M2VmYzBjNmVkMjY3NDJhZWEwMz'
              'RjNTNmZWQ4YzkyYmM=|1578187311|9f6d01bd9cd498c4ac2f934dd015423a4e0e564c"; '
              'z_c0=Mi4xM2JXRkRnQUFBQUFBY0tOVGpTaU1FQmNBQUFCaEFsVk5PWWotWGdEOV9DNC1yT1p'
              'TNWFuY2twYUJWLU83ZUdvdEtn|1578187322|fde6e76499442b094e140a7ead85490fe965b'
              '29d; tst=r; q_c1=8b05da5f2d114a0b8e0f69d8707b6335|1579939789000|1579939789'
              '000; Hm_lvt_98beee57fd2ef70ccdd5ca52b9740c49=1580358020,1580368817,1580378'
              '216,1580378483',
    'Host': 'www.zhihu.com',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 '
                  '(KHTML, like Gecko) Chrome/79.0.3945.117 Safari/537.36'
}

r2 = requests.get('https://www.zhihu.com', headers=headers)
print(r2.text)


