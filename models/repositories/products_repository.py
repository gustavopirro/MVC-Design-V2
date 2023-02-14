from models.entities import Product


class __ProductsRepository:

    def __init__(self) -> None:
        self.__product_table = []

    def insert(self, product_dict: Product):
        new_product = {'product_name': product_dict.product_name, 'product_flavor': product_dict.product_flavor}
        self.__product_table.append(new_product)

        return new_product

    def get_all(self) -> object:
        return self.__product_table

    def delete(self, product_name):
        element_index = self.__find_element_index(product_name)
        
        if(element_index == -1):
            return {'success': False, 'error': 'Product not found.'}

        self.__product_table.pop(element_index)
        return {'success': True}

    def __find_element_index(self, element_name:str) -> int:
        for i, product in enumerate(self.__product_table):
            if product.get('product_name') == element_name:
                return i
        return -1
    
products_repository = __ProductsRepository()