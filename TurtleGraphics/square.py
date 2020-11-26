import time
import turtle as t

t.pendown()
t.pensize(1)
t.color("blue")
t.begin_fill()
for i in range(2):
	t.forward(100)
	t.right(90)
	t.forward(100)
	t.right(90)
t.end_fill()
t.penup()

time.sleep(10)

