import models.market as market
from os import getcwd


DIR = getcwd()
del getcwd


def main():
    market.run()


if __name__ == '__main__':
    main()
