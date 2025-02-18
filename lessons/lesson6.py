import sqlite3

# A4
connect = sqlite3.connect('User.db')

# Ruka c ruchkoi
cursor = connect.cursor()

cursor.execute('''
    CREATE TABLE users(
        name VARCHAR(25) NOT NULL
        age INT NOT NULL
        hobby  TEXT
    )                  
               '''
               )


# Множественное наследование

# горизонтальное наследование
# class Flyable:

#     def fly(self):
#         return 'Летит'


# class Swimmable:

#     def swim(self):
#         return 'Плавает'


# class Duck(Flyable, Swimmable):

#     def make_sound(self):
#         return 'Кря-Кря!!'

# donald_duck = Duck()
# print(donald_duck.fly())
# print(donald_duck.swim())

# ромбовидное наследование

class Animal:

    def __init__(self, name):
        self.name = name

    def make_sound(self):
        return "Издает звук"

    def action(self):
        return 'Базовое действие'


class Swimmable(Animal):

    def action(self):
        return 'Плавает'


class Flyable(Animal):

    def action(self):
        return 'Летит'


class Duck(Swimmable, Flyable):

    def make_sound(self):
        return 'Кря-Кря!!'

    def action(self):
        return 'Летает и плавает'


donald_duck = Duck('donald duck')
print(donald_duck.action())
print(Duck.mro())