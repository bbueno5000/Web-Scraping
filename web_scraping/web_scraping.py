"""
DOCSTRING
"""
import bs4
import urllib.request as request

URL = 'https://pythonprogramming.net/parsememcparseface/'
SOURCE = request.urlopen(URL).read()
SOUP = bs4.BeautifulSoup(SOURCE, 'lxml')

def navigating_tags():
    """
    DOCSTRING
    """
    nav = SOUP.nav
    for url in nav.find_all('a'):
        print(url.get('href'))
    print('######################################')
    body = SOUP.body
    for paragraph in body.find_all('p'):
        print(paragraph.text)
    print('######################################')
    for div in SOUP.find_all('div', class_='body'):
        print(div.text)

if __name__ == '__main__':
    navigating_tags()
