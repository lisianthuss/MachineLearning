from selenium import webdriver

USER = ""
PASS = ""

browser = webdriver.PhantomJS()
browser.implicitly_wait(3)

url_login = "https://nid.naver.com/nidlogin.login"
browser.get(url_login)
print("Access to login Page")

# text box에 id/pw 입력
e = browser.find_element_by_id("id")

e.send_keys(USER)
e = browser.find_element_by_id("pw")
e.clear
e.send_keys(PASS)

form = browser.find_element_by_css_selector("input.btn_global[type=submit]")
#print("submit:", form.submit())
print("click:", form.click())
print("click:", form.click())

browser.get("https://order.pay.naver.com/home?tabMenu=SHOPPING")

products = browser.find_elements_by_css_selector(".p_info span")

for product in products:
    print("-", product.text)
browser.save_screenshot("NaverShopping.png")
