import requests

response = requests.get("https://books.toscrape.com")
response_text = response.text
responce_parse = response_text.split('title="')

book_titles = []

for elem in responce_parse:
    if elem.startswith("A") or elem.startswith("B") or elem.startswith("T") or elem.startswith("S"):
        for elem2 in elem.split('"'):
            book_titles.append(elem2)
            break

for title in book_titles:
    print(title)