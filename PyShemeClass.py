import random
import turtle
from turtle import *
import math
from time import time

turtle.tracer(0)
turtle.delay(0)

WIDTH, HEIGHT = 1200, 1000
screen = Screen()
screen.setup(WIDTH + 5, HEIGHT + 5)  # fudge factors due to window borders & title bar
screen.setworldcoordinates(0, HEIGHT, WIDTH, 0)


class PyScheme:
    # Класс построения секции, основана на функция эллипса и линии
    def __init__(self):
        self.myturtle = turtle.Turtle()
        self.myturtle.hideturtle()
        self.myturtle.pensize(1)
        self.myturtle.speed(0)
        self.x_pos = 0
        self.y_pos = 0
        self.section_len = 0
        self.section_stat = {}
        self.DWN = 0
        self.UP = 0
        self.isfirst = False
        # диаметр эллипса - 30
        self.el_diam = 30
        # ширина эллипса - 8
        self.el_len = 8
        self.x1 = 0
        self.x2 = 0
        self.UP = 0
        self.DWN = 0
        self.scheme_colors = {'blue': '#8C8CFF', 'green': '#8CFF8C', 'yellow': '#FFFF8C', 'pink': '#FFC8C8',
                              'red': '#FF6464',
                              'white': '#FFFFFF'}
        self.scheme_colors_index = ['blue', 'green', 'yellow', 'pink', 'red', 'white']
        self.f_color = ''
        self.weld_angle = 0

    def section_draw(self, x_pos, y_pos, section_len, section_stat, isfirst=False):

        self.isfirst = isfirst
        self.f_color = self.scheme_colors[self.scheme_colors_index[random.randrange(0, len(self.scheme_colors_index))]]
        self.y_pos = y_pos
        # коорданата левого эллипса
        self.x1 = x_pos
        # координата правого эллипса
        self.x2 = self.x1 + section_len
        # угол шва
        self.weld_angle = section_stat['weld_angle']
        self.section_len = section_len
        self.section_stat = section_stat

        # закрашиваем секции
        if self.isfirst is True:
            self.color_section(y_pos=y_pos, d_mode="123", f_color=self.f_color)
        else:
            self.color_section(y_pos=y_pos, d_mode="23", f_color=self.f_color)

        # эллипсы

        if self.isfirst is True:
            # left ellipse
            self.ellipse(x_pos=self.x1, y_pos=self.y_pos, dotted=False)
            # right ellipse
            self.ellipse(x_pos=self.x2, y_pos=self.y_pos, dotted=True)
        else:
            # left ellipse
            # не рисуем первый эллипс начиная со второго
            # ellipse(el_len=el_len, el_diam=el_diam, x_pos=x1, y_pos=y_pos, dotted=True)
            # right ellipse
            self.ellipse(x_pos=self.x2, y_pos=self.y_pos, dotted=True)

        # up line
        self.line(x1=self.x1, y1=self.y_pos, x2=self.x1 + self.section_len, y2=self.y_pos)
        # dwn line
        self.line(x1=self.x1, y1=self.y_pos + self.el_diam * 2, x2=self.x1 + self.section_len,
                  y2=self.y_pos + self.el_diam * 2)

        # продольный шов
        if self.weld_angle > 180:
            is_dotted = True
        else:
            is_dotted = False
        x_weld, y_weld = self.position_on_ellipse(self.weld_angle, self.x1, self.y_pos)
        self.line(x1=x_weld, y1=y_weld, x2=x_weld + self.section_len, y2=y_weld, dotted=is_dotted)

        if self.isfirst:
            self.write_text(x1=self.x1 - 80, y1=self.el_diam + self.y_pos - 75, text='Номер секции', align='left')
            self.write_text(x1=self.x1 - 80, y1=self.el_diam + self.y_pos - 60, text='Длина секции', align='left')
            self.write_text(x1=self.x1 - 80, y1=self.el_diam + self.y_pos - 45, text='Т.ст.', align='left')
            self.write_text(x1=self.x1 - 80, y1=self.el_diam + self.y_pos - 30, text='Угол', align='left')
            self.write_text(x1=self.x1 - 80, y1=self.y_pos + self.el_diam * 2 + 15, text='Дист.,м', align='left')

        self.write_text(x1=self.x1 + self.section_len / 2, y1=self.el_diam + self.y_pos - 75,
                        text=self.section_stat['joint_number'], align='center')
        self.write_text(x1=self.x1 + self.section_len / 2, y1=self.el_diam + self.y_pos - 60,
                        text=str(self.section_stat['joint_length']),
                        align='center')
        self.write_text(x1=self.x1 + self.section_len / 2, y1=self.el_diam + self.y_pos - 45,
                        text=str(self.section_stat['wt']), align='center')
        self.write_text(x1=self.x1 + self.section_len / 2, y1=self.el_diam + self.y_pos - 30,
                        text=str(self.section_stat['weld_angle']),
                        align='center')
        self.write_text(x1=self.x1, y1=self.y_pos + self.el_diam * 2 + 15,
                        text='{:.1f}'.format(self.section_stat['dist']), align='center')

        for i in range(50):
            us = random.randrange(0, self.section_len)
            fea_len = random.randrange(2, 10)
            fea_wid = random.randrange(5, 10)
            orient = random.randrange(0, 50)
            cl = random.randrange(1, 3)
            self.ml_rect(us=us, fea_len=fea_len, fea_wid=fea_wid, orient=orient, y_pos=self.y_pos,
                         f_color=cl)

    def position_on_ellipse(self, angle, x_pos, y_pos):
        # коодинаты точки на эллипсе

        dev = 360 / (2 * math.pi)
        x_pos1 = x_pos + self.el_len * math.cos((angle - 90) / dev)
        y_pos1 = y_pos + self.el_diam * math.sin((angle - 90) / dev) + self.el_diam

        return x_pos1, y_pos1

    def ellipse(self, x_pos=None, y_pos=None, dotted=None):

        # myturtle.up()

        if x_pos is None:
            x_pos = 0
        if y_pos is None:
            y_pos = 0
        if dotted is None:
            dotted = False

        step = 0
        # We are multiplying by 0.875 because for making a complete ellipse we are plotting 315 pts according
        # to our parametric angle value
        # Converting radian to degrees.
        for i in range(360):

            # количество пропусков для пунктира
            dots_skip = 10
            if i % (dots_skip * 2) == 0:
                step = dots_skip * 2
            if i == 0:
                self.myturtle.up()
            else:
                if self.myturtle.pen()['pendown'] is False:
                    self.my_dwn()
                # myturtle.down()

            # пунктирка для задней половины эллипса
            if step > dots_skip and (180 < i < 359) and dotted is True:
                if self.myturtle.pen()['pendown'] is True:
                    self.my_up()
                self.myturtle.goto(self.position_on_ellipse(i, x_pos, y_pos))
                step -= 1
            # обычная рисовка эллипаса
            else:
                self.myturtle.goto(self.position_on_ellipse(i, x_pos, y_pos))

    def my_dwn(self):
        self.myturtle.down()
        self.DWN += 1

    def my_up(self):
        self.myturtle.up()
        self.UP += 1

        # пишем текст над секциями

    def write_text(self, x1, y1, text, align):
        if self.myturtle.pen()['pendown'] is True:
            self.my_up()
        self.myturtle.goto(x1, y1)
        self.myturtle.write(arg=text, move=False, align=align, font=('Verdana', 7, 'normal'))

        # линия по 2м точкам

    def line(self, x1, y1, x2, y2, dotted=False):
        self.myturtle.up()
        self.myturtle.goto(x1, y1)
        self.myturtle.down()
        if dotted is False:
            self.myturtle.goto(x2, y2)
        else:
            len_dots = self.section_len
            while len_dots > 0:
                self.myturtle.forward(5)
                self.myturtle.up()
                self.myturtle.forward(5)
                self.myturtle.down()
                len_dots -= 10

    def ml_rect(self, us, fea_len, fea_wid, orient, y_pos, f_color):

        cl = f_color

        if cl == 1:
            cl = "#FF3300"
        else:
            cl = "#0033CC"

        self.myturtle.fillcolor(cl)

        up_left = (self.x1 + us, y_pos + orient)
        up_right = (self.x1 + us + fea_len, y_pos + orient)
        dwn_left = (self.x1 + us, y_pos + fea_wid + orient)
        dwn_right = (self.x1 + us + fea_len, y_pos + fea_wid + orient)

        self.myturtle.setposition(up_left)
        self.myturtle.begin_fill()
        # self.myturtle.down()
        self.myturtle.setposition(up_right)
        self.myturtle.setposition(dwn_right)
        self.myturtle.setposition(dwn_left)
        self.myturtle.setposition(up_left)
        # for i in range(y_pos + orient,y_pos + fea_wid + orient):
        #     myturtle.setposition(self..position_on_ellipse(i, x1 + us + fea_len, y_pos + orient, el_len, el_diam))
        # for i in range(y_pos + fea_wid + orient,y_pos + orient):
        #     myturtle.setposition(self..position_on_ellipse(i, x1 + us, y_pos + fea_wid + orient, el_len, el_diam))
        self.myturtle.end_fill()
        self.myturtle.up()

    def color_section(self, y_pos, d_mode=None, f_color=None):
        # закраска секции

        self.myturtle.up()
        # 123 - 3 зоны у секции под рисовку
        if d_mode is None:
            d_mode = '123'
        if f_color is None:
            f_color = '#000000'

        # RGB(140, 140, 255) / #8C8CFF ' синий (<20)
        # RGB(140, 255, 140) / #8CFF8C ' зеленый (20-30)
        # RGB(255, 255, 140) / #FFFF8C ' желтый (30-40)
        # RGB(255, 200, 200) / #FFC8C8 ' розовый (40-50)
        # RGB(255, 100, 100) / #FF6464 ' красный (>50)

        up_left = (self.x1 + 1, y_pos)
        up_rigth = (self.x1 - 1 + self.section_len, y_pos)
        dwn_left = (self.x1 + 1, y_pos + self.el_diam * 2)
        # dwn_rigth = (self.x1 - 1 + self.section_len, y_pos + self.el_diam * 2)

        self.myturtle.fillcolor(f_color)

        if d_mode == '123':
            self.myturtle.setposition(up_left)
            self.myturtle.begin_fill()
            self.myturtle.setposition(up_rigth)
            for i in range(180):
                self.myturtle.setposition(self.position_on_ellipse(i, self.x2, y_pos))
            self.myturtle.setposition(dwn_left)
            for i in range(180, 360):
                self.myturtle.setposition(
                    self.position_on_ellipse(i, self.x1 + 1, y_pos))
            self.myturtle.end_fill()
        elif d_mode == '23':
            self.myturtle.setposition(up_left)
            self.myturtle.begin_fill()
            self.myturtle.setposition(up_rigth)
            for i in range(180):
                self.myturtle.setposition(self.position_on_ellipse(i, self.x2, y_pos))
            self.myturtle.setposition(dwn_left)
            for i in range(180, 0, -1):
                self.myturtle.setposition(
                    self.position_on_ellipse(i, self.x1 + 1, y_pos))
            self.myturtle.end_fill()


def main():
    pipe_section = PyScheme()

    x_start = 80
    x = x_start
    y = 50
    len_total = 0
    first = True
    turtle.colormode(255)
    x1 = 0
    x2 = 0

    sections = []

    section_stat = {'weld_angle': 123, 'dist': 125874.475, 'joint_number': 0, 'wt': 11.1, 'joint_length': 12.13}
    x1 = time()
    for i in range(5):
        while len_total < 900:
            section_len = random.randrange(25, 200)
            section_stat['joint_length'] = round(section_len / 16.6, 1)
            section_stat['weld_angle'] = random.randrange(0, 359)

            tmp_element = [x, y, section_len, first, section_stat]
            sections.append(tmp_element)

            pipe_section.section_draw(x_pos=x, y_pos=y, section_len=section_len, isfirst=first,
                                       section_stat=section_stat)

            section_stat['joint_number'] += 10
            section_stat['dist'] += section_stat['joint_length']

            len_total += section_len
            x += section_len
            first = False
        # сдвиг вниз на одну строчку - 160
        y += 160
        # возврат в начало координат
        x = x_start
        len_total = 0
        first = True

    x2 = time()

    print(x2 - x1)

    # turtle.update()

    turtle.exitonclick()


if __name__ == "__main__":
    main()
