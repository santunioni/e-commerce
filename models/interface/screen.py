import models.interface.request as request
import models.market as market
from utils.utility import clear


def initial_page():
    clear()
    if not market.status['user_type']:
        while (user_label := input('Are you a client or a employee here (c/e)? ').lower()[0]) not in ['c', 'e']:
            continue
        market.status['user_type'] = 'client' if user_label == 'c' else 'employee'
    elif market.status['user_type'] == 'client':
        ClientScreen.initial_page()
    elif market.status['user_type'] == 'employee':
        EmployeeScreen.initial_page()


class GeneralScreen:

    @staticmethod
    def login():
        clear()
        email = input("Tell me you email: ")
        password = input("Tell me you password: ")
        request.login(email=email, password=password)

    @staticmethod
    def sign_in():
        clear()
        full_name = input("Tell me you full namee: ")
        email = input("Tell me you email: ")
        password = input("Tell me you password: ")
        request.sign_in(full_name=full_name, email=email, password=password)


class ClientScreen(GeneralScreen):

    @staticmethod
    def initial_page():
        clear()
        client = market.status['current_user']
        if client:
            options = [ClientScreen.display_products,
                       ClientScreen.display_kart,
                       request.close_order,
                       request.logout]
            while (number := int(input("""
            Select an option: 
        
            1 - Listar produtos
            2 - Visualizar carrinho
            3 - Fechar pedido
            4 - Fazer logout
            """))) not in [1, 2, 3, 4]:
                pass

        else:
            options = [ClientScreen.sign_in,
                       ClientScreen.login,
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
        if market.status['current_user']:
            kart = market.status['current_user'].kart
            print("="*50)
            print("Product ID \t\t product name \t\t price \t\t amount")
            print("-"*50)
            print("")
            for product in kart:
                amount, obj = product['amount'], product['object']
                print(f"{obj.identifier} \t\t {obj.name} \t\t {obj.price} \t\t {amount}")
            print("="*50)
            # while (command := input("Digite o número do produto que deseja adicionar ao carrinho (quit para sair): ")) \
            #         != 'quit':
            #     if command in range(1, len(kart) + 1):
            #         market.status['current_user'].kart.add(kart[int(command)])
            input("Press enter to leave: ")

    @staticmethod
    def display_products():
        clear()
        inventory = request.inventory()
        print(inventory)
        if market.status['current_user']:
            while (command := input("Digite o número do produto que deseja adicionar ao carrinho (quit para sair): ")) \
                    != 'quit':
                if command in range(1, len(inventory) + 1):
                    market.status['current_user'].kart.add(inventory[int(command)])
        else:
            input("Press enter to leave: ")


class EmployeeScreen(GeneralScreen):

    @staticmethod
    def initial_page(logged=False):
        # TODO: implement the initial page for employees
        pass
