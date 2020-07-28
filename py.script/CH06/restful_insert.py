import requests
import json

# 호출방식 : response = web_request(method_name='GET', url=url, dict_data=data)

def web_request(method_name, url, dict_data, is_urlencoded=True):
    method_name = method_name.upper()
    if method_name not in ('GET','POST'):
        print("다시 함수 호출해주세요. Method가 다릅니다.")
        return 0
    
    if method_name == 'GET':
        response = requests.get(url=url, params=dict_data)
    if method_name == 'POST':
        if is_urlencoded is True:
            response = requests.post(url=url, data=dict_data, headers={'content_type' :'application/x-www-form-urlencoded'})
        else:
            response = requests.post(url=url, data=json.dumps(dict_data), headers={'content_type' :'application/json'})
    dict_meta = {'status_code': response.status_code, 'ok':response.ok, 'encoding': response.encoding, 'content_type':response.headers['content_type']}

    if 'json' in str(response.headers['content_type']): #JSON 형태의 경우
        return {**dict_meta, **response.json()}
    else: #문자열 형태의 경우
        return {**dict_meta, **{'text':response.text}}