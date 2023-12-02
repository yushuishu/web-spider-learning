# -------------------------------
# @Author : 谁书-ss
# @Time   : 2020/1/14 10:30
# -------------------------------

"""

allow_fragments: 即是否忽略 fragment。如果它被设置为 false ，fragment部分就会忽略，它会被解析成
                path、params、或者 query 的一部分，而 fragment 部分为空

如果 URL 不包含 params 和 query，fragment 会解析为 path 的一部分

返回的结果 ParseResult 实际上是一个元组，可以通过索引顺序来获取，也可以通过属性名获取
"""

from urllib.parse import urlparse

result = urlparse('https://www.baidu.com/index.html;user?id=5#comment', allow_fragments=False)
print(result)
print(result.scheme, result[0], result.netloc, result[1], sep='\n')



