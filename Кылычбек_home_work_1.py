# Создать класс Person с атрибутами fullname, age, is_married
class Person:
    def init(self, full_name, age, is_married):
        self.full_name = full_name
        self.age = age
        self.is_married = is_married

# Добавить в класс Person метод introduce_myself
    def introduce_myself(self, full_name, age, is_married):
        print(f"fullname: {full_name} \n age: {age} \n is_married: {is_married}")

    def output(self,):
        return f"full name {self.full_name}\n" \
            f"age {self.age}\n" \
            f"is married {self.is_married}\n" \


# Создать класс Student наследовать его от класса Person и дополнить его атрибутом marks
class Student(Person):
# дополнить его атрибутом marks
    def __init__(self, full_name, age, is_married, marks):
        Person.init(self, full_name, age, is_married)
        self.marks = marks
# Добавить метод в класс Student, который бы подсчитывал среднюю оценку ученика по всем предметам
    def average(self):
        print(sum(self.marks) / 5)

# Создать класс Teacher и наследовать его от класса Person
class Teacher(Person):
# дополнить атрибутом experience
    def __init__(self, full_name, age, is_married, experience=3):
        Person.init(self, full_name, age, is_married)
        self.experience = experience
        #Добавить в класс Teacher поле уровня класса salary
        self.salary = 15000
#Также добавить метод в класс Teacher, который бы считал зарплату по следующей формуле:
#к стандартной зарплате прибавляется бонус 5% за каждый год опыта свыше 3х лет.
    def Teacher_cash(self):
        if self.experience > 3:
            new_salary = self.salary + ((self.salary/100*5) * (self.experience-3))
            return new_salary
#Создать объект учителя и распечатать всю информацию о нем и высчитать зарплату
teacher06 = Teacher("Феликс", 35, True, 8)

print(f'{teacher06.full_name} {teacher06.age} {teacher06.is_married} {teacher06.experience}')
print(teacher06.Teacher_cash())

#Написать функцию create_students, в которой создается 3 объекта ученика,
#эти ученики добавляются в список и список возвращается методом как результат.
def create_students():
    student1 = Student(full_name="Кылычбек", age=26, is_married=True, marks={
        "география": 5,
        "химия": 4,
        "физика": 3,
        "русский-язык": 4,
        "математика": 5,
        "кыргыз-тили": 5,
    })
    student2 = Student(full_name="Нурбек", age=22, is_married=False, marks={
        "география": 4,
        "химия": 3,
        "физика": 3,
        "русский-язык": 4,
        "математика": 4,
        "кыргыз-тили": 5,
    })
    student3 = Student(full_name="Алмаз", age=19, is_married=False, marks={
        "география": 3,
        "химия": 2,
        "физика": 3,
        "русский-язык": 4,
        "математика": 3,
        "кыргыз-тили": 5,
    })

    resultu = [student1, student2, student3]
    return resultu

#Вызвать функцию create_students и через цикл распечатать всю 
#информацию о каждом ученике с его оценками по каждому предмету. Также рассчитать его среднюю оценку по всем предметам.
students = create_students()
for i in students:
    list = []
    for marks in i.marks.values():
        list.append(marks)
    print(f"Name: {i.full_name}\n"
        f"Age: {i.age}\n"
        f"Maried: {i.is_married}\n"
        f"Average marks: {sum(list)/len(list)}\n")