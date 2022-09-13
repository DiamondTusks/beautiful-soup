from bs4 import BeautifulSoup
import requests

response = requests.get("https://news.ycombinator.com/news")
yc_web_page = response.text

soup = BeautifulSoup(yc_web_page, "html.parser")
# print(soup.title)
article_tag = soup.find(name="a", class_="titlelink")
article_text = article_tag.getText()
article_link = article_tag.get("href")
article_upvote = soup.find(name="span", class_="score").getText()

print(article_text)
print(article_link)
print(article_upvote)





# with open("website.html") as file:
#     contents = file.read()
#
# soup = BeautifulSoup(contents, "html.parser")
# print(soup.title)
# print(soup.title.name)
# print(soup.title.string)
# print(soup.prettify())

# print(soup.p)

# all_anchor_tags = soup.find_all(name="a")
# print(all_anchor_tags)

# for tag in all_anchor_tags:
    # print(tag.getText())
    # print(tag.get("href"))

# name = (soup.find(name="h1", id="name"))
# print(name.getText())

# h3_heading = soup.find_all("h3", class_="heading")
# print(h3_heading)

# name = soup.select_one(selector="#name")
# print(name)

# list_of_class_heading = soup.select(".heading")
# print(list_of_class_heading)
# for item in list_of_class_heading:
#     heading = item.getText()
#     print(heading)