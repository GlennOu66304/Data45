import requests

r = requests.get('https://www.douban.com')
print(r.text)