from bs4 import BeautifulSoup

html = """
<html>
    <body>
        <h1>What is a scrapping?</h1>
        <p>1. Analyze web pages</p>
        <p>2. Extract portion of web pages</p>
    </body>
</html>
"""

soup = BeautifulSoup(html, 'html.parser')

h1 = soup.html.body.h1
p1 = soup.html.body.p
p2 = p1.next_sibling.next_sibling

print("h1 = " + h1.string)
print("p = " + p1.string)
print("p = " + p2.string)
