import psycopg2
from abc import ABC, abstractmethod


class DataClient(ABC):
    @abstractmethod
    def _get_connection(self):
        pass

    @abstractmethod
    def create_pizza_table(self):
        pass

    @abstractmethod
    def insert(self, pizza_name, pizza_img, pizza_price, pizza_weight, pizza_description):
        pass

    def run_test(self):
        self.create_pizza_table()


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

    def create_pizza_table(self):
        with self._get_connection() as conn:
            cursor_object = conn.cursor()
            cursor_object.execute("""CREATE TABLE IF NOT EXISTS menu_pizza(id serial PRIMARY KEY, pizza_name text, pizza_img text, pizza_price text, pizza_weight text, pizza_description text)""")

    def insert(self, pizza_name, pizza_img, pizza_price, pizza_weight, pizza_description):
        with self._get_connection() as conn:
            cursor = conn.cursor()
            cursor.execute(f"INSERT INTO menu_pizza (pizza_name,pizza_img,pizza_price,pizza_weight,pizza_description) VALUES ('{pizza_name}', '{pizza_img}', '{pizza_price}', '{pizza_weight}', '{pizza_description}')")
            conn.commit()


base_data = PostgresClient()
base_data.run_test()
