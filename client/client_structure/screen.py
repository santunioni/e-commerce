# project imports
from system.aux_functions.clear import clear
from system.interface.general_screen import GeneralScreen
from client.client_structure.status import ClientStatus


class ClientScreen(GeneralScreen):

    @staticmethod
    def initial_page():
        clear()

        if ClientStatus.active_client():
            client = ClientStatus.active_client()
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
                       ClientScreen.display_products]
            while (number := int(input("""
            Select an option: 
        
            1 - Sign in
            2 - Fazer login
            3 - Listar produtos
            """))) not in [1, 2, 3]:
                pass

        options[int(number) - 1]()

    @staticmethod
    def display_kart():
        clear()
        # TODO: re-implement the display_kart method
        # if client.client_structure.session.status['current_user']:
        #     kart = client.client_structure.session.status['current_user'].kart
        #     print("="*75)
        #     print("Product ID \t\t product name \t\t price \t\t amount")
        #     print("-"*75)
        #     print("")
        #     for product in kart:
        #         amount, obj = product['amount'], product['object']
        #         print(f"{obj.identifier} \t\t {obj.name} \t\t {obj.price} \t\t {amount}")
        #     print("="*75)
        input("Press enter to leave: ")
