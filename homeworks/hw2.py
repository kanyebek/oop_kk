class Heroes:
    def __init__(self, name, hp):
        self.name = name
        self.hp = hp
    def action(self):
        print(f"{self.name} does a basic action")
    def attack(self):
        print(f"{self.name} attacks")
    def status(self):
        print(f"Name: {self.name},/n"
              f"HP: {self.hp},/n ")

class Archer(Heroes):
    def __init__(self, name, hp, arrows, precision):
        super().__init__(name, hp)
        self.arrows = arrows
        self.precision = precision
    def attack(self):
            if self.precision >= 50:
                print('Successfull attack')
                self.arrows -= 1
            else:
                print('Unsuccessful attack')
                self.arrows -= 1

    def rest(self):
        self.arrows += 5
        print(f'Now you have {self.arrows} arrows')
    def status(self):
        print(f"Name: {self.name}, HP: {self.hp}, Arrows: {self.arrows}, Precision: {self.precision}")

kanybek = Archer("Kanybek", 100, 5, 65)
kanybek.action()
kanybek.attack()
kanybek.rest()
kanybek.status()