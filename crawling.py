from bs4 import BeautifulSoup
import requests

def campusNotice():
    site = 'https://www.gist.ac.kr/kr/html/sub05/050209.html'
    page = requests.get(site)
    soup = BeautifulSoup(page.text, "html.parser")

    elements = soup.select('.bd_list_wrap tbody .lstNtc .title a')
    string = ''
    for index, element in enumerate(elements, 1):
            string+="{}. {}\n".format(index, element.text)
    
    return string

