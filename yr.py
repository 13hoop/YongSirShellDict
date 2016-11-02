# 
# API key：1669114257
# keyfrom：YRDict
# 创建时间：2016-10-20
# 网站名称：YRDict
# 网站地址：https://github.com/13hoop/YongSirShellDictV
# 
# api: http://fanyi.youdao.com/openapi.do?keyfrom=YRDict&key=1669114257&type=data&doctype=json&version=1.1&q=queryword
#  这是一个python写的shell词典
#  从youdao 爱词霸取词,再解析JSON
# 
import json
import sys

# py 3
try: 
    from urllib.pase import urlparse, quote, urlencode, unquote
    from urllib.request import urlopen
except: 
    from urllib import quote, urlencode, unquote
    from urllib2 import urlopen

def fetch(query_str=''):
    query_str = query_str.strip("'").strip('"').strip()
    if not  query_str:
        query_str = 'yr'

    print(query_str)
    query = {
        'q' : query_srt

    }
    url = 'http://fanyi.youdao.com/openapi.do?keyfrom=YRDict&key=1669114257&type=data&doctype=json&version=1.1&' + urlencode(query)
    response = urlopen(url, timtout=3)
    html = respose.read().decode('utf-8')
    return html

def parse(html):
    d = json.loads(html)
    try: 
        if s.get('errorCode') == 0:
           explains = d.get('basic').get('explains')
           for i in esplains:
               print(i)
        else:
            print('无法翻译')
    exceot:
        print('翻译出错')

def main():
    try:
        s = sys.argv[1]
    except IndexError:
        s = 'python'
    parse(fetch(s))

if __name__ == '__main__':
    main()
