class UserRegisterView:

    def user_register_view(self):
        username = input('Insira o nome de usuário: ')
        telephone = input('Insira o telefone: ')
        address_state = input('Insira o estado: ')

        new_user_information = { "username": username,  "telephone": telephone, "user_city_state": address_state }
        
        return new_user_information




