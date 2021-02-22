from bs4 import BeautifulSoup
from urllib.request import urlopen

import argparse
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


def main(file_ext: str, method: str, search_term: str):
    if get_article(search_term) is None:
        print('No results found, try searching for something else.')
        return

    return handle_article(get_article(search_term), file_ext, method)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Process search term query.')
    parser.add_argument('query', metavar='query',  help='the query to search \
                        on the Anarchist library website')
    parser.add_argument('-e', '--ext', default='.html', choices=['.html',
                        '.pdf'], help='specify the file extension')
    parser.add_argument('-m', '--method', default='launch', choices=['launch',
                        'download'], help='choose whether to launch the file \
                        automatically or download it locally')

    parsed = parser.parse_args()
    main(parsed.ext, parsed.method, parsed.query)
