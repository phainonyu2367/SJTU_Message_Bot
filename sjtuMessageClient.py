from bs4 import BeautifulSoup
from AI_Client import AIclient
from urllib.parse import urljoin
import requests
import lxml


BASE_URL = 'https://www.sjtu.edu.cn/'
URL = 'https://www.sjtu.edu.cn/tg/index.html'

def scrape_message(url: str=URL) -> str:
    """Scraping message from the specified source"""
    print('------------------------------')
    print(f'start page scraping, url={url}')
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
    print('Start index processing')
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
        print('successful index processing')
        print('------------------------------')
        return tg_dict

def arti_soup_maker(time: str, text: str) -> str:
    """divide the specific html to readable article"""
    soup = BeautifulSoup(text, 'lxml')
    try:
        content = soup.body.div.find_all('div')[1].find_all('section')[1].div.div.div.find('div', class_='Article_content').text
    except Exception as e:
        print(f"error occured when proccesing the article's html-text, error {e}")
    else:
        # try:
        #     return content
        # except TypeError:
        #     print('No text in this tg, you might want to check the tg at web-page')
        return content

def get_tg():
    index_text = scrape_message(URL)
    tgs = cat_soup_maker(index_text)
    for tg in tgs:
        path = tgs[tg][0]
        article_text = scrape_message(urljoin(BASE_URL, path))
        tgs[tg].append(arti_soup_maker(tgs[tg][1], article_text))
    return tgs

def AI_summarize(tgs):
    AI_client = AIclient()
    for tg, raw_content in zip(tgs.keys(), list(tgs.values())):
        tgs[tg].append(AI_client.summarize(raw_content[2]))
    return tgs

# TODO: update scrape_message() and arti_soup_maker()(probably write a new func) to handle the pictures