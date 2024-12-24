import requests
from bs4 import BeautifulSoup

URL = "https://www.empireonline.com/movies/features/best-movies-2/"


response = requests.get(URL)
website_html = response.text

soup = BeautifulSoup(website_html, "html.parser")

moveis = soup.find_all(name="h2")
#print(moveis)

movie_titles = [movie.find("strong").get_text() for movie in moveis if movie.find("strong")]
print(movie_titles)

all_movies = movie_titles[::-1]

with open("movies.txt", mode="w") as file:
     for movie in all_movies:
         file.write(f"{movie}\n")