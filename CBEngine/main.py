import pygame as pg
from world import World


class App():  # главное окно приложения
    def __init__(self, WIDTH=1600, HEIGHT=800):
        pg.init()
        self.screen = pg.display.set_mode([WIDTH, HEIGHT])
        self.clock = pg.time.Clock()

        self.world = World(self.screen)  # класс со всеми объектами

    def run(self):
        while True:
            self.screen.fill((50, 50, 50))  # заполнение непонятным цветом

            self.world.render_world()  # отрисовка всех объектов

            [exit() for i in pg.event.get() if i.type == pg.QUIT]  # цикл проверки на закрытие окна

            pg.display.set_caption(str(self.clock.get_fps()))  # отрисовка fps на названии окна

            pg.display.flip()  # обновление экрана
            self.clock.tick(60)  # контроль тиков/фрэйм рейта


if __name__ == '__main__':  # TODO:придумать комментарий к этой строке
    app = App()  # создание экземпляра класса окна
    app.run()  # запуск программы
