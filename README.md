## 1. EDUCrawling.py 此脚本用于爬取数据，并写入到指定的文档
用文本编辑打开脚本，可以修改需要爬取的页数范围

`for page in range(1, 211):`

可以选择爬取任何内容，我这里用的是xpath()函数，当然还有其他解析提取函数

`nodes = element.xpath('//td[@class="am-text-center"]//a[@href]/text()')`

可以指定爬取的数据，写入到指定文档，也可以在代码头部直接定义页面范围和指定文档

`with open('edu_data.txt', 'a+', encoding='utf-8') as f:`

建议设置避免IP被封.我这里设置的延迟1秒

`time.sleep(1)`
## 2. FOFACrawling.py 此脚本用于读取1中爬取到的数据，将捕获的内容写入另一个指定的文档
通过FOFA的API接口，配置你个人的KEY，这里需要FOFA会员

`key = ' '`

这里可以自定义FOFA语句

`search = f'"{edu_num}" && country="CN" && title="Apache Tomcat"'`

同1中可以自定义指定文档

`with open('edu_data.txt', encoding='utf-8') as r, open('target.txt', 'a', encoding='utf-8') as w:`
## 3. FOFASearch.py 此脚本自定义FOFA语句，爬取目标，捕获指定内容
这里需配置FOFA登录cookie的token值

`header = {'cookie': ' '}`

填写FOFA语句形成的URL地址

`url = ''`

我这里用的是xpath()函数来解析网页，还有其他解析函数

`nodes = element.xpath()`

