import re

import requests
from bs4 import BeautifulSoup


def parse(start_url):
    start_url = start_url.replace('\n', '').replace('https://', '').replace('http://', '')
    url = re.search('[a-zA-Z0-9\_]*.t.me', start_url)

    if not url:
        url = re.search('t.me.[a-zA-Z0-9\_]*', start_url)

    if url:
        url = url.group(0).strip()
        url = 'https://' + url
        response = requests.get(url)
        soup = BeautifulSoup(response.content, 'html.parser')

        title = soup.find(
            'div',
            class_='tgme_page_title')
        if title:
            return url
    return None


def main():
    with open(f'links.txt', 'r', encoding="utf8") as file:
        links = file.readlines()
    counter, valid = 0, 0
    for link in links:
        counter += 1
        res = parse(link)
        if res:
            with open(f'result.txt', 'a') as result:
                valid += 1
                result.write(f'{res}\n')
                print(f'{valid}/{counter}/{len(links)} | {res}')


if __name__ == '__main__':
    main()
