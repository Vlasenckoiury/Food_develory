import psycopg2
from abc import ABC, abstractmethod


class DataClient(ABC):
    @abstractmethod
    def _get_connection(self):
        pass

    @abstractmethod
    def create_product_table(self):
        pass

    @abstractmethod
    def insert(self, name, img, price, weight, description):
        pass

    def run_test(self):
        self.create_product_table()


class PostgresClient(DataClient):
    USER = "postgres"
    PASSWORD = "postgres"
    HOST = "localhost"
    PORT = "5432"

    def _get_connection(self):
        return psycopg2.connect(
                user=self.USER,
                password=self.PASSWORD,
                host=self.HOST,
                port=self.PORT
        )

    def create_product_table(self):
        with self._get_connection() as conn:
            cursor_object = conn.cursor()
            cursor_object.execute("""CREATE TABLE IF NOT EXISTS app_food_product(id serial PRIMARY KEY, name text, img text, price text, weight text, description text)""")

    def insert(self, name, img, price, weight, description):
        with self._get_connection() as conn:
            cursor = conn.cursor()
            cursor.execute(f"INSERT INTO app_food_product (name,img,price,weight,description) VALUES ('{name}', '{img}', '{price}', '{weight}', '{description}')")
            conn.commit()


base_data = PostgresClient()
base_data.run_test()
