import requests, json

api = "https://openapi.naver.com/v1/papago/n2mt"
text = '만나서 반갑습니다'
headers = {'Content-Type':'application/x-www-form-urlencoded; charset=UTF-8',
           'X-Naver-Client-Id':'pIcOBxmtdBbIrqgFpvUj',
           'X-Naver-Client-Secret':'Fz5vGVJnOj'}
payload = {'source':'ko',
           'target':'en',
           'text':text}

res = requests.post(api, headers=headers, data=payload)
res.raise_for_status()

data = json.loads(res.text)

print("ko:", text)
print("en:", data["message"]["result"]["translatedText"])
