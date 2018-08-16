import re
import requests
from bs4 import BeautifulSoup


def ngrams(input, n):
    input = re.sub('\n+', " ", input)
    input = re.sub(' +', " ", input)
    input = bytes(input, "UTF-8")
    input = input.decode("ascii", "ignore")
    input = input.split(' ')
    output = []
    for i in range(len(input) - n + 1):
        output.append(input[i:i + n])
    return output


html = requests.get("https://en.wikipedia.org/wiki/Python_(programming_language)").text
soup = BeautifulSoup(html, "lxml")
content = soup.find('div', {'id': 'mw-content-text'}).getText()
print(ngrams(content, 2))
