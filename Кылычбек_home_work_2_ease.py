#  Создать класс Figure(фигура)
class Figure:
# с атрибутом уровня класса unit(единица измерения величин) и присвоить ему
#  значение cm(сантиметры)
    unit = "cm"
    # В конструкторе класса Figure должен быть только 1 входящий параметр self, то есть не должно быть атрибутов уровня объекта
    def __init__(self):
        pass
    # Добавить в класс Figure нереализованный публичный метод calculate_area(подсчет площади фигуры)
    def calculate_area(self):
        pass
    # Добавить в класс Figure нереализованный публичный метод info(вывод полной информации о фигуре)
    def info(self):
        pass

# Создать класс Circle(круг), наследовать его от класса Figure.
class Circle(Figure):
    p = 3.14
    # Добавить в класс Circle атрибут radius(радиус круга), атрибут должен быть приватным.
    def __init__(self,radius):
        self.__radius = radius
    # В классе Circle переопределить метод calculate_area, который бы считал и возвращал площадь круга    
    def calculate_area(self):
        return Circle.p * (self.__radius ** 2)
    # В классе  Circle переопределить метод info, который бы распечатывал всю информацию о круге следующим образом: 
    # Например -  Circle radius: 2cm, area: 12.57cm    
    def info(self):
        print(f"Circle radius: {self.__radius}, area: {self.calculate_area()} {self.unit}")

# Создать класс Triangle(треугольник), наследовать его от класса Figure
class Triangle(Figure):
    # Добавить в класс Triangle атрибут side_a(сторона а) и side_b(сторона б), атрибуты должны быть приватными
    def __init__(self, side_a,side_b):
        super().__init__()
        self.__side_a =  side_a
        self.__side_b = side_b
    # Добавить в класс Triangle атрибут side_a(сторона а) и side_b(сторона б), атрибуты должны быть приватными    
    def calculate_area(self):
        return self.__side_b * self.__side_a / 2
    #В классе Triangle переопределить метод info, который бы распечатывал всю информацию о треугольнике следующим образом: 
    # Например - Triangle side a: 5cm, side b: 8cm, area: 20cm    
    def info(self):
        print(f"Triangle side a: {self.__side_a}, side b: {self.__side_b}, area: {self.calculate_area()} {self.unit}.")

# В исполняемом файле создать список из 2-х разных кругов и 3-х разных треугольников
ciOne = Circle(8)
ciTwo = Circle(4)

trOne = Triangle(3, 6)
trTwo = Triangle(4, 9)
trTree = Triangle(2, 4)

# Затем через цикл вызвать у всех объектов списка метод info
general = [ciOne, ciTwo, trOne, trTwo, trTree]
for i in general:
    i.info()