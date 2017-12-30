from bs4 import BeautifulSoup as bs
from os.path import join
import requests

"""
    This scirpt gets from wikipedia the list of bunny breeds
    This script has its own dependencies, as it is not critical to
    running the server. The only reason to run this script again is if
    the list of rabbit breeds has changed (Very unlikely).
"""


def main():
    breeds = ['Unknown']
    r = requests.get(
        'https://en.wikipedia.org/api/rest_v1/page/html/List_of_rabbit_breeds?sections=mwDg')
    s = bs(r.text, 'html.parser')
    for row in s.find_all('tr')[1:]:
        if row.a:
            breeds.append(row.a.string)

    path = join('..', 'testsite', 'rabbits_rest', 'data', 'breeds.txt')
    with open(path, 'w', encoding='utf-8') as f:
        f.write('\n'.join(breeds))


if __name__ == '__main__':
    main()
