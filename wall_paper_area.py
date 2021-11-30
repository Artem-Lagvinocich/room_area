class Parameters:
    def __init__(self, l, w, h):
        self.length = l
        self.width = w
        self.height = h


class Room(Parameters):
    def wall_area(self):
        wall_1 = self.length * self.height
        wall_2 = self.width * self.height
        room_walls = (wall_1 + wall_2) * 2
        return room_walls


class Window(Parameters):
    def window_area(self):
        window = self.height * self.length
        return window


class Door(Parameters):
    def door_area(self):
        door = self.height * self.width
        return door


class Wallpaper(Parameters):
    def get_paper_area(self):
        paper_area = self.length * self.width
        return paper_area


def area_to_wall_paper():
    area = r1.wall_area() - w1.window_area() - d1.door_area()
    count_rolls = area // wp.get_paper_area()
    part_of_the_roll = area % wp.get_paper_area()
    print('Конечная площать для поклейки: ', area)
    print('Кол-во целлых руллонов для поклейки: ', count_rolls)
    print('Часть целого руллона: ', part_of_the_roll)
    return area, count_rolls, part_of_the_roll


r1 = Room(6, 3, 2.7)
print('Room walls area: ', r1.wall_area())

w1 = Window(1.5, 1, 2)
print('Window area: ', w1.window_area())

d1 = Door(1, 0.65, 2.3)
print('Door area: ', d1.door_area())

wp = Wallpaper(10, 1, 1)
print('Wall paper area: ', wp.get_paper_area())

area_to_wall_paper()
