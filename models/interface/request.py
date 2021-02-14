# TODO: implement storage into HD: Products for sell; Clients list; Client kart
import models.market as market
import models.interface.screen as screen
from models.structure.client import Client
import main
import pickle
import os


def logout():
    market.status['current_user'] = None
    market.status['user_type'] = None


def login(*, email, password):
    # TODO: implement the login function

    clients_list_path = os.path.join(main.DIR, 'database', market.status['user_type'], "clients.pickle")
    with open(clients_list_path, 'rb') as file:
        clients_list = pickle.load(file)
    if email in clients_list:
        market.status['current_user'] = clients_list['email']

    else:
        while (sign_in := input("User isn't registered. Want to sign in (y/n)? ")) not in ['y', 'n']:
            continue
        if sign_in == 'y':
            screen.GeneralScreen.sign_in()


def sign_in(email, password):
    # TODO: implement the sign_in function

    file_path = os.path.join(main.DIR, 'database', market.status['user_type'], f"{email}.pickle")
    try:
        with open(file_path, 'wb') as file:
            user =
            pickle.dump(user, file)
    except FileExistsError:
        while (login := input("User already exist. Want to sign in (y/n)? ")) not in ['y', 'n']:
            continue
        if login == 'y':
            screen.GeneralScreen.login()

    market.status['current_user'] = user


def close_order():
    # TODO: implement the close_order function
    pass


def inventory():
    # TODO: implement the inventory function
    return []
