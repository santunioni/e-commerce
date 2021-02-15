from os.path import join as os_path_join
from os import getcwd

DIR = getcwd()

CLIENTS_LIST_PATH = os_path_join(DIR, '../database', 'client', "clients.pickle")
EMPLOYEES_LIST_PATH = os_path_join(DIR, '../database', 'employee', "employees.pickle")
INVENTORY_PATH_CSV = os_path_join(DIR, '../database', 'inventory', "inventory.csv")
INVENTORY_PATH_PICKLE = os_path_join(DIR, '../database', 'inventory', "inventory.pickle")

del os_path_join, getcwd
