import turtle
import side_defs
from turtle import Screen

turtle.delay(0)

#turtle.tracer(0, 0)


def ellipse(el_len, el_diam, x_pos=None, y_pos=None, dotted=None):

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
    for i in range(361):

        print(myturtle.speed())

        # количество пропусков для пунктира
        dots_skip = 5
        if i % (dots_skip * 2) == 0:
            step = dots_skip * 2
        if i == 0:
            myturtle.up()
        else:
            myturtle.down()

        # пунктирка для задней половины эллипса
        # if step > dots_skip and (180 < i < 360) and dotted == True:
        #     myturtle.up()
        #     myturtle.setposition(position_on_ellipse(i, x_pos, y_pos, el_len, el_diam))
        #     step -= 1
        #     myturtle.down()
        # # обычная рисовка эллипаса
        # else:
        myturtle.goto(side_defs.position_on_ellipse(i, x_pos, y_pos, el_len, el_diam))
        #myturtle.up()



if __name__ == '__main__':

    myturtle = turtle.Turtle()
    myturtle.pensize(2)
    myturtle.ht()

    WIDTH, HEIGHT = 1200, 1000
    screen = Screen()
    screen.setup(WIDTH + 5, HEIGHT + 5)  # fudge factors due to window borders & title bar
    screen.setworldcoordinates(0, HEIGHT, WIDTH, 0)

    myturtle.speed(0)


    el_len=50
    el_diam=200
    x_pos=500
    y_pos=100

    ellipse(el_len=el_len, el_diam=el_diam, x_pos=x_pos, y_pos=y_pos, dotted=False)

    myturtle.up()
    myturtle.setposition(side_defs.position_on_ellipse(angle=90, x_pos=x_pos, y_pos=y_pos, el_len=el_len, el_diam=el_diam))
    myturtle.down()
    myturtle.dot()
    myturtle.write("90")

    myturtle.setposition(side_defs.position_on_ellipse(angle=270, x_pos=x_pos, y_pos=y_pos, el_len=el_len, el_diam=el_diam))
    myturtle.down()
    myturtle.dot()
    myturtle.up()

    myturtle.setposition(side_defs.position_on_ellipse(angle=0, x_pos=x_pos, y_pos=y_pos, el_len=el_len, el_diam=el_diam))
    myturtle.down()
    myturtle.dot()
    myturtle.write("0")

    myturtle.setposition(side_defs.position_on_ellipse(angle=180, x_pos=x_pos, y_pos=y_pos, el_len=el_len, el_diam=el_diam))
    myturtle.down()
    myturtle.dot()
    myturtle.up()

    turtle.exitonclick()
