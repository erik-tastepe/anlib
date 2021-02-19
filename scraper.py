import requests
from bs4 import BeautifulSoup

URL = 'https://theanarchistlibrary.org/search?query='
query = input("What would you like to search: ")

def search_topic(search=query):
    full_url = ''.join((URL, search))

    page = requests.get(full_url)
    soup = BeautifulSoup(page.content, 'html.parser')

if __name__ == '__main__':
    search_topic()
