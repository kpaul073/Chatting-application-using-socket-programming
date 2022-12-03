from bs4 import BeautifulSoup
import requests

site = 'https://www.gist.ac.kr/kr/html/sub05/050209.html'
page = requests.get(site)
soup = BeautifulSoup(page.text, "html.parser")

elements = soup.select('.bd_list_wrap tbody .lstNtc .title a')

for index, element in enumerate(elements, 1):
		print("{} 번째 게시글의 제목: {}".format(index, element.text))