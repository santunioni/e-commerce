from models.interface.screen import ClientScreen, EmployeeScreen
import models.interface.screen as screen
import models.interface.request as request

status = {
    'current_user': None,
    'user_type': None
}


def run():

    while True:
        screen.initial_page()
