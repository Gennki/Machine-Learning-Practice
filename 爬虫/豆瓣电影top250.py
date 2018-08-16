import requests
from bs4 import BeautifulSoup

baseUrl = 'https://movie.douban.com/top250'
movie_name_list = []


def parse_html(url):
    data = requests.get(url).text
    soup = BeautifulSoup(data, "lxml")
    movie_li_list = soup.find('ol', {'class': 'grid_view'})
    for movie_li in movie_li_list.find_all('li'):
        detail = movie_li.find('div', {'class': 'hd'})
        movie_name = detail.find('span', {'class': 'title'})
        movie_name_list.append(movie_name.get_text())

    next_page = soup.find('span', {'class': 'next'}).find('a')
    if next_page:
        parse_html(baseUrl + next_page['href'])
    else:
        print(movie_name_list)


if __name__ == '__main__':
    parse_html(baseUrl)
    with open('a.txt', 'w', encoding='utf-8') as file:
        for i in range(len(movie_name_list)):
            file.write(str(i + 1) + movie_name_list[i] + "\n")
