import run.interface.screen as screen

from models.structure.product import Product
from models.structure.data import (ClientCollection,
                                   EmployeeCollection,
                                   Inventory)

from settings import (CLIENTS_LIST_PATH,
                      EMPLOYEES_LIST_PATH,
                      INVENTORY_PATH_CSV,
                      INVENTORY_PATH_PICKLE)

from os.path import exists as os_path_exists
from csv import DictReader
import pickle


def run():
    if not os_path_exists(CLIENTS_LIST_PATH):
        clients_list = ClientCollection()
        with open(CLIENTS_LIST_PATH, 'wb') as file:
            pickle.dump(clients_list, file)
        del clients_list

    if not os_path_exists(EMPLOYEES_LIST_PATH):
        employee_list = EmployeeCollection()
        with open(EMPLOYEES_LIST_PATH, 'wb') as file:
            pickle.dump(employee_list, file)
        del employee_list

    if (not os_path_exists(INVENTORY_PATH_PICKLE)) and os_path_exists(INVENTORY_PATH_CSV):
        inventory_dict = DictReader(INVENTORY_PATH_CSV)
        inventory = Inventory(inventory_dict)
        for product_csv in inventory_dict:
            product = Product(name=product_csv.get('name'), price=float(product_csv.get('price')))
            for _ in range(int(product_csv.get('amount'))):
                inventory += product
        with open(INVENTORY_PATH_PICKLE, 'wb') as file:
            pickle.dump(inventory, file)
        del employee_list

    while True:
        screen.initial_page()
