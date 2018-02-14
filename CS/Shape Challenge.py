#I do realize that this is not the most effective/efficient way of doing it.
import turtle
from random import randint

length = 0
x = 0
y = 0

def line(l, direction):
    global length
    if direction == 1:
        turtle.seth(0)
    elif direction == 2:
        turtle.seth(-90)
    elif direction == 3:
        turtle.seth(-180)
    elif direction == 4:
        turtle.seth(90)
    turtle.forward(l)
    length = l
    return length
    
def curve(l, degree, direction):
    global length
    turtle.seth(direction)
    for i in range(l):
        turtle.forward(degree)
        if direction >= 0:
            turtle.right(1)
        elif direction < 0:
            turtle.left(1)
    length = l
    return length
    
def diagonal(l, direction):
    global length
    turtle.seth(direction)
    turtle.forward(l)
    length = l
    return length

def space(l):
    turtle.up()
    turtle.forward(l)
    turtle.down()

def back():
    turtle.up()
    turtle.backward(length)
    turtle.down()

def reset():
    global x
    global y
    turtle.up()
    turtle.goto(x, y)
    turtle.down()
    turtle.seth(0)
    space(60)

def start_position():
    global x
    global y
    x = turtle.xcor()
    y = turtle.ycor()
    return x, y 

    

#-----------------------------------------------------------------------------------------------------------------------------------\

def A():
    space(30)
    start_position()
    diagonal(120, -70)
    back()
    diagonal(120, -110)
    back()
    turtle.seth(-90)
    space(82)
    turtle.seth(0)
    turtle.backward(30)
    line(60, 1)
    reset()
    space(50)

def B():
    start_position()
    line(114, 2)
    back()
    line(30, 1)
    curve(181, 0.5, 0)
    line(30, 3)
    back()
    curve(181, 0.5, 0)
    turtle.forward(30)
    reset()
    space(60)

def C():
    space(60)
    start_position()
    turtle.backward(30)
    curve(180, 1, -180)
    turtle.forward(30)
    reset()

def D():
    start_position()
    line(114, 2)
    back()
    line(30, 1)
    curve(180, 1, 0)
    turtle.forward(30)
    reset()
    space(90)

def E():
    line(114, 2)
    back()
    line(40, 1)
    start_position()
    back()
    line(57, 2)
    line(40, 1)
    back()
    line(57, 2)
    line(40, 1)
    reset()

def F():
    line(114, 2)
    back()
    line(40, 1)
    start_position()
    back()
    line(57, 2)
    line(40, 1)
    reset()

def G():
    space(60)
    start_position()
    turtle.backward(30)
    curve(180, 1, -180)
    turtle.forward(30)
    line(50, 4)
    line(30, 3)
    reset()

def H():
    line(114, 2)
    line(57, 4)
    line(60, 1)
    line(57, 4)
    start_position()
    line(114, 2)
    reset()

def I():
    line(40, 1)
    start_position()
    line(20, 3)
    line(114, 2)
    line(20, 3)
    line(40, 1)
    reset()

def J():
    line(40, 1)
    start_position()
    line(85.5, 2)
    for i in range(181):
        turtle.forward(0.5)
        turtle.right(1)
    reset()

def K():
    start_position()
    line(57, 2)
    turtle.seth(50)
    turtle.forward(70)
    turtle.backward(50)
    turtle.seth(-55)
    turtle.forward(87)
    turtle.backward(87)
    turtle.seth(50)
    turtle.backward(20)
    line(57, 2)
    reset()
    space(50)

def L():
    start_position()
    line(114, 2)
    line(60, 1)
    reset()
    space(30)

def M():
    line(114, 2)
    back()
    diagonal(90, -60)
    diagonal(90, 60)
    start_position()
    line(114, 2)
    reset()

def N():
    line(114, 2)
    back()
    diagonal(130, -60)
    line(114, 4)
    start_position()
    reset()

def O():
    start_position()
    curve(91, 0.5, -180)
    line(57, 2)
    curve(181, 0.5, -90)
    line(57, 4)
    curve(91, 0.5, -270)
    reset()
    space(30)

def P():
    start_position()
    line(114, 2)
    back()
    line(30, 1)
    curve(181, 0.5, 0)
    line(30, 3)
    reset()
    space(60)


def Q():
    start_position()
    curve(91, 0.5, -180)
    line(57, 2)
    curve(181, 0.5, -90)
    line(57, 4)
    curve(91, 0.5, -270)
    turtle.up()
    turtle.seth(-90)
    turtle.forward(100)
    turtle.down()
    diagonal(30, -45)
    reset()
    space(30)

def R():
    line(114, 2)
    back()
    line(30, 1)
    start_position()
    curve(181, 0.5, 0)
    line(30, 3)
    back()
    diagonal(70, -50)
    reset()
    space(30)


def S():
    space(30)
    line(30, 1)
    start_position()
    line(60, 3)
    curve(181, 0.5, -180)
    line(30, 1)
    curve(181, 0.5, 0)
    line(60, 3)
    reset()

def T():
    line(30, 1)
    start_position()
    back()
    line(30, 3)
    back()
    line(114, 2)
    reset()

def U():
    line(88.5, 2)
    curve(181, 0.5, -90)
    line(88.5, 4)
    start_position()
    reset()

def V():
    diagonal(120, -70)
    diagonal(120, 70)
    start_position()
    reset()

def W():
    line(114, 2)
    diagonal(90, 60)
    diagonal(90, -60)
    line(114, 4)
    start_position()
    reset()

def X():
    diagonal(120, -70)
    diagonal(60, 110)
    diagonal(60, 70)
    start_position()
    back()
    diagonal(60, -110)
    reset()

def Y():
    diagonal(65, -60)
    diagonal(65, 60)
    start_position()
    back()
    line(58, 2)
    reset()

def Z():
    line(60, 1)
    start_position()
    diagonal(130, -118)
    line(60, 1)
    reset()



#-----------------------------------------------------------------------------------------------------------------------------------\

color = ["red", "blue", "black", "green", "yellow", "purple"]

def name_input():
    while True:
        name = raw_input("Enter the Name: ")
        list(name)
        print(name)
        turtle.reset()
        turtle.speed("fastest")
        turtle.pensize(10)
        space(-(len(name)/2*100))
        for i in name:
            shape_color = color[randint(0, len(color)-1)]
            turtle.color(shape_color)
            if i == "A" or i == "a":
                A()
            elif i == "B" or i == "b":
                B()
            elif i == "C" or i == "c":
                C()
            elif i == "D" or i == "d":
                D()
            elif i == "E" or i == "e":
                E()
            elif i == "F" or i == "f":
                F()
            elif i == "G" or i == "g":
                G()
            elif i == "H" or i == "h":
                H()
            elif i == "I" or i == "i":
                I()
            elif i == "J" or i == "j":
                J()
            elif i == "K" or i == "k":
                K()
            elif i == "L" or i == "l":
                L()
            elif i == "M" or i == "m":
                M()
            elif i == "N" or i == "n":
                N()
            elif i == "O" or i == "o":
                O()
            elif i == "P" or i == "p":
                P()
            elif i == "Q" or i == "q":
                Q()
            elif i == "R" or i == "r":
                R()
            elif i == "S" or i == "s":
                S()
            elif i == "T" or i == "t":
                T()
            elif i == "U" or i == "u":
                U()
            elif i == "V" or i == "v":
                V()
            elif i == "W" or i == "w":
                W()
            elif i == "X" or i == "x":
                X()
            elif i == "Y" or i == "y":
                Y()
            elif i == "Z" or i == "z":
                Z()


#-----------------------------------------------------------------------------------------------------------------------------------\
        

name_input()



turtle.done()
