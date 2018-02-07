import turtle

def draw_square(some_turtle):
    for x in range(1, 5):
        some_turtle.forward(100)
        some_turtle.right(90)

def draw_triangle(some_turtle):
    for x in range(1, 4):
        some_turtle.forward(70)
        some_turtle.right(120)

def draw_art():
    window = turtle.Screen()
    window.bgcolor("red")

    brad = turtle.Turtle()
    brad.shape("turtle")
    brad.color("green")
    brad.speed(10)
    for x in range(1, 37):
        brad.right(10)
        draw_square(brad)

    fred = turtle.Turtle()
    fred.shape("classic")
    fred.color("yellow")
    fred.speed(10)
    for x in range(1, 37):
        fred.right(10)
        draw_triangle(fred)
        
    angie = turtle.Turtle()
    angie.shape("arrow")
    angie.color("blue")
    angie.up()
    angie.sety(-150)
    angie.position()
    angie.down()
    angie.circle(150)

    window.exitonclick()

draw_art()
