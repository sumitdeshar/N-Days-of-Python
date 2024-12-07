html_doc = """
<html><head><title>The Dormouse's story</title></head>

<p class="title"><b>The Dormouse's story</b></p>

<p class="story">Once upon a time there were three little sisters; and their names were
<a href="http://example.com/elsie" class="sister" id="link1">Elsie</a>,
<a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> and
<a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>;
and they lived at the bottom of a well.</p>

<p class="story">...</p>
"""

from bs4 import BeautifulSoup # type: ignore
soup = BeautifulSoup(html_doc, features='html.parser')
# print(soup)


# print('head', soup.head) #head <head><title>The Dormouse's story</title></head>
# print('title',soup.title) #title <title>The Dormouse's story</title>
# print('b',soup.p.b) #actual implemtation //   made easy #b <b>The Dormouse's story</b>
# print('b',soup.b) #b <b>The Dormouse's story</b>

# print('a',soup.a) #a <a class="sister" href="http://example.com/elsie" id="link1">Elsie</a>
# print('all a tags:', soup.find_all('a'))
# #all a tags: [<a class="sister" href="http://example.com/elsie" id="link1">Elsie</a>, <a class="sister" href="http://example.com/lacie" id="link2">Lacie</a>, <a class="sister" href="http://example.com/tillie" id="link3">Tillie</a>]

# print(soup.head.contents) #[<title>The Dormouse's story</title>]
# print(soup.head.contents[0]) #<title>The Dormouse's story</title>

# for child in soup.head.children: #.childern is a genrator
#     print(child) #<title>The Dormouse's story</title>
    
# for child in soup.head.descendants: #.children gives only its direct children but .descendants will give all direct and grandchildren and continued
#     print(child) #The Dormouse's story. here the string is grand child/child of title so it will give direct data as well.

# print(soup.head.string) #The Dormouse's story. gives string similar to .text
# print(soup.string) #! but returns None if the tag contains multiple children tags

# print(soup.strings) #returns all available white space and unimportant data

# for data in soup.stripped_strings:
#     print(data)
# # The Dormouse's story
# # The Dormouse's story
# # Once upon a time there were three little sisters; and their names were
# # Elsie
# # ,
# # Lacie
# # and
# # Tillie
# # ;
# # and they lived at the bottom of a well.
# # ...

title_tag = soup.title
# <title>The Dormouse's story</title>
title_tag.parent
# <head><title>The Dormouse's story</title></head>

sibling_soup = BeautifulSoup("<a><b>text1</b><c>text2</c></a>")
print(sibling_soup.prettify())
# <a>
#  <b>
#   text1
#  </b>
#  <c>
#   text2
#  </c>
# </a>


sibling_soup.b.next_sibling
# <c>text2</c>

sibling_soup.c.previous_sibling
# <b>text1</b>


# for <a href="http://example.com/elsie" class="sister" id="link1">Elsie</a>
# <a href="http://example.com/lacie" class="sister" id="link2">Lacie</a>
# <a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>

link = soup.a
link
# <a class="sister" href="http://example.com/elsie" id="link1">Elsie</a>

link.next_sibling
# -->',\n'
# The second <a> tag is actually the .next_sibling of the comma:

link.next_sibling.next_sibling
# <a class="sister" href="http://example.com/lacie" id="link2">Lacie</a>


for sibling in soup.a.next_siblings:
    print(repr(sibling))
# u',\n'
# <a class="sister" href="http://example.com/lacie" id="link2">Lacie</a>
# u' and\n'
# <a class="sister" href="http://example.com/tillie" id="link3">Tillie</a>
# u'; and they lived at the bottom of a well.'
# None

for sibling in soup.find(id="link3").previous_siblings:
    print(repr(sibling))
# ' and\n'
# <a class="sister" href="http://example.com/lacie" id="link2">Lacie</a>
# u',\n'
# <a class="sister" href="http://example.com/elsie" id="link1">Elsie</a>
# u'Once upon a time there were three little sisters; and their names were\n'
# None



last_a_tag = soup.find("a", id="link3")
last_a_tag
# <a class="sister" href="http://example.com/tillie" id="link3">Tillie</a>

last_a_tag.next_sibling
# '; and they lived at the bottom of a well.'
last_a_tag.next_element
# u'Tillie'


last_a_tag.previous_element
# u' and\n'
last_a_tag.previous_element.next_element
# <a class="sister" href="http://example.com/tillie" id="link3">Tillie</a>

for element in last_a_tag.next_elements:
    print(repr(element))
# u'Tillie'
# u';\nand they lived at the bottom of a well.'
# u'\n\n'
# <p class="story">...</p>
# u'...'
# u'\n'
# None

