import sys
from bs4 import BeautifulSoup

for i in range(5):
    html_file = open('html_file_finance.html','r')
    read_html = html_file.read()
    # read_html = read_html.decode("utf-8")
    soup = BeautifulSoup(read_html, 'html.parser')
    my_data = soup.select(
        '.main_news ul li a' 
    )

qustn = open("spot_title.txt","w")
for i in my_data:
    qustn.write(i.text.strip())
    qustn.write("\n")
qustn.close()

