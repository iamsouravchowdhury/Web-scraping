import requests
from bs4 import BeautifulSoup
url = "https://codewithharry.com"

r= requests.get(url)
Htmlcontent= r.content

soup= BeautifulSoup(Htmlcontent, 'html.parser')
# print(soup.prettify)

#commonly used type of object
#1. Tag
# 2. beautiful soup object
# 3.  Navigable string
# 4. comment

title= soup.title
# print(type(title.string))
# print(type(soup))
# print(type(title))

#get all para

para= soup.find_all('p')
# print(para)

#get all a tag
anchors = soup.find_all('a')
# print(anchors)

print(soup.find('p'))  #get first element of html
print(soup.find('p')['class']) #get class

print(soup.find_all('p' , class_='lead'))

print(soup.find('p').get_text())

print(soup.get_text())
all_links= set()

for link in anchors:
    if link != '#':
        link="https://codewithharry.com"+link.get('href')
        all_links.add(link)
        print(link)


