class Person:
    # Функция - конструктор
    def __init__(self, name, age):
        # Атрибуты класса
        self.name = name
        self.age = age

    # self - ссылка на обьект(экземпляр класса)
    # Метод класса
    def introduce(self,):
        print(f"Hi, I'm {self.name}")

# Обьект класса, экземпляр класса class OBJ
ardager = Person('Ardager', 19)
ardager.introduce()

print(type(ardager))
print(type('HEllO'))
print(type(14))

class Hero:

    def __init__(self, name, hp, lvl):
        self.name = name
        self.hp = hp
        self.lvl =lvl

    def action(self, ):
        print(f"{self.name} делает базовое действие")

# naofume = Hero("NaoFume", 100, 3)

# Дочерний класс
class ShieldHero(Hero):
    pass

naofume = ShieldHero("NaoFume", 100, 3)

naofume.action()

# class -- CamelCase
# переменные, методы, функции -- snek_case