import requests
import re
from bs4 import BeautifulSoup

url="http://news.naver.com/main/main.nhn?mode=LSD&mid=shm&sid1=101"
html=requests.get(url)
bs_html=BeautifulSoup(html.content,"html.parser")

news_list=bs_html.find_all("a",{"class":"cluster_text_headline"})

for n in news_list:
    news = re.findall('href="(.+?)">(.+?)</a>',str(n))[0]
    title = news[1]
    link = news[0].replace("amp;","") #네이버 링크에서 amp;라는 것 때문에 접근이 불가능하여 별도 처리
    print(title)
    print(link)