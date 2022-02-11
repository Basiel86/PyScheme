import random
import turtle
from turtle import *
import side_defs

turtle.tracer(0)
turtle.delay(0)

DWN = 0
UP = 0

WIDTH, HEIGHT = 1200, 1000
screen = Screen()
screen.setup(WIDTH + 5, HEIGHT + 5)  # fudge factors due to window borders & title bar
screen.setworldcoordinates(0, HEIGHT, WIDTH, 0)

myturtle = turtle.Turtle()
myturtle.hideturtle()
myturtle.pensize(1)
myturtle.speed(0)


def my_dwn():
    global DWN
    myturtle.down()
    DWN += 1


def my_up():
    global UP
    myturtle.up()
    UP += 1


def pipe_section(x_pos, y_pos, section_len, section_stat, isfirst=False):
    # Функция построения секции, основана на функция эллипса и линии

    # коорданата левого эллипса
    x1 = x_pos
    # координата правого эллипса
    x2 = x1 + section_len
    # диаметр эллипса - 30
    el_diam = 30
    # ширина эллипса - 8
    el_len = 8

    # угол шва
    weld_angle = section_stat['weld_angle']

    def ellipse(el_len, el_diam, x_pos=None, y_pos=None, dotted=None):

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
                myturtle.up()
            else:
                if myturtle.pen()['pendown'] is False:
                    my_dwn()
                # myturtle.down()

            # пунктирка для задней половины эллипса
            if step > dots_skip and (180 < i < 359) and dotted is True:
                if myturtle.pen()['pendown'] is True:
                    my_up()
                myturtle.goto(side_defs.position_on_ellipse(i, x_pos, y_pos, el_len, el_diam))
                step -= 1
            # обычная рисовка эллипаса
            else:
                myturtle.goto(side_defs.position_on_ellipse(i, x_pos, y_pos, el_len, el_diam))

    # пишем текст над секциями
    def write_text(x1, y1, text, align):
        if myturtle.pen()['pendown'] is True:
            my_up()
        myturtle.goto(x1, y1)
        myturtle.write(arg=text, move=False, align=align, font=('Verdana', 7, 'normal'))

    # линия по 2м точкам
    def line(x1, y1, x2, y2, dotted=False):
        myturtle.up()
        myturtle.goto(x1, y1)
        myturtle.down()
        if dotted is False:
            myturtle.goto(x2, y2)
        else:
            len_dots = section_len
            while len_dots > 0:
                myturtle.forward(5)
                myturtle.up()
                myturtle.forward(5)
                myturtle.down()
                len_dots -= 10

    def ml_rect(us, fea_len, fea_wid, orient, el_len, el_diam, y_pos,color):

        cl=color

        if cl==1:
            cl="#FF3300"
        else:
            cl="#0033CC"

        myturtle.fillcolor(cl)

        up_left = (x1 + us, y_pos + orient)
        up_rigth = (x1 + us + fea_len, y_pos + orient)
        dwn_left = (x1 + us, y_pos + fea_wid + orient)
        dwn_right = (x1 + us + fea_len, y_pos + fea_wid + orient)

        myturtle.setposition(up_left)
        myturtle.begin_fill()
        # myturtle.down()
        myturtle.setposition(up_rigth)
        myturtle.setposition(dwn_right)
        myturtle.setposition(dwn_left)
        myturtle.setposition(up_left)
        # for i in range(y_pos + orient,y_pos + fea_wid + orient):
        #     myturtle.setposition(side_defs.position_on_ellipse(i, x1 + us + fea_len, y_pos + orient, el_len, el_diam))
        # for i in range(y_pos + fea_wid + orient,y_pos + orient):
        #     myturtle.setposition(side_defs.position_on_ellipse(i, x1 + us, y_pos + fea_wid + orient, el_len, el_diam))
        myturtle.end_fill()
        myturtle.up()

    def color_section(el_len, el_diam, y_pos, mode=None, f_color=None):
        # закраска секции

        myturtle.up()
        # 123 - 3 зоны у секции под рисовку
        if mode is None:
            mode = '123'
        if f_color is None:
            f_color = '#000000'

        # RGB(140, 140, 255) / #8C8CFF ' синий (<20)
        # RGB(140, 255, 140) / #8CFF8C ' зеленый (20-30)
        # RGB(255, 255, 140) / #FFFF8C ' желтый (30-40)
        # RGB(255, 200, 200) / #FFC8C8 ' розовый (40-50)
        # RGB(255, 100, 100) / #FF6464 ' красный (>50)

        up_left = (x1 + 1, y_pos)
        up_rigth = (x1 - 1 + section_len, y_pos)
        dwn_left = (x1 + 1, y_pos + el_diam * 2)
        dwn_rigth = (x1 - 1 + section_len, y_pos + el_diam * 2)

        myturtle.fillcolor(f_color)

        if mode == '123':
            myturtle.setposition(up_left)
            myturtle.begin_fill()
            myturtle.setposition(up_rigth)
            for i in range(180):
                myturtle.setposition(side_defs.position_on_ellipse(i, x2, y_pos, el_len, el_diam))
            myturtle.setposition(dwn_left)
            for i in range(180, 360):
                myturtle.setposition(side_defs.position_on_ellipse(i, x1 + 1, y_pos, el_len, el_diam))
            myturtle.end_fill()
        elif mode == '23':
            myturtle.setposition(up_left)
            myturtle.begin_fill()
            myturtle.setposition(up_rigth)
            for i in range(180):
                myturtle.setposition(side_defs.position_on_ellipse(i, x2, y_pos, el_len, el_diam))
            myturtle.setposition(dwn_left)
            for i in range(180, 0, -1):
                myturtle.setposition(side_defs.position_on_ellipse(i, x1 + 1, y_pos, el_len, el_diam))
            myturtle.end_fill()

    scheme_colors = {'blue': '#8C8CFF', 'green': '#8CFF8C', 'yellow': '#FFFF8C', 'pink': '#FFC8C8', 'red': '#FF6464',
                     'white': '#FFFFFF'}
    scheme_colors_index = ['blue', 'green', 'yellow', 'pink', 'red', 'white']

    f_color = scheme_colors[scheme_colors_index[random.randrange(0, len(scheme_colors_index))]]

    # закрашиваем секции
    if isfirst is True:
        color_section(el_len=el_len, el_diam=el_diam, y_pos=y_pos, mode="123", f_color=f_color)
    else:
        color_section(el_len=el_len, el_diam=el_diam, y_pos=y_pos, mode="23", f_color=f_color)

    # эллипсы

    if isfirst is True:
        # left ellipse
        ellipse(el_len=el_len, el_diam=el_diam, x_pos=x1, y_pos=y_pos, dotted=False)
        # right ellipse
        ellipse(el_len=el_len, el_diam=el_diam, x_pos=x2, y_pos=y_pos, dotted=True)
    else:
        # left ellipse
        # не рисуем первый эллипс начиная со второго
        # ellipse(el_len=el_len, el_diam=el_diam, x_pos=x1, y_pos=y_pos, dotted=True)
        # right ellipse
        ellipse(el_len=el_len, el_diam=el_diam, x_pos=x2, y_pos=y_pos, dotted=True)

    # up line
    line(x1=x1, y1=y_pos, x2=x1 + section_len, y2=y_pos)
    # dwn line
    line(x1=x1, y1=y_pos + el_diam * 2, x2=x1 + section_len, y2=y_pos + el_diam * 2)

    # продольный шов
    if weld_angle > 180:
        is_dotted = True
    else:
        is_dotted = False
    x_weld, y_weld = side_defs.position_on_ellipse(weld_angle, x_pos, y_pos, el_len, el_diam)
    line(x1=x_weld, y1=y_weld, x2=x_weld + section_len, y2=y_weld, dotted=is_dotted)

    if isfirst:
        write_text(x1=x1 - 80, y1=el_diam + y_pos - 75, text='Номер секции', align='left')
        write_text(x1=x1 - 80, y1=el_diam + y_pos - 60, text='Длина секции', align='left')
        write_text(x1=x1 - 80, y1=el_diam + y_pos - 45, text='Т.ст.', align='left')
        write_text(x1=x1 - 80, y1=el_diam + y_pos - 30, text='Угол', align='left')
        write_text(x1=x1 - 80, y1=y_pos + el_diam * 2 + 15, text='Дист.,м', align='left')

    write_text(x1=x1 + section_len / 2, y1=el_diam + y_pos - 75, text=section_stat['joint_number'], align='center')
    write_text(x1=x1 + section_len / 2, y1=el_diam + y_pos - 60, text=str(section_stat['joint_length']), align='center')
    write_text(x1=x1 + section_len / 2, y1=el_diam + y_pos - 45, text=str(section_stat['wt']), align='center')
    write_text(x1=x1 + section_len / 2, y1=el_diam + y_pos - 30, text=str(section_stat['weld_angle']), align='center')
    write_text(x1=x1, y1=y_pos + el_diam * 2 + 15, text='{:.1f}'.format(section_stat['dist']), align='center')

    for i in range(20):
        us = random.randrange(0, section_len)
        fea_len = random.randrange(2, 10)
        fea_wid = random.randrange(5, 10)
        orient = random.randrange(0, 50)
        cl = random.randrange(1, 3)
        ml_rect(us=us, fea_len=fea_len, fea_wid=fea_wid, orient=orient, el_len=el_len, el_diam=el_diam, y_pos=y_pos,
                color=cl)


def main():

    x_start = 80
    x = x_start
    y = 50
    len_total = 0
    first = True
    turtle.colormode(255)

    section_stat = {'weld_angle': 123, 'dist': 125874.475, 'joint_number': 0, 'wt': 11.1, 'joint_length': 12.13}

    for i in range(5):
        while len_total < 900:
            section_len = random.randrange(25, 200)
            section_stat['joint_length'] = round(section_len / 16.6, 1)
            section_stat['weld_angle'] = random.randrange(0, 359)

            pipe_section(x_pos=x, y_pos=y, section_len=section_len, isfirst=first,
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

    # turtle.update()

    print(DWN)
    print(UP)

    turtle.exitonclick()


if __name__ == "__main__":
    main()
