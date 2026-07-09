import requests
from bs4 import BeautifulSoup

url = "https://realpython.github.io/fake-jobs/"

response = requests.get(url)

soup = BeautifulSoup(response.text, "html.parser")

print(type(soup))
print(soup.title)