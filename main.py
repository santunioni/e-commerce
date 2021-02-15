# project imports
from client import run as market


def initial_page():
    clear()
    if not client.session.status['user_type']:
        while (user_label := input('Are you a clients or a employees here (c/e)? ').lower()[0]) not in ['c', 'e']:
            continue
        client.session.status['user_type'] = 'clients' if user_label == 'c' else 'employees'
    elif client.session.status['user_type'] == 'clients':
        ClientScreen.initial_page()
    elif client.session.status['user_type'] == 'employees':
        EmployeeScreen.initial_page()


def main():
    market.run()


if __name__ == '__main__':
    main()
