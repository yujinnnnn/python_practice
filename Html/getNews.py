import sys
from urllib.request import urlopen
import datetime
#파일명을 만들 때 날짜와 시간으로 구분해서 만들기 위함

news_url = open('news_url.txt','r')
news_url_arr = news_url.read().split("\n")
news_url_arr.pop() #맨 끝 데이터 삭제

num = 0
for i in news_url_arr:
    num += 1
    f = urlopen(i)
    encoding = f.info().get_content_charset(failobj="utf-8")
    text = f.read().decode(encoding)
    html_file = open(str(num)+'_news_data.html', 'w')
    html_file.write(text)
    html_file.close


33
