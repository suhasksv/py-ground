"""
def rectangle(horizontal, verticle, color):
    t.pendown()
    t.pensize(1)
    t.color(color)
    t.begin_fill()
"""

import turtle as t
import time


def rectangle(horizontal, vertical, color):
    t.pendown()
    t.pensize(2)
    t.color(color)
    t.begin_to_fill()
    for i in range(1, 3):
        t.forward(horizontal)
        t.right(90)
        t.forward(vertical)
        t.right(90)


t.end_fill()
t.pendown()
time.sleep(3.0)
