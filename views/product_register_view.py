class ProductRegisterView:

    def product_register_view(self):
        
        product_name = input('Insira o nome do produto: ')
        product_flavor = input('Insira o sabor do produto: ')

        return { 'product_name': product_name, 'product_flavor': product_flavor}