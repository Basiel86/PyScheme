import math


def position_on_ellipse(angle, x_pos, y_pos, el_len, el_diam):
    # коодинаты точки на эллипсе

    dev = 360 / (2 * math.pi)
    x_pos1 = x_pos + el_len * math.cos((angle - 90) / dev)
    y_pos1 = y_pos + el_diam * math.sin((angle - 90) / dev) + el_diam

    return x_pos1, y_pos1
