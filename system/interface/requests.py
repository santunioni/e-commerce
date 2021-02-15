# PYTHON LIBRARIES IMPORTS
from os.path import exists as os_path_exists
from os import mknod
# from pickle import load as pickle_load
# from pickle import dump as pickle_dump
import pickle

# LOCAL APP IMPORTS
# importing app ENVIRONMENT variables
from system.env_variables.program_wide_constants import INVENTORY_PATH_PICKLE
# classes from the MARKET STRUCTURE package
from system.market_structure.market_collections import InventoryModel
# used only for TYPE HINTING
from system.market_structure.client import Kart


class InventoryManager:

    # inicialize __INVENTORY variable
    if os_path_exists(INVENTORY_PATH_PICKLE):
        with open(INVENTORY_PATH_PICKLE, 'rb') as invent_file:
            __inventory = pickle.load(invent_file)
    else:
        __inventory: InventoryModel = InventoryModel()
        with open(INVENTORY_PATH_PICKLE, 'xb') as invent_file:
            pickle.dump(__inventory, invent_file)

    @staticmethod
    def inventory():
        return InventoryManager.__inventory

    @classmethod
    def update(cls):
        with open(INVENTORY_PATH_PICKLE, 'rb') as invent_file:
            cls.__inventory = pickle.load(invent_file)

    @classmethod
    def deduct_order(cls, order: Kart):
        cls.update()
        cls.__inventory -= order
        with open(INVENTORY_PATH_PICKLE, 'wb') as invent_file:
            pickle.dump(cls.__inventory, invent_file)
