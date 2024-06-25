import requests
from lxml import etree
import os
header={'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.0.0 Safari/537.36'}
url="https://kma.kkbox.com/charts/yearly/newrelease?cate=314&lang=tc&terr=tw"
response = requests.get(url , headers=header)

print(response.content.decode())
html = etree.HTML(response.content.decode())
texts = html.xpath("//html/body/div[3]/div[1]/div[2]/ul/li[17]/a/div/div[2]/span[1]/span[1]")
print(texts[0].text)