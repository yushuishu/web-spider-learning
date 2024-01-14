# -*- coding: utf-8 -*-
"""
@Time ：2023-04-05 23:18
@Auth ：谁书-ss
@IDE  ：PyCharm
@Motto：ABC(Always Be Coding)
@Description ：
"""

import requests

# 运行直接报错，错误原因就是URL证书无效，一定要爬取网站内容，可以设置参数控制verify=False
# requests.exceptions.SSLError: HTTPSConnectionPool(host='ssr2.scrape.center', port=443):
# Max retries exceeded with url: / (Caused by SSLError(SSLCertVerificationError(1, '[SSL:
# CERTIFICATE_VERIFY_FAILED] certificate verify failed: self signed certificate (_ssl.c:997)')))
# response = requests.get("https://ssr2.scrape.center/")
response = requests.get("https://ssr2.scrape.center/", verify=False)
print(response.status_code)
print(response.text)

