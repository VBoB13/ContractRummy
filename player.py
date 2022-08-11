from colorama import Fore

from user import User

class Player(User):
    def __init__(self, email: str, nickname: str):
        super().__init__(email, nickname)

    def print(self):
        print(Fore.CYAN + "{}".format(self.nickname), Fore.RESET)