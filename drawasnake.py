import turtle


def python(factor):
    r1 = 270 * factor
    turtle.pencolor(0, 0.3, 0.4)
    turtle.penup()
    turtle.right(90)
    turtle.forward(r1)
    turtle.left(90)
    turtle.pendown()
    turtle.fillcolor(0, 0.3, 0.4)
    turtle.begin_fill()
    turtle.circle(r1)
    turtle.end_fill()
    # 画背景
    turtle.left(90)
    turtle.forward(r1)
    turtle.right(90)
    # 归位

    def snake(col):
        d = 5 * factor
        r2 = 45 * factor
        r3 = 20 * factor
        turtle.pencolor(col)
        turtle.penup()
        turtle.right(90)
        turtle.forward(d)
        turtle.left(90)
        turtle.pendown()
        turtle.fillcolor(col)
        turtle.begin_fill()
        turtle.forward(r2 + d)
        turtle.circle(r2, 90)
        turtle.forward(r2)
        turtle.right(90)
        turtle.forward(r2)
        turtle.right(-135)
        turtle.circle(2.828 * r2, -90)
        turtle.left(135)
        turtle.forward(3 * r2)
        turtle.left(90)
        turtle.forward(2 * d)
        turtle.left(90)
        turtle.forward(2 * r2)
        turtle.right(90)
        turtle.forward(r2 + r3 - 2 * d)
        turtle.left(135)

        turtle.circle(2.828 * r2, -90)
        turtle.left(135)
        turtle.forward(r3 + 2 * r2)
        turtle.left(180)
        turtle.circle(r2, -90)
        turtle.backward(r2)
        turtle.end_fill()
        # 蛇身
        turtle.penup()
        turtle.backward(r2)
        turtle.left(90)
        turtle.forward(3 * r2 - r3)
        turtle.right(90)
        turtle.pendown()
        turtle.fillcolor(0, 0.3, 0.4)
        turtle.begin_fill()
        turtle.circle(r3)
        turtle.end_fill()
        # 蛇眼
        turtle.penup()
        turtle.right(90)
        turtle.forward(3 * r2 - r3 + d)
        turtle.left(90)
        turtle.forward(r2 + d)
        turtle.pendown()
        # 归位

    snake('orange')
    snake('white')


python(0.8)

turtle.goto(300, 300)
python(0.4)

turtle.hideturtle()
turtle.exitonclick()
