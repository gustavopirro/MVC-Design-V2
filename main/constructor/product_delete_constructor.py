from views.product_delete_view import ProductDeleteView
from controllers.product_delete_controller import ProductDeleteController

def product_delete_process():
    product_delete_view = ProductDeleteView()
    product_delete_controller = ProductDeleteController()

    product_name = product_delete_view.delete_product_view()
    response = product_delete_controller.delete(product_name)

    if response['success']:
        return print('Produto deletado!')
    
    print('Ocorreu um erro ao deletar o produto...')
