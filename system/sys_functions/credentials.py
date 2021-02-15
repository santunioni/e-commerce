# TODO: I must refactor this file because I don't want to import anything from client to the sys_functions folder
import client.session
from system.market_structure.client import Client

from system import globals
from pickle import load as pickle_load
from pickle import dump as pickle_dump
from time import sleep


def logout():
    client.session.status['current_user'] = None
    client.session.status['user_type'] = None


def login(*, email, password):

    if client.session.status['user_type'] == 'employee':
        path = globals.EMPLOYEES_LIST_PATH
    else:
        path = globals.CLIENTS_LIST_PATH

    with open(path, 'rb') as file:
        clients_list = pickle_load(file)
    if email in clients_list.emails:
        current_user = clients_list[email]
        if current_user.check_pass(password):
            client.session.status['current_user'] = clients_list[email]
        else:
            print("Wrong password!")
            sleep(2)
    else:
        print("User isn't registered. Want to sign in (y/n)? ")
        sleep(2)


def sign_in(full_name, email, password):

    if client.session.status['user_type'] == 'employee':
        path = globals.EMPLOYEES_LIST_PATH
    else:
        path = globals.CLIENTS_LIST_PATH

    with open(path, 'rb') as file:
        clients_list = pickle_load(file)
    if email in clients_list.emails:
        print("User is already registered. Perhaps you want to log in? ")
        sleep(2)
    else:
        current_user = Client(full_name=full_name, email=email, password=password)
        clients_list.add(current_user)
        with open(path, 'wb') as file:
            pickle_dump(clients_list, file)
        client.session.status['current_user'] = current_user
