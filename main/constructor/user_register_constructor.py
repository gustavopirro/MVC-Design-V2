from controllers.user_register_controller import UserRegisterController
from views.user_register_view import UserRegisterView

def user_register_process():
    user_controller = UserRegisterController()
    user_view = UserRegisterView()

    new_user_data = user_view.user_register_view()
    response = user_controller.register(new_user_data)
    
    if response['success']:
        return print('Usuário inserido com sucesso!')

    print('Ocorreu um erro ao criar um novo usuário.')
