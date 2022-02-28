# Создать класс Computer (компьютер) с приватными атрибутами cpu и memory
from subprocess import call


class Computer:
    def __init__(self, cpu, memory):
        self.__cpu = cpu
        self.__memory = memory
# Добавить сеттеры и геттеры к существующим атрибутам
    @property
    def cpu(self):
        return self.__cpu

    @cpu.setter
    def cpu(self, value,):
        self.__cpu = value

    @property
    def memory(self):
        return self.__memory

    @memory.setter
    def memory(self, value):
        self.__memory = value
# Добавить в класс Computer метод make_computations, в котором бы выполнялись арифметические вычисления с атрибутами объекта cpu и memory
    def make_computations(self):
        return f"CPU + Memory = {self.__cpu + self.__memory}"

    def __str__(self):
        return f"CPU: {self.__cpu} " \
                f"Memory: {self.__memory}"

    def __gt__(self, other):
        return self.memory > other.memory

# Создать класс Phone (телефон) с приватным полем sim_cards_list (список симкард)
class Phone:
    def __init__(self, list_sim_cards):
        self.__list_sim_cards = list_sim_cards
# Добавить сеттеры и геттеры к существующему атрибуту
    @property
    def list_sim_cards(self):
        return self.__list_sim_cards

    @list_sim_cards.setter
    def list_sim_cards(self, value):
        self.__list_sim_cards = value
# Добавить в класс Phone метод call с входящим параметром sim_card_number и call_to_number, 
# в котором бы распечатывалась симуляция звонка в зависимости от переданного номера сим-карты 
# (например: если при вызове метода передать число 1 и номер телефона, распечатывается текст 
# “Идет звонок на номер +996 777 99 88 11” с сим-карты-1 - Beeline).
    def call(self, sim_card_number, call_to_number):
        print(f"Идет звонок на номер {sim} с сим-карты {sim}")

    def __str__(self):
        return f"list sim cards: {self.__list_sim_cards}"

# Создать класс SmartPhone и наследовать его от 2-х классов Computer и Phone
class SmartPhone(Computer, Phone):
    def __init__(self, cpu, memory, list_sim_cards):
        Computer.__init__(self, cpu, memory)
        Phone.__init__(self, list_sim_cards)
# Добавить метод в класс SmartPhone use_gps с входящим параметром location, который бы распечатывал симуляцию проложения маршрута до локации
    def use_gps(self, location):
        print(f"Локация отмечена, ведется маршрут в {location}")
# В каждом классе переопределить магический метод str которые бы возвращали полную информацию об объекте
# Перезаписать все магические методы сравнения в классе Computer, для того чтоб можно было сравнивать между собой объекты, по атрибуту memory
    def __str__(self):
        return f"CPU: {self.cpu} " \
                f"Memory:{self.memory} " \
                f"Sim card: {self.list_sim_cards}"


# Создать 1 объект компьютера, 1 объект телефона и 2 объекта смартфона
# Распечатать информацию о созданных объектах
# Опробовать все возможные методы каждого объекта (например: use_gps и тд.)
sim = ['мега-0555555555', 'Ошка-996505505505']
noutbook = Computer(8, 16)
noutbook.make_computations()
tel = Phone(1)
smartP = SmartPhone(888, 512, sim[0])
smartP2 = SmartPhone(15, 4, sim[1])
smartP.use_gps("ГОИН")

print(sim)
print(noutbook)
print(noutbook.make_computations())
print(call)
print(tel)
print(smartP)
print(smartP2)
print(noutbook > smartP)
