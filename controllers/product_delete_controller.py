from models.repositories.products_repository import products_repository

class ProductDeleteController:

    def delete(self, product_name):
        return products_repository.delete(product_name)
