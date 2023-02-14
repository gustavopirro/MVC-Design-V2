from models.entities import Product


class Product:

    def __init__(self, product_name: str = None, product_flavor: str = None) -> None:
        self.product_name = product_name
        self.product_flavor = product_flavor