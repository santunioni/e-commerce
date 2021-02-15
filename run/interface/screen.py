import run.interface.credentials
import run.interface.request as request
import run.market as market
import settings
from utils.utility import clear


def initial_page():
    clear()
    if not settings.status['user_type']:
        while (user_label := input('Are you a client or a employee here (c/e)? ').lower()[0]) not in ['c', 'e']:
            continue
        settings.status['user_type'] = 'client' if user_label == 'c' else 'employee'
    elif settings.status['user_type'] == 'client':
        ClientScreen.initial_page()
    elif settings.status['user_type'] == 'employee':
        EmployeeScreen.initial_page()


class GeneralScreen:

    @staticmethod
    def login():
        clear()
        email = input("Tell me you email: ")
        password = input("Tell me you password: ")
        run.interface.credentials.login(email=email, password=password)

    @staticmethod
    def sign_in():
        clear()
        full_name = input("Tell me you full namee: ")
        email = input("Tell me you email: ")
        password = input("Tell me you password: ")
        run.interface.credentials.sign_in(full_name=full_name, email=email, password=password)


class ClientScreen(GeneralScreen):

    @staticmethod
    def initial_page():
        clear()
        client = settings.status['current_user']
        if client:
            options = [ClientScreen.display_products,
                       ClientScreen.display_kart,
                       request.close_order,
                       run.interface.credentials.logout]
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
        if settings.status['current_user']:
            kart = settings.status['current_user'].kart
            print("="*75)
            print("Product ID \t\t product name \t\t price \t\t amount")
            print("-"*75)
            print("")
            for product in kart:
                amount, obj = product['amount'], product['object']
                print(f"{obj.identifier} \t\t {obj.name} \t\t {obj.price} \t\t {amount}")
            print("="*75)
            input("Press enter to leave: ")

    @staticmethod
    def display_products():
        clear()
        inventory = request.inventory()
        print("="*75)
        print("Product ID \t\t product name \t\t price \t\t amount available")
        print("-"*75)
        print("")
        for product in inventory:
            amount, obj = product['amount'], product['object']
            print(f"{obj.identifier} \t\t {obj.name} \t\t {obj.price} \t\t {amount}")
        print("="*75)
        if settings.status['current_user']:
            pass
        input("Press enter to leave: ")


class EmployeeScreen(GeneralScreen):

    @staticmethod
    def initial_page(logged=False):
        # TODO: implement the initial page for employees
        pass
