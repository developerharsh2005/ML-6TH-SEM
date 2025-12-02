import requests
from bs4 import BeautifulSoup

url = "https://books.toscrape.com/"
page = requests.get(url)
soup = BeautifulSoup(page.text, "html.parser")

books = soup.find_all("article", class_="product_pod")

data = []
for book in books:
    title = book.h3.a["title"]
    price = book.find("p", class_="price_color").text
    data.append([title, price])

import csv
with open("books.csv", "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerow(["Title", "Price"])
    writer.writerows(data)

print("Scraped books.csv created")
