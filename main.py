from client import run as market


def initial_page():
    clear()
    if not client.session.status['user_type']:
        while (user_label := input('Are you a client or a employee here (c/e)? ').lower()[0]) not in ['c', 'e']:
            continue
        client.session.status['user_type'] = 'client' if user_label == 'c' else 'employee'
    elif client.session.status['user_type'] == 'client':
        ClientScreen.initial_page()
    elif client.session.status['user_type'] == 'employee':
        EmployeeScreen.initial_page()


def main():
    market.run()


if __name__ == '__main__':
    main()
