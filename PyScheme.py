import random
from turtle import Screen, Turtle
import turtle
import colorsys
import math

myturtle = turtle.Turtle()
turtle.tracer(0, 0)
#turtle.tracer(False)
turtle.speed('fastest')

WIDTH, HEIGHT = 1200, 1000
screen = Screen()
screen.setup(WIDTH + 4, HEIGHT + 8)  # fudge factors due to window borders & title bar

# screen.setworldcoordinates(0, 0, WIDTH, HEIGHT)

myturtle.pensize(1)

def pipe_section(x_pos, y_pos, len, dotted, section_stat, endcap=True):
    # Функция построения секции, основана на функция эллипса и линии

    # коорданата левого эллипса
    x1 = x_pos
    # координата правого эллипса
    x2 = x1 + len
    # диаметр эллипса - 30
    el_diam = 30
    # ширина эллипса - 8
    el_len = 8

    # угол (при параметрике используется 318)
    converted_angle = 360 * 0.875
    # оригинальный угол (адаптированный)
    weld_angle_original = section_stat['weld_angle'] * 0.875
    # угол со сдвигом на 90 (отрисовка ведется с 90 градусув против часовой стрелки
    weld_angle = abs((section_stat['weld_angle'] - 90) - 360) * 0.875

    def ellipse(el_len, el_diam, x_pos=None, y_pos=None, dotted=None, weld_angle=0, endcap=True):

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
        for i in range(int(converted_angle) + 1):

            # количество пропусков для пунктира
            dots_skip = 5
            if i % (dots_skip * 2) == 0:
                step = dots_skip * 2
            if i == 0:
                myturtle.up()
            else:
                myturtle.down()

            # пунктирка для задней половины эллипса
            if step > dots_skip and (i > 79 and i < 237) and dotted == True:
                myturtle.up()
                myturtle.setposition(x_pos + el_len * math.cos(i / 50), y_pos + el_diam * math.sin(i / 50))
                step -= 1
                myturtle.down()
            # обычная рисовка эллипаса
            else:
                myturtle.setposition(x_pos + el_len * math.cos(i / 50), y_pos + el_diam * math.sin(i / 50))
                myturtle.up()

    def write_text(x1, y1, text):
        myturtle.up()
        myturtle.setposition(x1, y1)
        myturtle.write(arg=text, move=False, align='center', font='Verdana 7')
        myturtle.down()

    # линия по 2м точкам
    def line(x1, y1, x2, y2, dotted=False):
        myturtle.up()
        myturtle.setposition(x1, y1)

        myturtle.down()
        if dotted == False:
            myturtle.setposition(x2, y2)
        else:
            len_dots = len
            while len_dots > 0:
                myturtle.forward(5)
                myturtle.up()
                myturtle.forward(5)
                myturtle.down()
                len_dots -= 10

    ellipse(el_len=el_len, el_diam=el_diam, x_pos=x1, y_pos=y_pos, dotted=dotted, weld_angle=weld_angle)
    ellipse(el_len=el_len, el_diam=el_diam, x_pos=x2, y_pos=y_pos, dotted=True, weld_angle=weld_angle, endcap=endcap)
    line(x1=x1, y1=el_diam + y_pos, x2=x1 + len, y2=el_diam + y_pos)
    line(x1=x1, y1=-el_diam + y_pos, x2=x1 + len, y2=-el_diam + y_pos)

    # продольный шов
    x_weld = x_pos + el_len * math.cos(weld_angle / 50)
    y_weld = y_pos + el_diam * math.sin(weld_angle / 50)
    # если в задней полусфере то пунктиром
    if weld_angle_original > converted_angle / 2:
        is_dotted = True
    else:
        is_dotted = False

    write_text(x1=x1, y1=el_diam + y_pos + 45, text=section_stat['joint_number'])
    write_text(x1=x1, y1=el_diam + y_pos + 30, text=str(section_stat['joint_length']))
    write_text(x1=x1, y1=el_diam + y_pos + 15, text=str(section_stat['wt']))
    write_text(x1=x1, y1=el_diam + y_pos, text=str(section_stat['weld_angle']))

    write_text(x1=x1, y1=-el_diam + y_pos-15, text='{:.1f}'.format(section_stat['dist']))

    line(x1=x_weld, y1=y_weld, x2=x_weld + len, y2=y_weld, dotted=is_dotted)

def main():

    x = -550
    y = 350
    len_total = 0
    first = True

    section_stat = {'weld_angle': 123, 'dist': 0, 'joint_number': 0, 'wt': 11.1,'joint_length':12.13}

    for i in range(6):
        while len_total < 900:
            len = random.randrange(25, 200)
            section_stat['joint_length'] = round(len/16.6,1)
            section_stat['weld_angle'] = random.randrange(90, 270)
            section_stat['joint_number']+=10
            section_stat['dist'] += section_stat['joint_length']

            if first == True:
                pipe_section(x_pos=x, y_pos=y, len=len, dotted=False, endcap=False, section_stat=section_stat)
            else:
                pipe_section(x_pos=x, y_pos=y, len=len, dotted=True, endcap=False, section_stat=section_stat)
            len_total += len
            x += len
            first = False
        # сдвиг вниз на одну строчку - 160
        y -= 160
        # возврат в начало координат
        x = -550
        len_total = 0
        first = True

    #screen.update()
    turtle.tracer(True)

    myturtle.hideturtle()
    turtle.hideturtle()

    turtle.exitonclick()
    turtle.update()



if __name__ == "__main__":
    main()
