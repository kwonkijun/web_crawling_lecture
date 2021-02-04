import requests
from bs4 import BeautifulSoup

url = 'https://search.naver.com/search.naver?&where=news&query=%EC%82%BC%EC%84%B1%EC%A0%84%EC%9E%90'

response = requests.get(url)
response.raise_for_status()
html = response.text
soup = BeautifulSoup(html, 'html.parser')

headers = soup.select("div.info_group")

for header in headers:
    links = header.select("a.info")

    if len(links) > 1:
        # 네이버 뉴스 링크 url 가져오기 links[0] : 언론사 홈페이지 링크
        sub_url = links[1].attrs['href']
        
        # 예외상황
        # 비정상적인 접근이라고 판단 (Connection aborted) -> 사용자 인 것처럼 (브라우저에서 접근한 것처럼)
        response = requests.get(sub_url, headers={'User-Agent' : 'Mozilla/5.0'})
        response.raise_for_status()
        html = response.text
        soup = BeautifulSoup(html, 'html.parser')
        
        title = soup.select_one("#articleTitle").get_text(strip=True)
        content = soup.select_one("#articleBodyContents").get_text(strip=True)

        print(title)
        print(content)