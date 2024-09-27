import math
class Figure:

    sides_count = 0

    def __init__(self, color: list[int, int, int], *sides, filled=False):
        if self.__is_valid_color(color[0], color[1], color[2]):
            self.__color = list(color)
        self.__sides = list(sides)
        self.filled = filled


    def get_color(self):
        return self.__color
    @staticmethod
    def __is_valid_color(r, g, b):
        valid_value = 0 <= r <= 255 and 0 <= g <= 255 and 0 <= b <= 255
        valid_types = isinstance(r, int) and isinstance(g, int) and isinstance(b, int)
        return valid_value and valid_types

    def set_color(self, r, g, b):
        if self.__is_valid_color(r, g, b):
            self.__color = [r, g, b]

    @staticmethod
    def __is_valid_sides(*sides_int_list):
        for side in sides_int_list:
            if not isinstance(side, int) or side <= 0:
                return False
        return True


    def get_sides(self):
        return self.__sides

    def __len__(self):
        return sum(self.__sides)

    def set_sides(self, *new_sides):
        if len(new_sides) == len(self.__sides):
            valid_sides = []
            for side in new_sides:
                if self.__is_valid_sides(side):
                    valid_sides.append(side)
            self.__sides = valid_sides



class Circle(Figure):
    sides_count = 1

    def __init__(self, color: list[int, int, int], length, filled=False):
        super().__init__(color, length, filled = filled)
        self.__radius = length/ (2 * math.pi)


    def get_square(self):
        return len(self)**2 / (4 * math.pi)



class Triangle(Figure):
    sides_count = 3
    def __init__(self, color: tuple[int, int, int], height, *sides, filled = False):
        super().__init__(color, *sides, filled=filled)
        self.height = height

    def get_square(self):
        '''По формуле через полупериметр:'''
        half_P = 0.5 * len(self)
        sides = self.get_sides()
        return math.sqrt(half_P*(half_P - sides[0])*(half_P - sides[1])*(half_P - sides[2]))


class Cube(Figure):
    sides_count = 12

    def __init__(self, color: list[int, int, int], side, filled = False):
        cube_sides = [side]*12
        super().__init__(color, *cube_sides, filled = filled)

    def get_volume(self):
        return self.get_sides()[0] ** 3

'''
ВАЖНО!
При создании объектов делайте проверку на количество переданных сторон, если сторон не ровно sides_count, то создать массив с единичными сторонами и в том кол-ве, которое требует фигура.
Пример 1: Circle((200, 200, 100), 10, 15, 6), т.к. сторона у круга всего 1, то его стороны будут - [1]
Пример 2: Triangle((200, 200, 100), 10, 6), т.к. сторон у треугольника 3, то его стороны будут - [1, 1, 1]
Пример 3: Cube((200, 200, 100), 9), т.к. сторон(рёбер) у куба - 12, то его стороны будут - [9, 9, 9, ....., 9] (12)
Пример 4: Cube((200, 200, 100), 9, 12), т.к. сторон(рёбер) у куба - 12, то его стороны будут - [1, 1, 1, ....., 1]
'''
circle1 = Circle((200, 200, 100), 10) # (Цвет, стороны)
cube1 = Cube((222, 35, 130), 6)

# Проверка на изменение цветов:
circle1.set_color(55, 66, 77) # Изменится
print(circle1.get_color())
cube1.set_color(300, 70, 15) # Не изменится
print(cube1.get_color())

# Проверка на изменение сторон:
cube1.set_sides(5, 3, 12, 4, 5) # Не изменится
print(cube1.get_sides())
circle1.set_sides(15) # Изменится
print(circle1.get_sides())

# Проверка периметра (круга), это и есть длина:
print(len(circle1))

# Проверка объёма (куба):
print(cube1.get_volume())
