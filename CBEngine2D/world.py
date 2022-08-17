from numpy import array
from object import Object


class World():  # класс всех объектов на экране
    def __init__(self, screen):
        self.screen = screen  # передача экрана для отрисовки

        self.create_objects()  # вызов функции создания объектов

    def create_objects(self):  # создание объектов с вершинами
        self.obj = self.get_object_from_file('presets/monkey_test.obj', 200, (300, 400))
        self.block_1 = self.quad((1000, 100), 200)
        self.block_2 = self.quad((700, 100), 100)
        self.block_2.rotate_z(70)
        self.tringle = self.figure((900, 500), array([(-100, 100), (0, -85), (100, 100)]), array([((0, 1, 2))]))

    # функция квадрата
    def quad(self, pos, size=float or int, faces=array([((0, 1, 2)), ((0, 2, 3))])):
        vert = array([(0, 0), (size, 0), (size, size), (0, size)])
        return Object(vert, faces, pos, self.screen)

    # функция с произвольными вершинами и гранями
    def figure(self, pos, vertex, facets):
        return Object(vertex, facets, pos, self.screen)

    def render_world(self):  # отрисовка всех объектов
        self.obj.render()
        self.block_1.render()
        self.block_2.render()
        self.tringle.render()

    # импорт объекта из obj файла
    # коментов побольше чем обычно потому что код функции не совсем мой и таким обычно не пользуюсь
    def get_object_from_file(self, filename, size, pos):
        vertex, faces = [], []
        with open(filename) as f:
            for line in f:
                if line.startswith('v '):  # если линия начинается с символа v
                    vertex.append([float(i) * size for i in line.split()[1:]] + [1])  # добавление вершин
                elif line.startswith('f'):  # если линия начинается с символа f
                    faces_ = line.split()[1:]
                    faces.append([int(face_.split('/')[0]) - 1 for face_ in faces_])  # добавление граней
        return Object(vertex, faces, pos, self.screen)  # возврат объекта с вершинами и гранями из файла
