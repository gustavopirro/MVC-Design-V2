from controllers.user_list_controller import UserListController
from views.user_list_view import UserListView

def user_list_process():
    user_list_controller = UserListController()
    user_list_view = UserListView()

    address_filter = user_list_view.user_list_view()
    response = user_list_controller.get_users(address_filter)

    if response['success']:
        for user in response['data']['users']:
            print(f'Nome: {user["username"]}')
            print(f'Telefone: {user["telephone"]}')
            print(f'Estado: {user["user_city_state"]}')
        return

    print('Ocorreu um erro!')
