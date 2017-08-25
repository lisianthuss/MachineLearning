import sys
import urllib.request
import urllib.parse

if len(sys.argv) <= 1:
    print("Usage: download-forecast-argv <Region Number>")
    sys.exit()

regionNumber = sys.argv[1]
API = "http://www.kma.go.kr/weather/forecast/mid-term-rss3.jsp"
values = {'stnId': regionNumber}
params = urllib.parse.urlencode(values)

url = API + "?" + params
print("url=", url)

data = urllib.request.urlopen(url).read()
text = data.decode("utf-8")
print(text)

