import requests
from bs4 import BeautifulSoup

url = 'https://dominos.by/pizza'
response = requests.get(url)
soup = BeautifulSoup(response.text, 'lxml')
items = soup.find_all('div', class_='product-card product-card--vertical')
for pizza in items:
    pizza_name = pizza.find('div', class_='product-card__title').text
    pizza_img = pizza.find('img', class_='media-image__element product-card-media__element').get('src')
    pizza_price = pizza.find('p', class_='product-card__modification-info-price').text
    pizza_weight = pizza.find('p', class_='product-card__modification-info-weight').text
    pizza_description = pizza.find('div', class_='product-card__description').text
    print(f"{pizza_name} : {pizza_img} : {pizza_price}|{pizza_weight} : {pizza_description}")
