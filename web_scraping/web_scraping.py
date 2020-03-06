"""
DOCSTRING
"""
import bs4
import pandas
import urllib.request as request

URL = 'https://pythonprogramming.net/parsememcparseface/'
SOURCE = request.urlopen(URL).read()
SOUP = bs4.BeautifulSoup(SOURCE, 'lxml')

DATAFRAMES = pandas.read_html(URL, header=0)
for DATAFRAME in DATAFRAMES:
    print(DATAFRAME)

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

def tables():
    """
    DOCSTRING
    """
    table = SOUP.find('table')
    table_rows = table.find_all('tr')
    for table_row in table_rows:
        table_data = table_row.find_all('td')
        row = [i.text for i in table_data]
        print(row)

def xml():
    """
    DOCSTRING
    """
    source = request.urlopen('https://pythonprogramming.net/sitemap.xml').read()
    soup = bs4.BeautifulSoup(source, 'xml')
    for url in soup.find_all('loc'):
        print(url.text)

if __name__ == '__main__':
    xml()
