# FOFA通过API接口获取指定目标文件并捕获指定目标信息

import base64
import requests


def get_data(key):
    try:
        # 从指定文档读取，并将捕获到的目标写入到新文档中
        with open('edu_data.txt', encoding='utf-8') as r, open('target.txt', 'a', encoding='utf-8') as w:
            for edu_data in r:
                edu_num = edu_data.strip()
                # 自定义搜索目标
                search = f'"{edu_num}" && country="CN" && title="Apache Tomcat"'
                b64 = base64.b64encode(search.encode('utf-8')).decode('utf-8')
                url = 'https://fofa.info/api/v1/search/all?&key={}&qbase64={}'.format(key, b64)
                try:
                    # 发送GET请求获取内容
                    response = requests.get(url)
                    response.raise_for_status()  # 如果请求失败，会抛出HTTPError异常
                    # 解析内容并写入文档
                    size = response.json()
                    if size['size'] != 0:
                        print(f"{edu_num}: 捕获到Apache Tomcat")
                        for ip in size['results']:
                            print(ip[0])
                            w.write(ip[0] + '\n')
                except requests.RequestException as e:
                    print(f"获取第{edu_num}时出错，错误信息: {e}")
        print("已全部获取并写入指定文档。")
    except FileNotFoundError:
        print("edu_data.txt 文件未找到，请检查文件路径。")
    except IOError as e:
        print(f"文件操作出错: {e}")


if __name__ == '__main__':
    # 配置FOFA_key
    key = ' '
    get_data(key)
