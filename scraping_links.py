import requests
from bs4 import BeautifulSoup
url = "http://www.jaduniv.edu.in/"

r= requests.get(url)
Htmlcontent= r.content

soup= BeautifulSoup(Htmlcontent, 'html.parser')
# print(soup.prettify)

anchors = soup.find_all('a')
all_links= set()

for link in anchors:
    if link != '#':
        link='http://www.jaduniv.edu.in/'+link.get('href')
        all_links.add(link)
        print(link)

    

