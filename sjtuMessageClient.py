from bs4 import BeautifulSoup
from urllib.parse import urljoin
import requests
import lxml
import datetime
import pandas

BASE_URL = 'https://www.sjtu.edu.cn/'
URL = 'https://www.sjtu.edu.cn/tg/index.html'

def scrape_message(url: str) -> str:
    """Scraping message from the specified source"""
    try:
        response = requests.get(url)
        response.raise_for_status()
    except requests.RequestException as e:
        raise requests.RequestException(f'failed to request html pages from server, error ouccred {e}')
    else:
        print('successful page scraping')
        print('------------------------------')
        return response.text

def cat_soup_maker(text: str) -> str:
    """Divide the required information from the specific page"""
    print('Start html-text processing')
    print('------------------------------')
    try:
        soup = BeautifulSoup(text, 'lxml')
        tgs = soup.body.div.find_all('section')[1].div.div.ul.find_all('li')
        tg_dict = {}
        for tg in tgs:
            tg_dict[tg.a.get('title')] = [tg.a.get('href'), tg.span.string]
    except Exception as e:
        raise Exception(f"error occured when proccesing the index's html-text, error {e}")
    else:
        print('successful text processing')
        print('------------------------------')
        return tg_dict

def arti_soup_maker(time: str, text: str) -> str:
    """divide the specific html to readable article"""
    print('Start html-text processing')
    print('------------------------------')
    print(time)
    soup = BeautifulSoup(text, 'lxml')
    try:
        content = soup.body.div.find_all('div')[1].find_all('section')[1].div.div.div.find('div', class_='Article_content').find_all('p')
        article = [text.string for text in content]
    except Exception as e:
        print(f"error occured when proccesing the article's html-text, error {e}")
    else:
        print('successful text processing')
        print('------------------------------')
        try:
            return ' '.join(article)
        except TypeError:
            print('No text in this tg, you might want to check the tg at web-page')