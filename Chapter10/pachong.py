# coding:utf-8
# 下载豆瓣爱情的电影封面
import requests
import json

# 下载图片
def download(url, title):
    dir = './' + title + '.jpg'
    try:
        pic = requests.get(url)
        fp = open(dir, 'wb')
        fp.write(pic.content)
        fp.close()
        print(title)
    except requests.exceptions.ConnectionError:
        print('图片无法下载')


for num in range(0, 1000, 20):
    # 构造url，翻页变换参数为start=, tag=电影, gender=爱情, 改变start=后面的数字，可以爬取不同的页
    url = 'https://movie.douban.com/j/new_search_subjects?sort=U&range=0,10&tags=%E7%94%B5%E5%BD%B1&start='\
          + str(num)+'&genres=%E7%88%B1%E6%83%85'
    print(url)
    html = requests.get(url=url, headers={
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.130 Safari/537.36"
    }).text
    # 转为json格式
    res = json.loads(html,encoding='utf-8')
    for result in res['data']:
        cover = result['cover']
        title = result['title']
        download(cover, title)