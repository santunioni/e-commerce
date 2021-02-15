import settings
from models.structure.client import Client

import pickle
from time import sleep


def logout():
    settings.status['current_user'] = None
    settings.status['user_type'] = None


def login(*, email, password):

    if settings.status['user_type'] == 'employee':
        path = settings.EMPLOYEES_LIST_PATH
    else:
        path = settings.CLIENTS_LIST_PATH

    with open(path, 'rb') as file:
        clients_list = pickle.load(file)
    if email in clients_list.emails:
        current_user = clients_list[email]
        if current_user.check_pass(password):
            settings.status['current_user'] = clients_list[email]
        else:
            print("Wrong password!")
            sleep(2)
    else:
        print("User isn't registered. Want to sign in (y/n)? ")
        sleep(2)


def sign_in(full_name, email, password):

    if settings.status['user_type'] == 'employee':
        path = settings.EMPLOYEES_LIST_PATH
    else:
        path = settings.CLIENTS_LIST_PATH

    with open(path, 'rb') as file:
        clients_list = pickle.load(file)
    if email in clients_list.emails:
        print("User is already registered. Perhaps you want to log in? ")
        sleep(2)
    else:
        current_user = Client(full_name=full_name, email=email, password=password)
        clients_list.add(current_user)
        with open(path, 'wb') as file:
            pickle.dump(clients_list, file)
        settings.status['current_user'] = current_user
