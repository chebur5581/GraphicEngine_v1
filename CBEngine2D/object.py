import pygame as pg
import numpy as np
import math


class Object():  # класс для создания объектов.
    def __init__(self, vertex, facets, pos, screen):
        self.vertex = vertex  # вершины
        self.facets = facets  # грани
        self.x, self.y, = pos  # позиция

        self.basis = np.array([(1, 0),  # базисы
                               (0, 1)])

        self.screen = screen  # экран на котором происходит отрисовка

    def render(self):  # обработка граней и добавление в массив точек которые нужно объединить в полигон
        for facet in self.facets:
            sub_poly = []
            for ind in facet:
                sub_poly.append(self.vertex[ind])
            self.draw_poly(sub_poly)  # вызов функции отрисовки полигона

    def draw_poly(self, vertex):  # отрисовка полигона исходя из переданных ему вершин
        poly = []
        for vert in enumerate(vertex):
            poly.append(vert[1][0] * self.basis[0] + vert[1][1] * self.basis[1])
            # ^вычисление положения точки/вектора изходя из базисов^
            poly[vert[0]][0] += self.x  # смещение
            poly[vert[0]][1] += self.y
        pg.draw.polygon(self.screen, (150, 200, 150), poly, 2)

    def rotate_z(self, angle):
        self.basis = np.array([(math.cos(angle), -math.sin(angle)),
                               (math.sin(angle), math.cos(angle))])
