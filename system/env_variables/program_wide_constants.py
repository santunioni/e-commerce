# PYTHON LIBRARIES IMPORTS
from os.path import join as os_path_join
from os.path import abspath as os_path_abspath
from os.path import dirname, realpath
from os import pardir

ENV_VARIABLES_DIR = dirname(realpath(__file__))
ROOT_DIR = os_path_abspath(os_path_join(ENV_VARIABLES_DIR, pardir, pardir))

CLIENTS_FILES_PATH = os_path_join(ROOT_DIR, 'database', 'clients')
CLIENTS_EMAILS_LIST_PATH = os_path_join(ROOT_DIR, 'database', 'server', 'clients_emails.csv')

EMPLOYEES_FILES_PATH = os_path_join(ROOT_DIR, 'database', 'employees')
EMPLOYEES_EMAILS_LIST_PATH = os_path_join(ROOT_DIR, 'database', 'server', "employees_emails.csv")

INVENTORY_PATH_CSV = os_path_join(ROOT_DIR, 'database', 'server', "inventory.csv")
INVENTORY_PATH_PICKLE = os_path_join(ROOT_DIR, 'database', 'server', "inventory.bin")

del os_path_join, pardir, os_path_abspath, dirname, realpath
