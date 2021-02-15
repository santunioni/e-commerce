from system.aux_functions.clear import clear


class GeneralScreen:

    @staticmethod
    def login_screen() -> [str, str]:
        clear()
        email = input("Tell me you email: ")
        password = input("Tell me you password: ")
        return email, password

    @staticmethod
    def sign_in_screen():
        clear()
        full_name = input("Tell me you full name: ")
        email = input("Tell me you email: ")
        password = input("Tell me you password: ")
        return full_name, email, password

    @staticmethod
    def display_products():
        clear()
        # TODO: implement the display_products method
        # inventory = request.inventory()
        # print("="*75)
        # print("Product ID \t\t product name \t\t price \t\t amount available")
        # print("-"*75)
        # print("")
        # for product in inventory:
        #     amount, obj = product['amount'], product['object']
        #     print(f"{obj.identifier} \t\t {obj.name} \t\t {obj.price} \t\t {amount}")
        # print("="*75)
        # if client.client_structure.session.status['current_user']:
        #     pass
        input("Press enter to leave: ")
