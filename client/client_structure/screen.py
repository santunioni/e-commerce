# python libraries imports
from sys import exit
# imported only for MYPY type hinting
from typing import Union
from system.market_structure.client import Client
# LOCAL APP IMPORTS
from system.aux_functions.clear import clear
from system.interface.general_screen import GeneralScreen
from client.client_structure.status import ClientStatus


class ClientScreen(GeneralScreen):

    @staticmethod
    def initial_page() -> None:
        clear()

        if ClientStatus.active_client():
            client: Client = ClientStatus.active_client()
            options = [ClientScreen.display_products,
                       ClientScreen.display_kart,
                       client.close_order,
                       ClientStatus.logout]
            while (number := int(input("""
            Select an option: 
        
            1 - Listar produtos
            2 - Visualizar carrinho
            3 - Fechar pedido
            4 - Fazer logout
            """))) not in [1, 2, 3, 4]:
                pass
            del client

        else:
            options = [lambda: ClientStatus.sign_in(*GeneralScreen.sign_in_screen()),
                       lambda: ClientStatus.login(*GeneralScreen.login_screen()),
                       ClientScreen.display_products,
                       exit]
            while (number := int(input("""
            Select an option: 
        
            1 - Sign in
            2 - Fazer login
            3 - Listar produtos
            4 - Sair do programa
            """))) not in [1, 2, 3, 4]:
                clear()

        options[int(number) - 1]()

    @staticmethod
    def display_kart() -> None:
        clear()

        if ClientStatus.active_client():
            client: Client = ClientStatus.active_client()
            products_dict: dict = client.kart.dict_form()
            print("="*75)
            print("Product ID \t\t Product Name \t\t Price \t\t Amount \t\t Cost")
            print("-"*75)
            print("")
            for product_id, product_dict in products_dict:
                print(f"{product_id} \t\t {product_dict['name']} \t\t "
                      f"{product_dict['price']} \t\t {product_dict['amount']}"
                      f"{product_dict['amount']*product_dict['price']}")
            print("="*75)
            input("Press enter to leave: ")
