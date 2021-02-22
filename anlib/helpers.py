from bs4 import BeautifulSoup
from urllib.request import urlopen

import random
import requests
import webbrowser


def get_article(search_term: str):
    BASE_URL = 'https://theanarchistlibrary.org/'
    search_url = ''.join((BASE_URL, 'search?query=', search_term))

    page = requests.get(search_url)
    soup = BeautifulSoup(page.content, 'html.parser')

    articles = [link.get('href') for link in soup.find_all(
        'a', class_='list-group-item')]

    if len(articles) == 0:
        return

    return random.choice(articles)


def handle_article(article: str, file_ext: str, method: str):
    file_path = ''.join((article, file_ext))

    if method == 'launch':
        return webbrowser.open(file_path)

    response = urlopen(file_path)
    dl_file = file_path.split('/')[-1]
    fil = open(dl_file, 'wb')
    fil.write(response.read())
    return fil.close()
