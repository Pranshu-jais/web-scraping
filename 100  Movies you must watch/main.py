import requests
from bs4 import BeautifulSoup


response = requests.get("https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/")
web_page_text = response.text
soup = BeautifulSoup(web_page_text, "html.parser")

names =[name.getText() for name in soup.find_all(name="h3",class_ ="title")]
movies = names[::-1]
print(movies)

with open("movies.txt",mode="w",encoding="utf8") as file:
    for movie in movies:
      file.write(f"{movie}\n")





