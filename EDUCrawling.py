# 爬取EDU名单

import time
import requests
from lxml import etree


def get_data():
    # 自定义爬取页数范围
    for page in range(1, 211):
        print(f"正在获取第{page}页...")
        url = f"https://src.sjtu.edu.cn/rank/firm/0/?page={page}"
        try:
            # 发送GET请求获取内容
            response = requests.get(url)
            response.raise_for_status()  # 如果请求失败，会抛出HTTPError异常
            html = response.content
            # 解析内容
            element = etree.HTML(html)
            nodes = element.xpath('//td[@class="am-text-center"]//a[@href]/text()')
            # 写入文档
            with open('edu_data.txt', 'a+', encoding='utf-8') as f:
                for node in nodes:
                    print(node)
                    f.write(node + '\n')
                    f.flush()
                    # 避免被封
                    time.sleep(1)
        # 避免程序崩溃
        except requests.RequestException as e:
            print(f"获取第{page}页时出错，错误信息: {e}")
    print("已全部获取并写入指定文档。")


if __name__ == '__main__':
    get_data()
