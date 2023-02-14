from models.repositories.products_repository import products_repository


class ProductController:

    def get_all(self):
        return products_repository.get_all()