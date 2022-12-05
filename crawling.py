from bs4 import BeautifulSoup
import requests

def help():
    string = 'Commands:\n'\
        '1. notice, 공지 → Shows the campus notice of GIST.\n'\
        '2. news, 뉴스 → Shows 5 news headlines of SBS.\n'\
        '3. music, 뮤직 → Shows music ranking Top 10 from Melon.\n'\
        '4. movie → Shows top 10 movies currently playing.\n'\
        '5. stock: <stock ID> → Shows the price of given stock.\n'\
        '6. weather, 날씨 → Shows the current weather of Gwangju.'

    return string


def campusNotice():
    site = 'https://www.gist.ac.kr/kr/html/sub05/050209.html'
    page = requests.get(site)
    soup = BeautifulSoup(page.text, "html.parser")

    elements = soup.select('.bd_list_wrap tbody .lstNtc .title a')
    string = ''
    for index, element in enumerate(elements, 1):
        if index<=5: string+="{}. {}\n".format(index, element.text)
    
    return string

def news():
    site = 'https://media.naver.com/press/055/ranking?type=popular'
    page = requests.get(site)
    soup = BeautifulSoup(page.text, "html.parser")

    elements = soup.select('.press_ranking_list li a div strong')
    string = 'Top 5 News of SBS'
    for index, element in enumerate(elements, 1):
        if index<=5: string+="\n{}. {}".format(index, element.text)
    
    return string

def musicRanking():
    h = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.212 Safari/537.36"}
    site= 'https://www.melon.com/chart/index.htm'
    page = requests.get(site, headers = h)
    soup = BeautifulSoup(page.text, "lxml")

    titles = soup.select('tbody div.ellipsis.rank01 a')
    artists = soup.select('tbody span.checkEllipsis')

    string = 'Top 10 Music from Melon'
    for index in range(10):
        string+="\n{}. {} - {}".format(index+1, titles[index].text, artists[index].text)

    return string

def movieRanking():
    site= 'https://movie.naver.com/movie/sdb/rank/rmovie.naver'
    page = requests.get(site)
    soup = BeautifulSoup(page.text, "html.parser")

    elements = soup.select('tbody td.title a')
    string = 'Top 10 Movie from Naver'
    for index, element in enumerate(elements, 1):
        if index<=10: string+="\n{}. {}".format(index, element.text)
    return string

def stockPrice(stock_id):
    site= 'https://finance.yahoo.com/quote/'+stock_id+'?p='+stock_id+'&.tsrc=fin-srch'
    page = requests.get(site)
    soup = BeautifulSoup(page.text, "html.parser")

    try:
        price = soup.select_one('div.D\(ib\).Mend\(20px\) fin-streamer').text
        rate = soup.select_one('div.D\(ib\).Mend\(20px\) fin-streamer:nth-child(2) > span').text
        string = 'Price of {} : {}, {} % today'.format(stock_id, price, rate)
    except:
        string = 'No stock exist with ID : {}'.format(stock_id)

    return string

def weather():
    site= 'https://weather.com/en-GY/weather/today/l/95fc36941623059ef1c4846d2aa90c7c25957fc246f7977c443cf8c96e6e27cd'
    page = requests.get(site)
    soup = BeautifulSoup(page.text, "html.parser")

    weather = soup.select_one('div.CurrentConditions--phraseValue--mZC_p').text
    temp = soup.select_one('div.CurrentConditions--primary--2DOqs > span').text
    high = soup.select_one('div.CurrentConditions--tempHiLoValue--3T1DG > span:nth-child(1)').text
    low = soup.select_one('div.CurrentConditions--tempHiLoValue--3T1DG > span:nth-child(2)').text
    string = "Today's weather : {} \nCurrent Temperature : {}C, High : {}C, Low : {}C".format(weather, temp, high, low)

    return string

