class ProductListView:
    def product_list_view(self, product_list):
        print('Lista de Produtos: \n')
        for product in product_list:
            print(f"Produto: { product['product_name'] }, Sabor: { product['product_flavor'] }")
