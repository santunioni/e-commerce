# PYTHON LIBRARIES IMPORTS
from pickle import load as pickle_load
from pickle import dump as pickle_dump
from os.path import join as os_path_join
from os.path import exists as os_path_exists
from passlib.hash import pbkdf2_sha256 as cryp
from csv import reader, writer
# imported only for MYPY type checking
from typing import Union, Tuple

# LOCAL APP IMPORTS
# classes from the MARKET STRUCTURE package
from system.market_structure.client import Client
# importing ENVIRONMENT variables
from system.env_variables.program_wide_constants import (CLIENTS_FILES_PATH,
                                                         CLIENTS_EMAILS_LIST_PATH)


class ClientCredentials:

    @staticmethod
    def login(user_id: str, password: str) -> Union[Client, None]:

        _, user_file_exist = ClientCredentials.__user_exist(user_id)

        if user_file_exist:
            with open(ClientCredentials.__user_file_path(user_id), 'rb') as file:
                if ClientCredentials.__authenticate(client_object_in_check := pickle_load(file), password):
                    client_object: Client = client_object_in_check
                del client_object_in_check
            return client_object
        else:
            return None

    @staticmethod
    def sign_in(full_name: str, email: str, password: str) -> Union[Client, None]:

        user_id: str = email
        id_in_list, user_file_exist = ClientCredentials.__user_exist(user_id)
        if not id_in_list:
            with open(CLIENTS_EMAILS_LIST_PATH, 'a+', newline='') as file:
                file_writer = writer(file)
                file_writer.writerow(user_id)

        if not user_file_exist:
            # Register new clients
            new_client_object: Client = Client(full_name=full_name, email=email, password=password)
            with open(ClientCredentials.__user_file_path(user_id), 'wb') as file:
                pickle_dump(new_client_object, file)

            return new_client_object

        else:
            return ClientCredentials.login(user_id, password)


    @staticmethod
    def __authenticate(client_object: Client, password: str) -> bool:
        return client_object.check_pass(password)

    @staticmethod
    def __user_exist(identifier: str) -> Tuple[bool, bool]:

        with open(CLIENTS_EMAILS_LIST_PATH) as file:
            # the next line will get the email list from the csv file
            clients_list = [existent_id[0] for existent_id in reader(file) if len(existent_id) == 1]
            if identifier in clients_list:
                identifier_in_list = True
            else:
                identifier_in_list = False
        user_pickle_file = os_path_exists(ClientCredentials.__user_file_path(identifier))

        return identifier_in_list, user_pickle_file

    # Not being used:
    # @staticmethod
    # def __user__hash(identifier: str) -> str:
    #     return cryp.hash(identifier, rounds=200000, salt_size=16)

    @staticmethod
    def __user_file_path(identifier: str) -> str:
        return os_path_join(CLIENTS_FILES_PATH, f"{identifier}.bin")

# TODO: implement employees credentials Class
