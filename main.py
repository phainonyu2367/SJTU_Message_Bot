from sjtuMessageClient import *
from urllib.parse import urljoin
from AI_Client import AIclient
import pandas

def main():
    index_text = scrape_message(URL)
    tgs = cat_soup_maker(index_text)
    for tg in tgs:
        path = tgs[tg][0]
        article_text = scrape_message(urljoin(BASE_URL, path))
        tgs[tg].append(arti_soup_maker(tgs[tg][1], article_text))
    return tgs
        

if __name__ == "__main__":
    tgs = main()
    for tg in tgs:
        print(tg)
