from main.constructor.app_index_constructor import app_index_process 
from main.constructor.product_list_constructor import product_list_process
from main.constructor.user_register_constructor import user_register_process
from main.constructor.user_list_constructor import user_list_process
from main.constructor.product_register_constructor import product_register_process
from main.constructor.product_delete_constructor import product_delete_process

def start_app():
    while True:
        user_choice = app_index_process()

        if(user_choice == 1): user_register_process()
        elif(user_choice == 2): user_list_process()
        elif(user_choice == 3): product_list_process()
        elif(user_choice == 4): product_register_process()
        elif(user_choice == 5): product_delete_process()
        elif(user_choice == 6): exit()