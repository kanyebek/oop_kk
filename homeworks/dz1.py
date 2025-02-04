class Hero:
    def __init__(self, name, lvl, hp):
        self.name = name
        self.lvl = lvl
        self.hp = hp
    def introduce(self, ):
        print(f"Привет, меня зовут {self.name}, мой lvl {self.lvl}, мое hp {self.hp}")
    def is_adult(self, ):
        if self.lvl >= 10:
            print(True)
        else:
            print(False)

kanybek = Hero('kanybek', 22, 150)
kanybek.introduce()
kanybek.is_adult()