from bs4 import BeautifulSoup # type: ignore
import requests # type: ignore

url = 'https://www.daraz.com.np/'

res = requests.get(url)
print(res.text)

soup = BeautifulSoup(res.text, features='html.parser')
# soup = BeautifulSoup(open("index.html"), features='html.parser')

print(soup)

# followed the docs
soup = BeautifulSoup('<b class="boldest">Extremely bold</b>', features='html.parser')
tag = soup.b
print(type(tag))
print(tag.text)
print('name',tag.name)
print('attribute',tag.attrs)

tag['class'] = 'verybold'
tag['id'] = 1
print(tag)


css_soup = BeautifulSoup('<p class="body strikeout"></p>', features='html.parser')
print(css_soup.p['class'])