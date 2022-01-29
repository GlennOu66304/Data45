import os
import requests
from lxml import etree
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

search_text = "王祖贤"
start = 0
limit = 9
total = 5

def download(img, title):
    dir = "/Users/glennou/data45/"
    id = title.replace(u'\u200e', u'').replace(u'?', u'') .replace(u'/', u'or')
    if not os.path.exists(dir):
       os.makedirs(dir)
    try:
        pic = requests.get(img, timeout=10)
        img_path = dir + str(id) + '.png'
        fp = open(img_path, 'wb')
        fp.write(pic.content)
        fp.close()
    except requests.exceptions.ConnectionError:
         print('图片无法下载')

def main():
    src_img = "//div[@class='item-root']/a[@class='cover-link']/img[@class='cover']/@src"
    src_title = "//div[@class='item-root']/div[@class='detail']/div[@class='title']/a[@class='title-text']"

    for i in range(start,total,limit):
        request_url = "https://search.douban.com/movie/subject_search?search_text="+search_text+"&cat=1002&start="+str(i)
        driver = webdriver.Chrome(ChromeDriverManager().install())
        driver.get(request_url)
        html = etree.HTML(driver.page_source)
        imgs = html.xpath(src_img)
        titles = html.xpath(src_title)
        print(imgs,titles)
        
        for img, title in zip(imgs, titles):
            download(img, title.text)                  
main()