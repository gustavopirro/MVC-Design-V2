from controllers.product_register_controller import ProductController
from views.product_register_view import ProductRegisterView

def product_register_process():
    product_controller = ProductController()
    product_view = ProductRegisterView()

    new_product_data = product_view.product_register_view()
    response = product_controller.register(new_product_data)

    if response['success']:
        return print(response['data'])
    print(response)


