# Создать класс под названием data, в класс добавить атрибуты full_name, email, file_name, color.
class Data:
    def __init__(self, full_name, email, file_name, color):
        self.__full_name = full_name
        self.__email = email
        self.__file_name = file_name
        self.__color = color
# Добавить геттеры и сеттеры для всех атрибутов
    @property
    def full_name(self):
        return self.__full_name

    @full_name.setter
    def full_name(self, value):
        self.__full_name = value

    @property
    def email(self):
        return self.__email

    @email.setter
    def email(self, value):
        self.__email = value

    @property
    def file_name(self):
        return self.__file_name

    @file_name.setter
    def file_name(self, value):
        self.__file_name = value

    @property
    def color(self):
        return self.__color

    @color.setter
    def color(self, value):
        self.__color = value

# Затем считать из файла MOCK_DATA.txt, в котором 1000 строк с данными
# (Имя и Фамилия, почта, название файла с расширением и код цвета)
files = ['full_name.txt', 'email.txt', 'file_name.txt', 'color.txt']

 # Затем через цикл пройтись по каждому объекту и записать в 4 разных файла все типы информации.
# (1й файл: Имена с фамилиями, 2й файл: почта,
 # 3й файл: названия файлов с расширением, 4й файл: коды цветов)
def Work():
    with open('MOCK_DATA.txt') as fread:
        for line in fread:
            s = line.split()
            s[0] += ' ' + s.pop(1)
            if len(s) > 4:
                s[0] += ' ' + s.pop(1)
            info = Data(*s)
            with open(files[0], 'a') as f0:
                f0.write(info.full_name)
                f0.write('\r')
            with open(files[1], 'a') as f1:
                f1.write(info.email)
                f1.write('\r')
            with open(files[2], 'a') as f2:
                f2.write(info.file_name)
                f2.write('\r')
            with open(files[3], 'a') as f3:
                f3.write(info.color)
                f3.write('\r')


# очитска списков
def Clear():
    file = open('full_name.txt', 'w')
    file.close()

    file = open('email.txt', 'w')
    file.close()

    file = open('file_name.txt', 'w')
    file.close()

    file = open('color.txt', 'w')
    file.close()

Clear()
Work()