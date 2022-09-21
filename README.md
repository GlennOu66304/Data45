## Grammar syntext:

[Python try except 异常处理详解（入门必读）](http://c.biancheng.net/view/4599.html)   
[Python Try-Except inside of Function]()    

## package issue

[pyecharts](https://pyecharts.org/#/zh-cn/quickstart)    
[NameError: name 'requests' is not defined [closed\]](https://stackoverflow.com/questions/26895371/nameerror-name-requests-is-not-defined).  
[Python 库引用提示：name ‘json‘ is not defined. 问题解决办法](https://blog.csdn.net/qq_38161040/article/details/91410095)   

Reference:[用 python 画出北上广深的地铁路线动态图](https://github.com/GlennOu66304/Data-Sciences/blob/Quantitative_trading/README.md)   

# Mock Up browser

## install the chrome driver

Chrome driver zip install:
[mac 搭建 selenium 与 ChromeDriver 环境](https://www.jianshu.com/p/39716ea15d99)

Brew install:
[方法 1：在 bash 中执行命令安装：brew install chromedriver](https://blog.csdn.net/banshouqi4050/article/details/101650719?utm_medium=distribute.pc_relevant.none-task-blog-2~default~baidujs_title~default-0.pc_relevant_aa&spm=1001.2101.3001.4242.1&utm_relevant_index=3)

## Configuration chrome driver:

[2、设置环境变量：](https://blog.csdn.net/banshouqi4050/article/details/101650719?utm_medium=distribute.pc_relevant.none-task-blog-2~default~baidujs_title~default-0.pc_relevant_aa&spm=1001.2101.3001.4242.1&utm_relevant_index=3)

Error message: "'chromedriver' executable needs to be available in the path":
[Error message: "'chromedriver' executable needs to be available in the path"](https://stackoverflow.com/questions/29858752/error-message-chromedriver-executable-needs-to-be-available-in-the-path)

Mac “'chromedriver' executable needs to be in PATH”
[Mac “'chromedriver' executable needs to be in PATH”](https://www.cnblogs.com/LY-CC/p/11072241.html)

[Add to the PATH on Mac OS X 10.8 Mountain Lion and up](https://www.architectryan.com/2012/10/02/add-to-the-path-on-mac-os-x-mountain-lion/)

处理 session not created: This version of ChromeDriver only supports Chrome version 问题的方法

[处理 session not created: This version of ChromeDriver only supports Chrome version 问题的方法](https://blog.csdn.net/weixin_46308904/article/details/109306234)

## How to clear screen in python?

Ctrl + L
[How to clear screen in python?](https://www.geeksforgeeks.org/clear-screen-python/)

## X path find:

```
2. Hit Ctrl-Shift-X (or Command-Shift-X on OS X), or click the XPath Helper button in the toolbar, to open the XPath Helper console.
3. Hold down Shift as you mouse over elements on the page. The query box will continuously update to show the XPath query for the element below the mouse pointer, and the results box will show the results for the current query.
```

[XPath Helper](https://chrome.google.com/webstore/detail/xpath-helper/hgimnogjllphhhkhlmebbmlgjoejdpjl)

## image process

even though you convert the webp image to the png, you still can not view the
through the png format with preview app on mac, it still keeps the webp format
[留言里有人评论说用 XPath 下载的图片打不开](https://time.geekbang.org/column/article/76001)

## JSONDecodeError: Expecting value: line 1 column 1 (char 0)

```
html = requests.get(url=url,headers={
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.130 Safari/537.36"
    }).text
```

[JSONDecodeError: Expecting value: line 1 column 1 (char 0)](https://time.geekbang.org/column/article/76001)

## Process handle:

1）获取 xpath 时，chrome 浏览器需要安装插件 xpatn-helper；  
2）使用 python3.7，提前引入模块 requests，lxml，selenium，安装这些模块需要更新 pip 至 20 版本；  
3）模拟用户访问浏览器，需要下载 chromedriver.exe,放入 python.exe 所在目录；  
4）图片路径中出现导致编译失败的字符，使用 replace 替换报错字符。      
[总结一下小白编写时遇到的几个问题](https://time.geekbang.org/column/article/76001)     

## Novel Craw

[Python3 爬虫实战教程](https://www.w3cschool.cn/python3/python3-enbl2pw9.html)

[Python 爬虫第一战 爬取小说](https://zhuanlan.zhihu.com/p/114591172)

## “NameError: name ‘re’ is not defined”的解决方案

[“NameError: name ‘re’ is not defined”的解决方案](https://blog.csdn.net/mathematican/article/details/118529036)

[Remote end closed connection without response](https://blog.csdn.net/m0_50061234/article/details/119542517)

## Repo

https://github.com/cystanford/pachong/blob/master/douban_love_download.py
