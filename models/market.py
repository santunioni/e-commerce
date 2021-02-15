from models.structure.data import ClientCollection, EmployeeCollection
import pickle
import models.interface.screen as screen
import main
from os.path import join as os_path_join
from os.path import exists as os_path_exists

status = {
    'current_user': None,
    'user_type': None
}


CLIENTS_LIST_PATH = os_path_join(main.DIR, 'database', 'client', "clients.pickle")
EMPLOYEES_LIST_PATH = os_path_join(main.DIR, 'database', 'employee', "employees.pickle")


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

    while True:
        screen.initial_page()
