import requests
from bs4 import BeautifulSoup

def get_html_text(url):

    # 헤더 필요하면 헤더 따오는 모듈도 필요할듯
    #header = {'user-agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36'}
    #r = requests.get(url, headers = header)
    r = requests.get(url)
    soup = BeautifulSoup(r.text, 'html.parser')
    text = soup.select('div')[0].text
    #text = list(filter(None, text))
    
    return text


