import random

class Animal:
    _DEGREE_OF_DANGER = 0

    def __init__(self, speed):
        self.live = True
        self._cords = [0, 0, 0]
        self.speed = speed
        self.sound = None

    def move(self, dx, dy, dz):
        if dz < 0:
            print("It's too deep, i can't dive :(")
        else:
            self._cords[0] += self.speed * dx
            self._cords[1] += self.speed * dy
            self._cords[2] += self.speed * dz

    def get_cords(self):
        return f"X: {self._cords[0]}, Y: {self._cords[1]}, Z: {self._cords[2]}"

    def attack(self):
        if self._DEGREE_OF_DANGER < 5:
            print("Sorry, i'm peaceful :)")
        else:
            print("Be careful, i'm attacking you 0_0")

    def speak(self):
        print(self.sound)

class Bird(Animal):
    beak = True

    def lay_eggs(self):
        return f"Here are {random.randint(1, 4)} eggs for you"

class AquaticAnimal(Animal):
    _DEGREE_OF_DANGER = 3

    def dive_in(self, dz):
        dz = abs(dz)
        self.speed //= 2
        self._cords[2] -= dz

class PoisonousAnimal(Animal):
    _DEGREE_OF_DANGER = 8

class Duckbill(Bird, AquaticAnimal, PoisonousAnimal):
    sound = "Click-click-click"

# Пример использования
db = Duckbill(10)

print(db.live)
print(db.beak)
db.speak()
db.attack()
db.move(1, 2, 3)
print(db.get_cords())
db.dive_in(6)
print(db.get_cords())
db.lay_eggs()
