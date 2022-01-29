"""导入包"""
import re
import os
import requests

"""下载每一章的函数"""
def downloadnovel(title, chapter_url, chapter_title):
    """
        title -- 小说名
        chapter_url -- 每一章的地址
        chapter_titlehar -- 每一章的名字
    """
    
    filename = './webspider/'+ '%s.txt' %(title)
    fp = open(filename, 'a')
    
    # 获取每一章的小说
    chapter_request = requests.get(chapter_url)
    chapter_request.encoding = 'gbk'
    chapter_html = chapter_request.text
    print(chapter_html)
    # 获取小说内容
    chapter_content = re.findall(r'<div id="content">(.*?)<BR>', chapter_html, re.S)[0]
    
    # 清洗内容
    chapter_content = chapter_content.replace('&nbsp;', '')
    chapter_content = chapter_content.replace('<br />', '')
    chapter_content = chapter_content.replace('\n', '')
    chapter_content = "".join([s for s in chapter_content.splitlines(True) if s.strip()])  # 去除字符串中的空行

    # 写入文件
    fp.write(chapter_title)
    fp.write('\n')
    fp.write(chapter_content)
    fp.write('\n\n')

"""下载小说爬虫"""
def novelwebspider(chapternum):
    
    # 这是一个请求配置选项， 如果没有这个配置，下面get的时候，可能返回空
    headers = {
    'Cookie':'OCSSID=4df0bjva6j7ejussu8al3eqo03',
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
                 ' (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36',
    }
    
    
    # 获取一个网页
    url = "http://www.zzjdkj.cn/book/8/8027/"
    
    # 模拟浏览器发送HTTP请求
    response = requests.get(url, headers=headers)
    
    # 编码方式
    """ 
        这里的编码先说一个问题，首先，先输出一下编码方式，如果这里的编码方式使用的ISO-8859-1, 直接转成utf-8依然会出现乱码
        此时，应该用开发者工具去查看原网页的HTML页面中的heard里面的编码。这个网页采用的gbk。 
        不会查看？ F12->network->刷新-> 点开第一个 -> 看head部分的编码
    
    """
    #print(response.encoding)     #  查看一下编码方式，不一定都是utf-8编码
    response.encoding = 'gbk'
    
    # 目标小说主页的网页源码
    html = response.text
    # print(html)
    # 获取每一章的信息（章节， url）， 这里用正则表达式匹配
    dl = re.findall(r'<dl>.*?</dl>', html, re.S)[0]    # re.S很重要，匹配任何字符， 要不然会是空列表
    chapter_info_list = re.findall(r'href="(.*?)">(.*?)<', dl)  # 获取到每一章的信息（地址+章节名）
    #print(chapter_info_list)
    
    
    # 获取小说的名字
    title = re.findall(r'<meta property="og:title" content="(.*?)"/>', html)[0]

    #建立文件保存小说
    downloadpath = './webspider/'
    if not os.path.exists(downloadpath):
        os.mkdir(downloadpath)
    
    dir = downloadpath + '%s.txt' %(title)
    fp = open(dir, 'w', encoding='gbk')
    
    # 接下来去循环访问每一章，去访问，然后一章章的下载
    for chapter_info in chapter_info_list:
        
        # 获取章节地址和章节名
        chapter_url, chapter_title = chapter_info
        chapter_url = 'http://www.zzjdkj.cn/book/8/8027/%s' %chapter_url
        
        # 下面就是下载每一章
        print(chapter_url, chapter_title)
        downloadnovel(title, chapter_url, chapter_title)
        chapternum -= 1
        if chapternum == 0:
            return

"""测试爬虫"""
chapternum = input('您需要下载个多少章节的内容： ')  # 数字
novelwebspider(int(chapternum))   
