from bs4 import BeautifulSoup
import requests

# with open("website.html") as file:
#     contents = file.read()
#
# soup = BeautifulSoup(contents, "lxml")
# # print(soup.title)
# # print(soup.title.string)
#
# # print(soup.prettify())
#
# all_anchor_tags = soup.find_all(name="a")
# # print(all_anchor_tags)
#
# # for tag in all_anchor_tags:
# #     print(tag.getText())
# #     print(tag.get("href"))
#
# heading = soup.find(name="h1", id="name")
# # print(heading)
#
# section_heading = soup.find(name="h3", class_="heading")
# # print(section_heading.getText())
#
# company_url = soup.select_one(selector="p a")
# print(company_url)



# response = requests.get("https://news.ycombinator.com/news")
# yc_web_page = response.text
#
# soup = BeautifulSoup(yc_web_page, "lxml")
# # print(soup.title)
#
# # Get the titles
# title = soup.find(name="span", class_="titleline")
# article_text = title
# print(article_text)
#
# anchor_tags = soup.find(name="span", class_="score")
# print(anchor_tags)

URL = "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/"

response = requests.get(URL)
website_html = response.text

soup = BeautifulSoup(website_html, "html.parser")

all_movies = soup.find_all(name="h3", class_="title")
movie_titles = [movie.getText() for movie in all_movies]
movies = movie_titles[::-1]
print(movies)

with open("movies.txt", mode="w") as file:
    for movie in movies:
        file.write(f"{movie}\n")
