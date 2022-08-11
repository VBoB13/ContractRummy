from traceback import print_tb
from colorama import Fore, Style

class BaseException(Exception):
    """
    Base Exception for all application.
    """

    def print_self(self):
        print(Fore.RED, "{:<1}".format(str(self)), Style.RESET_ALL)
        print_tb(self.__traceback__)
