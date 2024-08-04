import requests
from bs4 import BeautifulSoup
url = "https://codewithharry.com"
l= "https://codewithharry.com"

# Step:1

r = requests.get(url)
htmlContent = r.content

#print(htmlContent)

# Step:2

soup = BeautifulSoup(htmlContent, 'html.parser')

# Step:3
title =  soup.title
#print(title)

paras = soup.find_all('title')
#print (paras)


anchors = soup.find_all('a')

text = soup.get_text()
#print (text)


allLinks = set()

for link in anchors:
    if(link.get('href') != '#'):
        linkText = l+ link.get('href')
        allLinks.add(link)
        print(linkText)