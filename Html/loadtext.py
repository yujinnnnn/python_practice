import sys
from bs4 import BeautifulSoup

for i in range(5):
    html_file = open('html_file_weather.html','r')
    read_html = html_file.read()

    soup = BeautifulSoup(read_html, 'html.parser')
    my_data = soup.select(
        '.table_midterm' ##content_weather > table:nth-child(7)
    )
    text_file = open(str(i+1)+'_news_read.txt','w',-1,"utf-8")
    text_file.write(my_data[0].get_text())
    text_file.close()
# qustn = open("news_title.txt","w")
# for i in my_data:
#     qustn.write(i.text.strip())
#     qustn.write("\n")
# qustn.close()

# qustn2 = open("news_url.txt","w")
# for i in my_data:
#     qustn.write("https://news.naver.com/"+i.attrs['href'])
#     qustn2.write("\n")
# qustn2.close