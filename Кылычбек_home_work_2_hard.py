# Создать класс Figure(фигура) с атрибутом уровня класса unit(единица измерения величин)
#  и присвоить ему значение cm(сантиметры)
# В конструкторе класса Figure должен быть только 1 входящий параметр self.
class Figure:
    unit = "cm"
    def __init__(self):
# Создать приватный атрибут perimeter в классе Figure, который бы по умолчанию в конструкторе присваивался к нулю 
# Добавить в класс Figure нереализованный приватный метод calculate_perimeter(подсчет периметра фигуры)   
# Добавить в класс Figure нереализованный публичный метод calculate_area(подсчет площади фигуры)
        self.__calculate_perimeter()
        self.calculate_area()

# Создать в классе Figure геттер и сеттер для атрибута perimeter.
    def get_perimeter(self):
        return self.__perimeter
    def set_perimeter(self, perimeter):
        self.__perimeter = perimeter

    def calculate_area(self):
        pass
    def __calculate_perimeter(self):
        pass
    def info(self):         # Добавить в класс Figure нереализованный публичный метод info(вывод полной информации о фигуре)
        pass
# Создать класс Square(квадрат), наследовать его от класса Figure.
# Добавить в класс Square атрибут side_length(длина одной стороны квадрата), атрибут должен быть приватным.
class Square(Figure):
    def __init__(self, __side_length):
# В конструкторе класса Square должен высчитываться периметр квадрата,
#  посредством вызова метода calculate_perimeter и возвращаемый результат метода задавался бы атрибуту perimeter.         
        self.__side_length = __side_length
        self.calculate_area()
        self.perimeter = self.__calculate_perimeter()
#  В классе Square переопределить метод calculate_area, который бы считал и возвращал площадь квадрата.
    def calculate_area(self):
        return self.__side_length * 2   
#  В классе Square переопределить метод calculate_perimeter, который бы считал и возвращал периметр квадрата.
    def __calculate_perimeter(self):
        return self.__side_length * 4
#  В классе Square переопределить метод info, который бы распечатывал всю информацию о квадрате следующим образом: 
# Например - Square side length: 5cm, perimeter: 20cm, area: 25cm.
    def info(self):
        print(f"Square:   Side length:{self.__side_length}{self.unit}   Perimeter:{self.__calculate_perimeter()}{self.unit}   Area:{self.calculate_area()}{self.unit}")

# Создать класс Rectangle(прямоугольник), наследовать его от класса Figure.
class Rectangle(Figure):
# Добавить в класс Rectangle атрибут length(длина) и width(ширина), атрибуты должны быть приватными.
    def __init__(self, __length, __width):
# В конструкторе класса Rectangle должен высчитываться периметр прямоугольника,
#  посредством вызова метода calculate_perimeter и возвращаемый результат метода задавался бы атрибуту perimeter.        
        self.__width = __width
        self.__length = __length
# В классе Rectangle переопределить метод calculate_area, который бы считал и возвращал площадь прямоугольника
    def calculate_area(self):
        return self.__length * self.__width
# В классе Rectangle переопределить метод calculate_perimeter, который бы считал и возвращал периметр прямоугольника
    def __calculate_perimeter(self):
        return (self.__length + self.__width) * 2
# В классе Rectangle переопределить метод info, который бы распечатывал всю информацию о прямоугольнике следующим образом: 
# Например - Rectangle length: 5cm, width: 8cm, perimeter: 26cm, area: 40cm.
    def info(self):
        print(
            f"Rectangle: Length:{self.__length}{self.unit}   Width:{self.__width}{self.unit}   Perimeter:{self.__calculate_perimeter()}{self.unit}   Area:{self.calculate_area()}{self.unit}")
# В исполняемом файле создать список из 2-х разных квадратов и 3-х разных прямоугольников
sq1 = Square(12)
sq2 = Square(9)

rec1 = Rectangle(9, 13)
rec2 = Rectangle(3, 6)
rec3 = Rectangle(8, 10)
# Затем через цикл вызвать у всех объектов списка метод info
forms = [sq1, sq2, rec1, rec2, rec3]
for i in forms:
    i.info()