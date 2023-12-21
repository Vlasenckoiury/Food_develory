import requests
from bs4 import BeautifulSoup
# import pandas
import base_data


class Parser:
    links_to_parse = [
        'https://dominos.by/pizza'
    ]
    data_client_imp = base_data.PostgresClient()

    @staticmethod
    def get_pizza_by_link(link):
        response = requests.get(link)
        response.encoding = 'utf8'
        pizza_data = response.text

        product_items = []
        to_parse = BeautifulSoup(pizza_data, 'html.parser')
        for elem in to_parse.find_all('div', class_='product-card product-card--vertical'):
            try:
                name = elem.find('div', class_='product-card__title').text
                img = elem.find('img', class_='media-image__element product-card-media__element').get('src')
                price = elem.find('p', class_='product-card__modification-info-price').text
                weight = elem.find('p', class_='product-card__modification-info-weight').text
                description = elem.find('div', class_='product-card__description').text
                product_items.append((name, img, price, weight, description.replace("'", "")))
            except:
                print(f'Noy info{elem.text}')
        return product_items

    def save_to_postgres(self, product_items):
        self.data_client_imp.create_product_table()
        for item in product_items:
            self. data_client_imp.insert(item[0], item[1], item[2], item[3], item[4])

    def run(self):
        product_items = []
        for link in Parser.links_to_parse:
            product_items.extend(self.get_pizza_by_link(link))
        self.save_to_postgres(product_items)


Parser().run()
