from abc import ABC


class Parameters(ABC):
    def __init__(self, l, w):
        self.length = l
        self.width = w

    @staticmethod
    def area_to_wall_paper():
        area = room_parameters.wall_area() - window_parameters.get_area() - door_parameters.get_area()
        count_rolls = area // wall_paper_parameters.get_area()
        part_of_the_roll = area % wall_paper_parameters.get_area()
        print('Конечная площать для поклейки: ', area)
        print('Кол-во целлых руллонов для поклейки: ', count_rolls)
        print('Часть целого руллона: ', part_of_the_roll)


class Room(Parameters):
    def __init__(self, l, w, h):
        super().__init__(l, w)
        self.height = h

    def wall_area(self):
        wall_1 = self.length * self.height
        wall_2 = self.width * self.height
        room_walls = (wall_1 + wall_2) * 2
        return room_walls


class Counting(Parameters):
    def get_area(self):
        return self.width * self.length


room_parameters = Room(6, 3, 2.7)
print('Room walls area: ', room_parameters.wall_area())

window_parameters = Counting(1.5, 2)
print('Window area: ', window_parameters.get_area())

door_parameters = Counting(2.3, 0.65)
print('Door area: ', door_parameters.get_area())

wall_paper_parameters = Counting(10, 1)
print('Wall paper area: ', wall_paper_parameters.get_area())

Parameters.area_to_wall_paper()
