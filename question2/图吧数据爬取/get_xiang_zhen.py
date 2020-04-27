from lxml import etree
from selenium import webdriver

driver = webdriver.Chrome()
url_zhen = 'https://poi.mapbar.com/changsha/FF0/'
driver.get(url_zhen)
html = driver.page_source
dom = etree.HTML(html, etree.HTMLParser(encoding='utf-8'))
zhen = dom.xpath('//div[@class="sortC"]/dl/dd/a/text()')

url_xiaoqu = 'https://poi.mapbar.com/changsha/F10/'
driver.get(url_xiaoqu)
html2 = driver.page_source
dom2 = etree.HTML(html2, etree.HTMLParser(encoding='utf-8'))
xiaoqu = dom2.xpath('//div[@class="sortC"]/dl/dd/a/text()')
xiaoqu.index('麓谷明珠小区')

with open('../data/changsha_ns.txt','w') as f:
    for i in zhen:
        f.write(i)
        f.write(' ')
        f.write('ns')
        f.write('\n')
    for i in xiaoqu:
        f.write(i)
        f.write(' ')
        f.write('ns')
        f.write('\n')