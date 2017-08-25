from bs4 import BeautifulSoup

html = """
<html>
    <body>
        <h1 id="title">What is a scrapping?</h1>
        <p id="body">1. Analyze web pages</p>
        <p>2. Extract portion of web pages</p>
    </body>
</html>
"""

soup = BeautifulSoup(html, 'html.parser')

title = soup.find(id="title")
body = soup.find(id="body")

print("title:", title.string)
print("body:", body.string)
