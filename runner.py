from tkinter import CENTER
import turtle
import random

class Jump():
    def __init__(self, jumps) -> None:
        self.jumps = jumps

    
    def setJumps(self, num):
        self.jumps = num
    def checkJumps(self, num):
        if self.jumps == num:
            return True
        else:
            return False
    def decreaseJumps(self, num):
        self.jumps -= num
        if self.jumps < 0:
            self.jumps = 0

rightBool = [False]
leftBool = [False]
downBool = [False]
onGround = [False]
inAir = [False]
jumpCount = Jump(2)
jumping = [False]
level = 1

counter = []
# Generate Window
win = turtle.Screen()
win.title("Runner")
win.bgcolor("light blue")
win.setup(width = 720, height = 360)
win.tracer(0)
win.mode()

# Generate Score
score = turtle.Turtle()
score.color("black")
score.hideturtle()
score.penup()
score.goto(-300, 150)
score.write("Level {}".format(level), align = "center", font = ("Courier", 14, "normal"))

# Generate Background
grass = turtle.Turtle()
grass.penup()
grass.shape("square")
grass.color("dark green")
grass.shapesize(stretch_wid=4, stretch_len=40)
grass.goto(0, -135)

turtle.register_shape("clouds2.gif", shape=None)
cloud = turtle.Turtle()
cloud.penup()
cloud.shape("clouds2.gif")
cloud.goto(0, 0)

# Generate Movable Scenary
platform = turtle.Turtle()
platform.penup()
platform.shape("square")
platform.color("brown")
platform.shapesize(stretch_len=4, stretch_wid=1)
a1 = platform.clone()
a2 = platform.clone()
a3 = platform.clone()
a1.goto(-180, 0)
a2.goto(0, 0)
a3.goto(180, 0)
platform.hideturtle()

turtle.addshape("door.gif", shape=None)
door = turtle.Turtle()
door.shape("door.gif")
door.penup()
door.goto(340, 80)

# Create Player
player = turtle.Turtle()
player.speed(0)
player.penup()
player.shape("square")
player.shapesize(stretch_len=1, outline=1)
player.color("black", "white")
player.goto(-340, -75)
playerdx = 0.1
playerdy = 0.05
maxSpeed = 25
turtle.addshape("eye", ((0, 0), (-5, 0)))
eye = turtle.Turtle()
eye.penup()
eye.shape("eye")
eye.color("black")
eyeLeft = eye.clone()
eyeRight = eye.clone()
eye.hideturtle()

# Create Trail
trail = turtle.Turtle()
trail.speed(0)
trail.shape("square")
trail.shapesize(stretch_len=1, stretch_wid=1)
trail.color("black")
trail.penup()
trail.hideturtle()

# Create Enemy
enemy = turtle.Turtle()
enemy.speed(0)
enemy.penup()
enemy.shape("square")
enemy.shapesize(stretch_len=1, outline=1)
enemy.color("red")
enemy.goto(0, -60)
enemy.hideturtle()
enemydx = 0.01

def right():
    x = player.xcor()
    x += playerdx
    player.setx(x)
def left():
    x = player.xcor()
    x -= playerdx
    player.setx(x)

def setRight():
    rightBool[0] = True
def setLeft():
    leftBool[0] = True
def setDown():
    downBool[0] = True
def unRight():
    rightBool[0] = False
def unLeft():
    leftBool[0] = False
def unDown():
    downBool[0] = False

def playerJump(jumpCount):
    if jumpCount.jumps > 0:
        jumping[0] = True
        y = player.ycor()
        y += 75
        player.sety(y)
    jumpCount.decreaseJumps(1)
    
"""
def playerRight(counter, maxSpeed, inMotion):
    inMotion.append(True)
    counter.append(len(counter))
    if len(counter) >= maxSpeed:
        counter.pop()
    x = player.xcor()
    x += len(counter)
    player.setx(x)

def playerLeft(counter, maxSpeed, inMotion):
    inMotion.append(True)
    counter.append(len(counter))
    if len(counter) >= maxSpeed:
        counter.pop()
    x = player.xcor()
    x -= len(counter)
    player.setx(x)
"""
def down():
    if inAir[0] == True:
        y = player.ycor()
        y -= 1
        player.sety(y)

# Keyboard Functions
win.listen()
win.onkeypress(lambda: playerJump(jumpCount), "w")
win.onkeypress(setRight, "d")
win.onkeypress(setLeft, "a")
win.onkeypress(setDown, "s")
win.onkeyrelease(unRight, "d")
win.onkeyrelease(unLeft, "a")
win.onkeyrelease(unDown, "s")

"""def inBounds(target, lower, upper):
    target = round(target, 1)
    ls = []
    for x in range((upper-lower)*10):
        ls.append(x/10+lower)
    for i in ls:
        if target == i:
            return True
    return False"""

def inBounds(target, lower, upper):
    if lower < target < upper:
        return True
    else:
        return False

while True:
    win.update()
    eyeLeft.goto(player.xcor()-5, player.ycor())
    eyeRight.goto(player.xcor()+5, player.ycor())
    if onGround[0] == True:
        jumpCount.setJumps(2)
    if rightBool[0] == True:
        right()
    if leftBool[0] == True:
        left()
    if downBool[0] == True:
        down()
    
    # Handle player clipping through ground
    if player.ycor() > grass.ycor()+49.8:
        player.sety(player.ycor()-playerdy)
        inAir[0] = True
        onGround[0] = False
    else:
        player.goto(player.xcor(), grass.ycor()+50)
        inAir[0] = False
        onGround[0] = True
    
    # Handle enemy clipping through ground
    if enemy.ycor() > grass.ycor()+50:
        enemy.sety(enemy.ycor()-enemydx)
    else:
        enemy.goto(enemy.xcor(), grass.ycor()+50)
    
    # Handle player clipping through platform
    if player.xcor() > a1.xcor()-50 and player.xcor() < a1.xcor()+50: # Platform a1
        if player.ycor() > a1.ycor()+19.8:
            player.sety(player.ycor()-playerdy)
            inAir[0] = True
            onGround[0] = False
        elif inBounds(player.ycor(), a1.ycor(), a1.ycor()+20):
            player.goto(player.xcor(), a1.ycor()+20)
            inAir[0] = False
            onGround[0] = True
    elif player.xcor() > a2.xcor()-50 and player.xcor() < a2.xcor()+50: # Platform a2
        if player.ycor() > a2.ycor()+19.8:
            player.sety(player.ycor()-playerdy)
            inAir[0] = True
            onGround[0] = False
        elif inBounds(player.ycor(), a2.ycor(), a2.ycor()+20):
            player.goto(player.xcor(), a2.ycor()+20)
            inAir[0] = False
            onGround[0] = True
    elif player.xcor() > a3.xcor()-50 and player.xcor() < a3.xcor()+50: # Platform a3
        if player.ycor() > a3.ycor()+19.8:
            player.sety(player.ycor()-playerdy)
            inAir[0] = True
            onGround[0] = False
        elif inBounds(player.ycor(), a3.ycor(), a3.ycor()+20):
            player.goto(player.xcor(), a3.ycor()+20)
            inAir[0] = False
            onGround[0] = True

    # Handle player going off screen
    if player.xcor() >= 350:
        level = 1
        score.clear()
        score.write("Level {}".format(level), align = "center", font = ("Courier", 14, "normal"))
        player.goto(-340, -75)
        a1.goto(-180, 0)
        a2.goto(0, 0)
        a3.goto(180, 0)
        door.goto(340, 80)
    elif player.xcor() <= -350: 
        player.goto(-348, player.ycor())
    
    if inBounds(player.xcor(), door.xcor()-25, door.xcor()+25) and inBounds(player.ycor(), door.ycor()-25, door.ycor()+25):
        level += 1
        score.clear()
        score.write("Level {}".format(level), align = "center", font = ("Courier", 14, "normal"))
        player.goto(-340, -75)
        a1y = random.randint(-80, 80)
        a2y = random.randint(-80, 80)
        a3y = random.randint(-80, 80)
        a1.goto(-180, a1y)
        a2.goto(0, a2y)
        a3.goto(180, a3y)
        cloud.speed(6)
        doory = random.randint(0, 120)
        door.goto(340, doory)