import requests
from bs4 import BeautifulSoup

def get_html_text(url):

    
    header = {'user-agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36'}
    r = requests.get(url, headers = header)

    # r = requests.get(url)
    soup = BeautifulSoup(r.text, 'html.parser')
    text = (soup.select('div')[0].text+ soup.select('div')[1].text)
    #text = list(filter(None, text))
    # text = re.sub(r"\n+", " ", text)
    # text = re.sub(r"\t+", " ", text)
    # sentences = re.split("[\.?!]\s+", text)
    # for x in sentences:
    #   x.split()
    
    return text


