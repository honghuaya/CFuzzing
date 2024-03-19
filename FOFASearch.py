# FOFA直接搜索并爬取相应的数据

import math
import requests
from lxml import etree

# 请求头配置fofa_token
header = {
    'cookie': ' '
}

url = 'https://fofa.info/result?qbase64=dGl0bGUgPSLkuIrmtbfkuqTpgJrlpKflraYiICYmIGNvdW50cnk9IkNOIg%3D%3D'
# 发送GET请求获取页面内容
response = requests.get(url, headers=header)
response.raise_for_status()  # 如果请求失败，会抛出HTTPError异常
html = response.content
# 解析内容
element = etree.HTML(html)

# 获取匹配个数
nodes = element.xpath('//p[@class="hsxa-nav-font-size"]/span[@class="hsxa-highlight-color"]/text()')
for node in nodes:
    # 获取页数
    node = int(node.replace(',', '')) / 10
    # 取最大整数作为遍历范围
    pages = math.ceil(node)
    for page in range(1, 3):
        print(f"正在获取第{page}页...")
        url = f"https://fofa.info/result?qbase64=dGl0bGUgPSLkuIrmtbfkuqTpgJrlpKflraYiICYmIGNvdW50cnk9IkNOIg%3D%3D&page={page}&page_size=10"
        print(url)

        # 获取域名
        domain = element.xpath('//span[@class="hsxa-host"]//a[@href]/text()')
        for domains in domain:
            # 去除字符串两端的空格
            domains = domains.strip()
            # 去除字符串内部的连续空格为一个空格
            domains = ' '.join(domains.split())
            print(domains)

# # 获取title
# title = element.xpath('//div[@class="hsxa-meta-data-list-main-left hsxa-fl"]/p[@class="el-tooltip hsxa-one-line item"]/text()')
# for titles in title:
#     # 去除字符串两端的空格
#     titles = titles.strip()
#     # 去除字符串内部的连续空格为一个空格
#     titles = ' '.join(titles.split())
#     print(titles)