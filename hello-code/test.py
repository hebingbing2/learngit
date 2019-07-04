import requests
from lxml import etree

addr="https://www.douban.com"
header = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.146 Safari/537.36'}

resq = requests.get(addr,headers = header)
htmlElement = etree.HTML(resq.content)

selectStr ="//ul[@class='time-list']/li/a/img/@src"
list = htmlElement.xpath(selectStr)

for item in list:
    print(item)
