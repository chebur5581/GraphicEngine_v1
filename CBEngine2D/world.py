import pygame as pg
import numpy as np
from object import Object


class World():  # класс всех объектов на экране
    def __init__(self, screen):
        self.screen = screen

        self.create_objects()  # вызов функции создания объектов

        self.ang = 0

    def create_objects(self):  # создание объектов с вершинами
        # self.cube_1 = self.quad((550, 300), 200)
        #
        # self.cube_1.rotate_z(45)
        #
        # self.figure_1 = self.figure((200, 200),
        #                 np.array([(60, 50), (-60, 50), (0, -50)]),
        #                 np.array([((0, 1, 2))]))
        #
        # self.obj = self.get_object_from_file('test.obj', 50, (300, 400))

        self.plate = self.get_object_from_file('monkey_test.obj', 200, (300, 400))

    # функция квадрата
    def quad(self, pos, size=float or int, facets=np.array([((0, 1, 2)), ((0, 2, 3))])):
        vert = np.array([(0, 0), (size, 0), (size, size), (0, size)])
        return Object(vert, facets, pos, self.screen)

    def figure(self, pos, vertex, facets):
        return Object(vertex, facets, pos, self.screen)

    def render_world(self):  # отрисовка всех объектов
        # self.cube_1.render()
        # self.figure_1.render()
        # self.obj.render()
        self.plate.render()
        self.plate.rotate_z(self.ang)
        self.ang += 0.01

    def get_object_from_file(self, filename, size, pos):
        vertex, faces = [], []
        with open(filename) as f:
            for line in f:
                if line.startswith('v '):
                    vertex.append([float(i) * size for i in line.split()[1:]] + [1])
                elif line.startswith('f'):
                    faces_ = line.split()[1:]
                    faces.append([int(face_.split('/')[0]) - 1 for face_ in faces_])
        return Object(vertex, faces, pos, self.screen)