import pygame as pg
import numpy as np
from object import Object
import math

class World():  # класс всех объектов на экране
    def __init__(self, screen):
        self.screen = screen

        self.create_objects()  # вызов функции создания объектов

    def create_objects(self):  # создание объектов с вершинами
        self.cube_1 = self.quad((0, 0), 100)

    # функция квадрата
    def quad(self, pos, size=float or int, facets=np.array([((0, 1, 2)), ((0, 2, 3))])):
        vert = np.array([(0, 0), (size, 0), (size, size), (0, size)])
        return Object(vert, facets, pos, self.screen)

    def render_world(self):  # отрисовка всех объектов
        self.cube_1.render()


