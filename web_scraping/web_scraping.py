import bs4
import urllib.request

url = 'https://pythonprogramming.net/parsememcparseface/'
source = urllib.request.urlopen(url).read()
soup = bs4.BeautifulSoup(source, 'lxml')
for url in soup.find_all('a'):
    print(url.get('href'))