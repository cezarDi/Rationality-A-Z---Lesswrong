from bs4 import BeautifulSoup
import requests

# pip install lxml, bs4
# URL = "https://www.lesswrong.com/rationality"

windows = [
    'https://www.lesswrong.com/s/5g5TkQTe9rmPS5vvM',
    'https://www.lesswrong.com/s/7gRSERQZbqTuLX5re',
    'https://www.lesswrong.com/s/zpCiuR4T343j9WkcK',
    'https://www.lesswrong.com/s/5uZQHpecjn7955faL',
    'https://www.lesswrong.com/s/FrqfoG3LJeCZs96Ym',
    'https://www.lesswrong.com/s/3ELrPerFTSo75WnrH',
    'https://www.lesswrong.com/s/GSqFqc646rsRd2oyz',
    'https://www.lesswrong.com/s/qqFS6Kw5fmPyzkLby',
    'https://www.lesswrong.com/s/pmHZDpak4NeRLLLCw',
    'https://www.lesswrong.com/s/M3TJ2fTCzoQq66NBJ',
    'https://www.lesswrong.com/s/5bZZZJ5psXrrD5BGb',
    'https://www.lesswrong.com/s/MH2b8NfWv22dBtrs8',
    'https://www.lesswrong.com/s/3HyeNiEpvbQQaqeoH',
    'https://www.lesswrong.com/s/SGB7Y5WERh4skwtnb',
    'https://www.lesswrong.com/s/oFePMp9rKftEeZDDr',
    'https://www.lesswrong.com/s/p3TndjYbdYaiWwm9x',
    'https://www.lesswrong.com/s/6BFkmEgre7uwhDxDR',
    'https://www.lesswrong.com/s/FqgKAHZAiZn9JAjDo',
    'https://www.lesswrong.com/s/Kqs6GR7F5xziuSyGZ',
    'https://www.lesswrong.com/s/fxynfGCSHpY4FmBZy',
    'https://www.lesswrong.com/s/fqh9TLuoquxpducDb',
    'https://www.lesswrong.com/s/9bvAELWc8y2gYjRav',
    'https://www.lesswrong.com/s/waF2Pomid7YHjfEDt',
    'https://www.lesswrong.com/s/SXurf2mWFw8LX2mkG',
    'https://www.lesswrong.com/s/3szfzHZr7EYGSWt92',
    'https://www.lesswrong.com/s/pvim9PZJ6qHRTMqD3'
]

all_articles = []
article_name = []


def window_links():
    url = "https://www.lesswrong.com/rationality"
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'lxml')
    links = soup.find_all('div', class_="LinkCard-background")
    for s in links:
        link = s.find('a').get('href')
        # print(link)

        windows.append(link)


def in_window_links(url):
    # url = URL + 'A'
    # url = URL
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'lxml')

    inp = soup.find_all('span', class_='PostsTitle-root')
    # items = soup.find_all('div', {'class': ['item', 'item even']})
    # print(len(inp))
    del article_name[:]
    for t in inp:
        # print(t)
        links = t.find('a').get('href')
        # print(t.text, links)
        # global all_articles
        # global article_name
        all_articles.append(links)
        # article_name.append(t.text)
        # return links


# works without this func
def parse_title_name(url):
    # url = "https://www.lesswrong.com/rationality"
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'lxml')
    # links = soup.find_all('div', class_="PostsPagePostHeader-headerLeft")[0].find('h1')
    # name = soup.find_all('h1', class_="Typography-root Typography-display3 PostsPageTitle-root")[0]
    name = soup.find('h1', {'class': 'Typography-root Typography-display3 PostsPageTitle-root'}).text
    return name


def main():
    # window_links()
    for i in windows:
        window = "https://www.lesswrong.com"
        in_window_links(i)

        for article in all_articles:
            articlelink = window + article

            print(f"'{articlelink}")
            article_name.append(parse_title_name(articlelink))
            # all_articles.append(articlelink)
            # article_name.append(art_name)
            # return articlelink
        del all_articles[:]


window_links()
main()
# Firstly, you need run window_links, and save all links in file or in the array
# Then, you can run main
