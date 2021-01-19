from bs4 import BeautifulSoup

# HTML 소스코드 

html = """
<html>
    <body>
        <h1 class="title">제목1</h1>
        <p class="content">본문1</p>
        <h1 id="title2">제목2</h1>
        <p id="content2">본문2</p>
    </body>
</html>
"""

# BeautifulSoup로 html 번역하기
soup = BeautifulSoup(html, 'html.parser')

# soup 이쁘게 출력하기
print(soup.prettify())

# 원하는 html 요소 선택하기
# h1 = soup.select_one("h1")
# p = soup.select_one("p")

# h1 = soup.select_one("h1.title2")
# p = soup.select_one("p.content2")

h1 = soup.select_one("h1#title2")
p = soup.select_one("p#content2")

# 요소의 텍스트만 출력하기
print(h1.get_text())
print(p.get_text())