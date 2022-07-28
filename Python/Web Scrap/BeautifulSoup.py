import requests
from bs4 import BeautifulSoup

# with open("simple.html", mode="r") as file:
#     soup = BeautifulSoup(file, "lxml")

# print(soup.prettify())
# some = (soup.find("head"))
# print(some.title.text)
# article = soup.find("div", class_="article")
# headline = article.h2.a.text
# paragraph = article.p.text
# print(headline)
# print(paragraph)

# second_article = soup.find_all("div", class_="article")
# second_headline = second_article[1].h2.a.text
# second_paragraph = second_article[1].p.text
# print(second_headline)
# print(second_paragraph)

source = requests.get(url="https://coreyms.com/").text
soup = BeautifulSoup(source, "lxml")

headers = soup.find_all("header", class_="entry-header")
paragraphs = soup.find_all("div", class_="entry-content")
links = soup.find_all("span", class_="embed-youtube")

# print(headers)
# print(len(paragraphs))
# print(len(links))

for title in range(len(headers)):
    print(headers[title].h2.a.text)
    print(paragraphs[title].p.text)
    print(links[title].iframe["src"])
    print()


