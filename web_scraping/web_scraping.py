"""
DOCSTRING
"""
import bs4
import pandas
import PyQt5.QtCore as qt_core
import PyQt5.QtWidgets as qt_widgets
import PyQt5.QtWebEngineWidgets as qt_web_widgets
import requests
import urllib.request as request
import sys

URL = 'https://pythonprogramming.net/parsememcparseface/'
SOURCE = request.urlopen(URL).read()
SOUP = bs4.BeautifulSoup(SOURCE, 'lxml')

DATAFRAMES = pandas.read_html(URL, header=0)
for DATAFRAME in DATAFRAMES:
    print(DATAFRAME)

class Render(qt_web_widgets.QWebEnginePage):
    """
    DOCSTRING
    """
    def __init__(self, html):
        self.html = None
        self.app = qt_widgets.QApplication(sys.argv)
        qt_web_widgets.QWebEnginePage.__init__(self)
        self.loadFinished.connect(self._load_finished)
        self.setHtml(html)
        while self.html is None:
            self.app.processEvents(
                qt_core.QEventLoop.ExcludeUserInputEvents |
                qt_core.QEventLoop.ExcludeSocketNotifiers |
                qt_core.QEventLoop.WaitForMoreEvents)
        self.app.quit()
    
    def _callable(self, data):
        self.html = data

    def _load_finished(self, result):
        self.toHtml(self._callable)

class WebScraping:
    """
    DOCSTRING
    """
    def javascript(self):
        """
        DOCSTRING
        """
        js_test = SOUP.find('p', class_='jstest')
        print(js_test.text)

    def navigating_tags(self):
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

    def tables(self):
        """
        DOCSTRING
        """
        table = SOUP.find('table')
        table_rows = table.find_all('tr')
        for table_row in table_rows:
            table_data = table_row.find_all('td')
            row = [i.text for i in table_data]
            print(row)

    def xml(self):
        """
        DOCSTRING
        """
        source = request.urlopen('https://pythonprogramming.net/sitemap.xml').read()
        soup = bs4.BeautifulSoup(source, 'xml')
        for url in soup.find_all('loc'):
            print(url.text)

if __name__ == '__main__':
    sample_html = requests.get(URL).text
    source = Render(sample_html).html
    print(source)
    soup = bs4.BeautifulSoup(source, 'lxml')
    js_test = soup.find('p', class_='jstest')
    print(js_test.text)
