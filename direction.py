import turtle

rightBool = [False]
leftBool = [False]
upBool = [False]
downBool = [False]

win = turtle.Screen()
win.setup(width=720, height=720)
win.bgcolor("black")
win.tracer(0)

block = turtle.Turtle()
block.shape("square")
block.color("white")
block.penup()
blockdx = 0.05
blockdy = 0.05

def setRight():
    rightBool[0] = True
def setLeft():
    leftBool[0] = True
def setUp():
    upBool[0] = True
def setDown():
    downBool[0] = True

def unRight():
    rightBool[0] = False
def unLeft():
    leftBool[0] = False
def unUp():
    upBool[0] = False
def unDown():
    downBool[0] = False

def right():
    x = block.xcor()
    x += blockdx
    block.setx(x)
def left():
    x = block.xcor()
    x -= blockdx
    block.setx(x)
def up():
    y = block.ycor()
    y += blockdy
    block.sety(y)
def down():
    y = block.ycor()
    y -= blockdy
    block.sety(y)
win.listen()
win.onkeypress(setRight, "d")
win.onkeyrelease(unRight, "d")
win.onkeypress(setLeft, "a")
win.onkeyrelease(unLeft, "a")
win.onkeypress(setUp, "w")
win.onkeyrelease(unUp, "w")
win.onkeypress(setDown, "s")
win.onkeyrelease(unDown, "s")



while True:
    win.update()
    if rightBool[0] == True:
        right()
    if leftBool[0] == True:
        left()
    if upBool[0] == True:
        up()
    if downBool[0] == True:
        down()
