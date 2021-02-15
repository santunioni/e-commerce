import run.market as market
import run.interface.screen as screen
from models.structure.client import Client
import pickle
from time import sleep


def logout():
    market.status['current_user'] = None
    market.status['user_type'] = None


def login(*, email, password):
    # TODO: implement the login function

    if market.status['user_type'] == 'employee':
        path = market.EMPLOYEES_LIST_PATH
    else:
        path = market.CLIENTS_LIST_PATH

    with open(path, 'rb') as file:
        clients_list = pickle.load(file)
    if email in clients_list.emails:
        current_user = clients_list[email]
        if current_user.check_pass(password):
            market.status['current_user'] = clients_list[email]
        else:
            print("Wrong password!")
            sleep(2)
    else:
        while (signin := input("User isn't registered. Want to sign in (y/n)? ")) not in ['y', 'n']:
            continue
        if signin == 'y':
            screen.GeneralScreen.sign_in()


def sign_in(full_name, email, password):
    # TODO: implement the sign_in function
    # FIX IT: something is wrong here

    if market.status['user_type'] == 'employee':
        path = market.EMPLOYEES_LIST_PATH
    else:
        path = market.CLIENTS_LIST_PATH

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
        market.status['current_user'] = current_user


def close_order():
    # TODO: implement the close_order function
    pass


def inventory():
    # TODO: implement the inventory function
    return []
