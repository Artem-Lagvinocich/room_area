from abc import ABC, abstractmethod


class Parameters(ABC):
    def __init__(self, l, w):
        self.length = l
        self.width = w

    @abstractmethod
    def area_to_wall_paper(self, r1, w1, d1):
        area = r1.wall_area() - w1.window_area() - d1.door_area()
        count_rolls = area // wp.get_paper_area()
        part_of_the_roll = area % wp.get_paper_area()
        print('Конечная площать для поклейки: ', area)
        print('Кол-во целлых руллонов для поклейки: ', count_rolls)
        print('Часть целого руллона: ', part_of_the_roll)


class Room(Parameters):
    def __init__(self, l, w, h):
        super().__init__(l, w)
        self.height = h

    @abstractmethod
    def wall_area(self):
        wall_1 = self.length * self.height
        wall_2 = self.width * self.height
        room_walls = (wall_1 + wall_2) * 2
        return room_walls


class Window(Parameters):
    @abstractmethod
    def window_area(self):
        return self.width * self.length


class Door(Parameters):
    @abstractmethod
    def door_area(self):
        return self.length * self.width


class Wallpaper(Parameters):
    @abstractmethod
    def get_paper_area(self):
        return self.length * self.width


r1 = Room(6, 3, 2.7)
print('Room walls area: ', r1.wall_area())

w1 = Window(1.5, 2)
print('Window area: ', w1.window_area())

d1 = Door(2.3, 0.65)
print('Door area: ', d1.door_area())

wp = Wallpaper(10, 1)
print('Wall paper area: ', wp.get_paper_area())

# area_to_wall_paper()
