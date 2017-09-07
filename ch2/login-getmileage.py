import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin


#define variables
USER = "id"
PASSWORD = "pw"

session = requests.session()
login_info = {
    "m_id":USER,
    "m_passwd":PASSWORD
}

# login
url_login = "http://www.hanbit.co.kr/member/login_proc.php"
res = session.post(url_login, data=login_info)
res.raise_for_status() # raise stored HTTPError, if one occured.

url_mypage = "http://www.hanbit.co.kr/myhanbit/myhanbit.html"
res = session.get(url_mypage)
res.raise_for_status()

soup = BeautifulSoup(res.text, "html.parser")
mileage = soup.select_one(".mileage_section1 span").get_text()
ecoin = soup.select_one(".mileage_section2 span").get_text()
print("Mileage:", mileage)
print("E-coin:", ecoin)
