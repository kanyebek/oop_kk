class Hero:
    def __init__(self, name, hp,  lvl):
        self.name = name
        self.hp = hp
        self.lvl = lvl
    def action(self):
        print(f"base action")

class Warrior(Hero):
    # Полиморфизм
    def __init__(self, name='John Doe', hp=100, lvl=1, st=50):
        super().__init__(name, hp, lvl)
        self.st = st
    def action(self):
        print(f"{self.name} action")

kirrito = Warrior(lvl=5, hp=1000, st=100, name='kirrito')
kirrito.action()

# Инкапсуляция
class BankAccount:
    def __init__(self, clientik, balance, password):
        self.client = clientik # открытый атрибут
        self._balance = balance # защищенный атрибут
        self.__password = password # приватный атрибут
    def about(self, amount):
        print(f"{self.__password}")
    def __top_up_balance(self,amount):
        self._balance += amount
    def add_balance(self, cash):
        self.__top_up_balance(cash)
        print(f'Balance update')

client = BankAccount("John Doe", 1000, 123456)
# client.about()
# print(client._BankAccount__password)
