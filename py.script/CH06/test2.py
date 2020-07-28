import requests

url = 'http://localhost:7777/add'
name = '김유진'
content = '테스트중입니다.'
data={'name' :name,'content': content}  #파라미터값 전달
response = requests.post(url=url, data=data)
# print(response.text)