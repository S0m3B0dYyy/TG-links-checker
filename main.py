import requests
from bs4 import BeautifulSoup


def parse(url):
    if not url:
        pass
    else:
        url = url.replace('\n', '')
        url = 'https://' + url if not (
                url.startswith('https://') or url.startswith('http://')) else url
        response = requests.get(url)
        soup = BeautifulSoup(response.content, 'html.parser')

        title = soup.find(
            'div',
            class_='tgme_page_title').get_text(strip=True)
        if title:
            return url
    return None


def main():
    with open(f'links.txt', 'r') as file:
        links = file.readlines()
    counter, valid = 0, 0
    for link in links:
        counter += 1
        res = parse(link)
        if res:
            with open(f'result.txt', 'a') as result:
                valid += 1
                result.write(link)
                print(f'{valid}/{counter}/{len(links)} | {res}')


if __name__ == '__main__':
    main()
