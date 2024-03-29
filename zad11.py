#!./venv/bin/python3.10

from exam_lib import User

class VIPUser(User):
    def __init__(self, mail, name, surname, card_number):
        super().__init__(mail, name, surname)
        self._card_number = card_number if self._check_card(card_number) else None

    @staticmethod
    def _check_card(card_number):
        return card_number > 999 and card_number % 2 == 0

    @staticmethod
    def use_vip_card():
        return None

    @property
    def card_number(self):
        return self._card_number

    @card_number.setter
    def card_number(self, card_number):
        self._card_number = card_number if self._check_card(card_number) else None


if __name__ == '__main__':
    user = VIPUser("Brajanusz", "Kowalski", "Kowalski@mail.pl", 1999)
    print(user.card_number)
    user.card_number = 9998
    print(user.card_number)
