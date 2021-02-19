from bs4 import BeautifulSoup
from urllib.request import urlopen

import argparse
import random
import requests

URL = 'https://theanarchistlibrary.org/'


def main(search, file_type):

    FILE_EXTS = (
        '.html',
        '.pdf'
        )

    if file_type not in FILE_EXTS:
        raise ValueError(f"'{file_type}' is not one of {FILE_EXTS}")

    search_url = ''.join((URL, 'search?query=', search))

    page = requests.get(search_url)
    soup = BeautifulSoup(page.content, 'html.parser')
    article = random.choice([link.get('href') for link in soup.find_all(
        'a', class_='list-group-item')])

    dl_path = ''.join((article, file_type))
    dl_file = dl_path.split('/')[-1]

    response = urlopen(dl_path)
    fil = open(dl_file, 'wb')
    fil.write(response.read())
    fil.close()


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Process search term query.')
    parser.add_argument('query', metavar='query',  help='the query to search \
        on the Anarchist library website')
    parser.add_argument('--extension', dest='ext', help='specify the file \
        extension')

    parsed = parser.parse_args()
    main(parsed.query, parsed.ext)
