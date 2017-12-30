from bs4 import BeautifulSoup as bs
from os.path import join
import requests

"""
    This scirpt gets from wikipedia the list of colors
    This script has its own dependencies, as it is not critical to
    running the server. The only reason to run this script again is if
    the list of colors has changed (SUPER unlikely).
"""


def main():
    links = [
        'https://en.wikipedia.org/api/rest_v1/page/html/List_of_colors:_A–F?sections=mwIQ',
        'https://en.wikipedia.org/api/rest_v1/page/html/List_of_colors:_G-M?sections=mwIQ',
        'https://en.wikipedia.org/api/rest_v1/page/html/List_of_colors:_N-Z?sections=mwIw',
    ]
    colors = ['Unknown']
    for link in links:
        r = requests.get(link)
        s = bs(r.text, 'html.parser')
        for row in s.find_all('tr')[1:]:
            if row.a:
                colors.append(row.a.string)

    path = join('..', 'testsite', 'rabbits_rest', 'data', 'colors.txt')
    with open(path, 'w', encoding='utf-8') as f:
        f.write('\n'.join(colors))


if __name__ == '__main__':
    main()
