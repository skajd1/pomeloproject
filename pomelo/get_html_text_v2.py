import requests
from bs4 import BeautifulSoup
import re


def get_html_text_v2(url):
    session = requests.Session()

    headers = {"User-Agent" : "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/15.2 Safari/605.1.15"}
    html = session.get(url, headers=headers).content
    soup = BeautifulSoup(html, "html.parser")

    for script in soup(["script", "style"]):
        script.extract()

    text = soup.get_text()

    lines = (line.strip() for line in text.splitlines())
    chunks = (phrase.strip() for line in lines for phrase in line.split("  "))
    #text = '\n'.join(chunk for chunk in chunks if chunk)
    text = [chunk for chunk in chunks if chunk]
    #text= re.sub(r"[^0-9가-힣?.!,]+", ' ', text) 
    # text = re.split("[\.?!]\s+", text)
    # text = text.split('\n')
    # text = [re.sub(r"[^0-9가-힣?.!,]+", ' ', l) for l in text]
    #print(text)
    return text

