import os
import random
from envparse import env


class Casino:
    def __init__(self):
        self.__cash = int(os.environ.get('MY_MONEY'))

        while int(self.__cash) > 0:
            self.__bet = int(input('Make your bet: '))
            if self.__bet > self.__cash:
                print('You have not enough money')
            else:
                self.__choice = int(input('Choice the slot: '))

                self.__slot = random.randint(1, 30)
                print(self.__slot)

                if self.__slot == self.__choice:
                    self.__cash += self.__bet
                    print(f'You win\n Your cash after win: {self.__cash}')
                    if self.__slot == self.__choice:
                        ans = input('Введите yes для продолжение введите no для выхода: ')
                        if ans == 'yes':
                            continue
                        if ans == 'no':
                            break

                else:
                    self.__cash -= self.__bet
                    print(f' You lost \n Your cash after lost: {self.__cash}')
                    if self.__slot != self.__choice:
                        ans = input('Введите yes для продолжение введите no для выхода: ')
                        if ans == 'yes':
                            continue
                        if ans == 'no':
                            break

    @property
    def slot(self):
        return self.__slot

    @slot.setter
    def slot(self, value):
        self.__slot = value


env.read_envfile('settings.env')