def pyfiglet(a):
    from colorama import Fore, Style
    from pyfiglet import Figlet
    f = Figlet(font="slant")
    print(Fore.RED + f.renderText(a))
    print(Style.RESET_ALL)
pyfiglet('prod by GGB')

class Animal:
    def __init__(self, name):
        self.alive = True # Животное живо по умолчанию
        self.fed = False # Животное не накормлено по умолчанию
        self.name = name # Индивидуальное название животного

    def eat(self, food):
        if isinstance(food, Plant) and food.edible:
            print(f'{self.name} сьел {food.name}')
            self.fed =True
        else:
            print(f'{self.name} не стал есть {food.name}')
            self.alive = False

class Mammal(Animal):
    pass

class Predator(Animal):
    pass

class Plant:
    def __init__(self, name, edible):
        self.edible = edible
        self.name = name

class Flower(Plant):
    def __init__(self, name):
        super().__init__(name, False)  # Не съедобное по умолчанию

class Fruit(Plant):
    def __init__(self, name):
        super().__init__(name, True)  # Съедобное по умолчанию

a1 = Predator('Волк с Уолл-Стрит')
a2 = Mammal('Хатико')
p1 = Flower('Цветик семицветик')
p2 = Fruit('Заводной апельсин')

print(a1.name)
print(p1.name)

print(a1.alive)
print(a2.fed)

a1.eat(p1)
a2.eat(p2)

print(a1.alive)
print(a2.fed)