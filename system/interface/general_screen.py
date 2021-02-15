# LOCAL APP IMPORTS
# auxiliary functions
from system.aux_functions.clear import clear
# classes from the INTERFACE package
from system.interface.requests import InventoryManager


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
        inventory_dict = InventoryManager().inventory().dict_form()
        print("="*75)
        print("Product ID \t\t product name \t\t price \t\t amount available")
        print("-"*75)
        print("")
        for product_id, product_dict in inventory_dict:
            print(f"{product_id} \t\t {product_dict['name']} \t\t "
                  f"{product_dict['price']} \t\t {product_dict['amount']}")
        print("="*75)
        input("Press enter to leave: ")
