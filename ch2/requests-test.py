import requests
r = requests.get("http://api.aoikujira.com/time/get.php")

print(r.text)

print(r.content)
