import math

class Figure:
    def __init__(self, color, *sides):
        self._sides = list(sides)[:self.sides_count] or [1] * self.sides_count
        self.filled = False
        self._color = color

    @property
    def sides_count(self):
        raise NotImplementedError("sides_count must be implemented by subclasses")

    def get_color(self):
        return self._color

    def _is_valid_color(self, r, g, b):
        return all(0 <= value <= 255 for value in (r, g, b))

    def set_color(self, r, g, b):
        if self._is_valid_color(r, g, b):
            self._color = (r, g, b)

    def _is_valid_sides(self, *new_sides):
        return len(new_sides) == self.sides_count and all(isinstance(side, int) and side > 0 for side in new_sides)

    def get_sides(self):
        return self._sides

    def set_sides(self, *new_sides):
        if self._is_valid_sides(*new_sides):
            self._sides = list(new_sides)

    def __len__(self):
        return sum(self._sides)


class Circle(Figure):
    sides_count = 1

    def __init__(self, color, diameter):
        super().__init__(color, diameter)
        self.diameter = diameter
        self._radius = self.calculate_radius()

    def calculate_radius(self):
        return self.diameter / 2

    def get_square(self):
        radius = self._radius
        return math.pi * radius ** 2

    def set_sides(self, new_diameter):
        if self._is_valid_sides(new_diameter):
            self.diameter = new_diameter
            self._radius = self.calculate_radius()

    def __len__(self):
        return self.diameter


def heron(a, b, c):
    s = (a + b + c) / 2
    area = (s * (s - a) * (s - b) * (s - c)) ** 0.5
    return area


class Triangle(Figure):
    sides_count = 3

    def get_square(self):
        a, b, c = self._sides
        return heron(a, b, c)


class Cube(Figure):
    sides_count = 12

    def __init__(self, color, *sides):
        super().__init__(color, *sides)
        if len(self._sides) != self.sides_count:
            self._sides = [self._sides[0]] * self.sides_count

    def get_volume(self):
        edge_length = self._sides[0]
        return edge_length ** 3

if __name__ == "__main__":
    circle1 = Circle((200, 200, 100), 10)  # (Цвет, диаметр)
    cube1 = Cube((222, 35, 130), 6)

    # Проверка на изменение цветов:
    circle1.set_color(55, 66, 77)  # Изменится
    print(circle1.get_color())

    cube1.set_color(300, 70, 15)  # Не изменится
    print(cube1.get_color())

    # Проверка на изменение сторон:
    cube1.set_sides(5, 3, 12, 4, 5)  # Не изменится
    print(cube1.get_sides())

    circle1.set_sides(15)  # Изменится
    print(circle1.get_sides())

    # Проверка периметра (круга), это и есть длина:
    print(len(circle1))

    # Проверка объёма (куба):
    print(cube1.get_volume())