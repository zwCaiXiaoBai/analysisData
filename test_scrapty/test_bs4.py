# coding:utf8
from bs4 import BeautifulSoup
import re

html_doc = """
<html><head><title>The Dormouse's story</title></head>
<body>
<p class="title"><b>The Dormouse's story</b></p>

<p class="story">Once upon a time there were three little sisters; and their names were
<a href="http://example.com/elsie" class="sister" id="link1">Elsie</a>,
<a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> and
<a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>;
and they lived at the bottom of a well.</p>

<p class="story">...</p>
"""

# 根据网页html字符创创建beautifulsoup对象
soup = BeautifulSoup(
    html_doc,    # html文档字符创
    'html.parser',      # html解析器
    from_encoding = 'utf-8'   # html文档编码
)

# 查找所有标签为a的节点
links = soup.find_all('a')
for link in links:
    print(link.name,link['href'],link.get_text())

# 查找所有标签为a，连接符合/view/123.html形式的节点
link_node = soup.find('a',href='http://example.com/lacie')
print(link_node.name,link['href'],link_node.get_text())


# 查找所有lli正则表达
link_re = soup.find('a',href = re.compile(r"ill"))
print(link_re.name,link['href'],link_re.get_text())

print('end')