# LOCAL APP IMPORTS
# importing auxiliary functions
from system.aux_functions.clear import clear
# importing the CLIENT and SERVER
from client.run import run as client_run
from server.run import run as server_run


def dev_page():
    clear()
    while (user_label := input('Are you a client or a employee here (c/e)? ').lower()[0]) not in ['c', 'e']:
        continue
    if user_label == 'c':
        client_run()
    if user_label == 'e':
        server_run()


def main():
    dev_page()


if __name__ == '__main__':
    main()
