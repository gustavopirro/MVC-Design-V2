from controllers.product_list_controller import ProductController
from views.product_list_view import ProductListView

def product_list_process():
    product_list_view = ProductListView()
    product_list_controller = ProductController()

    product_list = product_list_controller.get_all()
    product_list_view.product_list_view(product_list)