# LOCAL APP IMPORTS
# auxiliary functions
from system.aux_functions.clear import clear
# classes from the INTERFACE package
from system.interface.requests import InventoryManager
# imported only for MYPY type hinting
from typing import Tuple


class GeneralScreen:

    @staticmethod
    def login_screen() -> Tuple[str, str]:
        clear()
        email: str = input("Tell me you email: ")
        password: str = input("Tell me you password: ")
        return email, password

    @staticmethod
    def sign_in_screen() -> Tuple[str, str, str]:
        clear()
        full_name: str = input("Tell me you full name: ")
        email: str = input("Tell me you email: ")
        password: str = input("Tell me you password: ")
        return full_name, email, password

    @staticmethod
    def display_products() -> None:
        clear()
        products_dict: dict = InventoryManager().inventory().dict_form()
        print("="*75)
        print("Product ID \t\t product name \t\t price \t\t amount available")
        print("-"*75)
        print("")
        for product_id, product_dict in products_dict:
            print(f"{product_id} \t\t {product_dict['name']} \t\t "
                  f"{product_dict['price']} \t\t {product_dict['amount']}")
        print("="*75)
        input("Press enter to leave: ")
