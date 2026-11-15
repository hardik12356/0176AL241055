class Character:
    def __init__(self, name, health):
        self.name = name
        self.health = health

    def display(self):
        print("Name:", self.name)
        print("Health:", self.health)

class Warrior(Character):
    def attack(self):
        print(self.name, "attacks with a sword")

class Mage(Character):
    def attack(self):
        print(self.name, "uses magic")

class Archer(Character):
    def attack(self):
        print(self.name, "shoots an arrow")

w = Warrior("Warrior", 100)
m = Mage("Mage", 80)
a = Archer("Archer", 90)

w.display()
w.attack()

m.display()
m.attack()

a.display()
a.attack()