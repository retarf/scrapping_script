import certifi
import urllib3
import codecs
from bs4 import BeautifulSoup

web = 'https://www.bankier.pl/gielda/notowania/akcje'
tag = 'tr'
start = 1


def take(web, tag, start):
    """ Function witch take data from web witch have tag from start element and return list of that elements"""
    http = urllib3.PoolManager(
        cert_reqs='CERT_REQUIRED',
        ca_certs=certifi.where())
    req = http.request('GET', web)
    site = codecs.decode(req.data)

    soup = BeautifulSoup(site, "html.parser")
    for tr in soup.findAll('tr', {'class': 'adv'}):
        tr.decompose()
    soup = soup.findAll(tag)
    soup = soup[start:]

    data = []
    for i in soup:
        adv = i.find('tr', {'class': 'adv'})
        if adv:
            print('>>> TR <<<')
            continue
        stock = pool_data(i)
        data.append(stock)

    return data


def pool_data(item):
    """ Function pool data from soup object """
    item = item.prettify()

    soup = BeautifulSoup(item, "html.parser")
    name = soup.a['title']
    code = soup.a.text.strip()
    price = soup.find('td', {'class': 'colKurs'}).get_text().strip()

    data = {'name': name, 'code': code, 'price': price}

    return data


def kody(data):
    end = len(dane) - 1
    for i in dane:
        print(i['code'], end=', ')
        if i == dane[end]:
            print()


def walor(data, item):
    for i in data:
        if i['code'] == item:
            print(i)


if __name__ == '__main__':

    dane = take(web, tag, start)
    zap = 'polna'

    print('>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>')
    kody(dane)
    print('>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>')
    print()
    zap = zap.upper()
    walor(dane, zap)
