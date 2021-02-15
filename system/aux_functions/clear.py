# python libraries imports
# from os import system, name


def clear():
    """This function clear the terminal screen, either for Linux, Mac or Windows."""
    # for windows
    if name == 'nt':
        _ = system('cls')

        # for mac and linux(here, os.name is 'posix')
    else:
        _ = system('clear')