from models.entities.Product import Product
from models.repositories.products_repository import products_repository
from typing import Dict

class ProductController:

    def register(self, new_product_data):
        try:
            new_product = self.__create_product_entity(new_product_data)
            self.__save(new_product)
            return self.__format_response(new_product_data)
        except Exception as e:
            print(e)
            return { "success": False, "error": "An error ocurred" }

    def __create_product_entity(self, new_product_data: Dict):
        product_name = new_product_data["product_name"]
        product_flavor = new_product_data["product_flavor"]

        product = Product(product_name, product_flavor)
        return product
    
    def __save(self, new_product_data: Dict):
        products_repository.insert(new_product_data)
    
    def __format_response(self, new_product_data: Dict) -> Dict:
        return {
            "success": True,
            "data": {
                "product_name": new_product_data["product_name"],
                "product_flavor": new_product_data["product_flavor"]
            }
        }