# python libraries imports
from os.path import join as os_path_join
from os import pardir as parent_directory

ROOT_DIR = parent_directory

CLIENTS_FILES_PATH = os_path_join(ROOT_DIR, 'database', 'clients')
CLIENTS_EMAILS_LIST_PATH = os_path_join(ROOT_DIR, 'database', 'server', 'clients_emails.csv')

EMPLOYEES_FILES_PATH = os_path_join(ROOT_DIR, 'database', 'employees')
EMPLOYEES_EMAILS_LIST_PATH = os_path_join(ROOT_DIR, 'database', 'server', "employees_emails.csv")

INVENTORY_PATH_CSV = os_path_join(ROOT_DIR, 'database', 'server', "inventory.csv")
INVENTORY_PATH_PICKLE = os_path_join(ROOT_DIR, 'database', 'server', "inventory.pickle")

del os_path_join, parent_directory
