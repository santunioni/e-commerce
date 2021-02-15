# python libraries imports
from pickle import load as pickle_load
from pickle import dump as pickle_dump
from os.path import join as os_path_join
from os.path import exists as os_path_exists
from passlib.hash import pbkdf2_sha256 as cryp
from csv import reader, writer

# project imports
from system.market_structure.client import Client
from system.sys_functions.program_wide_constants import (CLIENTS_FILES_PATH,
                                                         CLIENTS_EMAILS_LIST_PATH)


class ClientCredentials:

    @staticmethod
    def login(user_id, password):

        _, user_file_exist = ClientCredentials.__user_exist(user_id)

        if user_file_exist:
            user_id_hash = cryp.hash(user_id, rounds=200000, salt_size=16)
            with open(os_path_join(CLIENTS_FILES_PATH, user_id_hash), 'rb') as file:
                if ClientCredentials.__authenticate(client_object_in_check := pickle_load(file), password):
                    client_object = client_object_in_check
                del client_object_in_check
            return client_object
        else:
            # TODO: implement clients sign in in case he/she is not registered yet
            return None

    @staticmethod
    def sign_in(full_name, email, password):

        user_id = email
        id_in_list, user_file_exist = ClientCredentials.__user_exist(user_id)

        if not id_in_list:
            with open(CLIENTS_EMAILS_LIST_PATH, 'a+', newline='') as file:
                file_writer = writer(file)
                file_writer.writerow(user_id)

        if not user_file_exist:
            # Register new clients
            new_client_object = Client(full_name=full_name, email=email, password=password)
            with open(os_path_join(CLIENTS_FILES_PATH, f"{cryp.hash(user_id)}.bin"), 'wb') as file:
                pickle_dump(new_client_object, file)

            return new_client_object

        else:
            return ClientCredentials.login(user_id, password)


    @staticmethod
    def __authenticate(client_object, password):
        return client_object.check_pass(password)

    @staticmethod
    def __user_exist(identifier):

        with open(CLIENTS_EMAILS_LIST_PATH) as file:
            clients_list = reader(file)
            if identifier in clients_list:
                identifier_in_list = True
            else:
                identifier_in_list = False

        user_file_exist = os_path_exists(os_path_join(CLIENTS_FILES_PATH, f"{cryp.hash(identifier)}.bin"))

        return identifier_in_list, user_file_exist

# TODO: implement employees credentials Class
