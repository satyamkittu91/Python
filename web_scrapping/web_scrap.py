import requests
from bs4 import BeautifulSoup

def fetchAndSaveToFile(url, path):
    r = requests.get(url)
    with open(path, "w", encoding="utf-8") as file:
        file.write(r.text)


def parseHtmlFile(path):
    with open(path, "r", encoding="utf-8") as file:
        return BeautifulSoup(file.read(), "html.parser")

def get_h5_tags(soup):
    return soup.find_all("h5")
    
#fetchAndSaveToFile("https://timesofindia.indiatimes.com/city/delhi", "times.html")

