import time
import turtle
from random import randint
from tkinter import *
from PIL import Image, ImageShow, ImageTk

#Function to generate a tic-tac-toe game
def generateBoard(root):
    root.destroy()
    #Creating screen & setting configurations
    root = Tk()
    root.configure(background = "light blue")
    root.title("Tic Tac Toe")
    root.geometry("160x160")

    #Makes buttons interactive
    def mark(r, c, button):
        button.destroy()
        x = Canvas(root, width = 50, height = 50, bg = "white")
        x.create_line(0, 0, 50, 50)
        x.create_line(50, 0, 0, 50)
        x.grid(row = r, column = c)

    #Loads a white square image
    im = PhotoImage(file = r"C:\Users\trued\Documents\Python\Experiments\Pictures\white.png")

    #Creates Buttons that symbolize each square in the tic-tac-toe board
    a1 = Button(root, image = im, width = 50, height = 50, bd = 1, activebackground = "Black", command = lambda: mark(0, 0, a1))
    a2 = Button(root, image = im, width = 50, height = 50, bd = 1, activebackground = "Black", command = lambda: mark(0, 1, a2))
    a3 = Button(root, image = im, width = 50, height = 50, bd = 1, activebackground = "Black", command = lambda: mark(0, 2, a3))
    b1 = Button(root, image = im, width = 50, height = 50, bd = 1, activebackground = "Black", command = lambda: mark(1, 0, b1))
    b2 = Button(root, image = im, width = 50, height = 50, bd = 1, activebackground = "Black", command = lambda: mark(1, 1, b2))
    b3 = Button(root, image = im, width = 50, height = 50, bd = 1, activebackground = "Black", command = lambda: mark(1, 2, b3))
    c1 = Button(root, image = im, width = 50, height = 50, bd = 1, activebackground = "Black", command = lambda: mark(2, 0, c1))
    c2 = Button(root, image = im, width = 50, height = 50, bd = 1, activebackground = "Black", command = lambda: mark(2, 1, c2))
    c3 = Button(root, image = im, width = 50, height = 50, bd = 1, activebackground = "Black", command = lambda: mark(2, 2, c3))

    #Assigns each button to a specific place in the board
    a1.grid(row = 0, column = 0)
    a2.grid(row = 0, column = 1)
    a3.grid(row = 0, column = 2)
    b1.grid(row = 1, column = 0)
    b2.grid(row = 1, column = 1)
    b3.grid(row = 1, column = 2)
    c1.grid(row = 2, column = 0)
    c2.grid(row = 2, column = 1)
    c3.grid(row = 2, column = 2)

    #Generates a live interactive sandbox for the user
    mainloop()

def generateRunner(root):
        root.destroy()
        # Generate Window
        win = turtle.Screen()
        win.title("Runner")
        win.bgcolor("light green")
        win.setup(width = 720, height = 240)
        win.tracer(0)

        # Generate Scenary
        grass = turtle.addshape("rectangle", ((-360, -120), (360, -120), (360, -240), (-360, -240)))
        win.addshape("rectangle", ((-360, -120), (360, -120), (360, -240), (-360, -240)))
        # Create player
        player = turtle.Turtle()
        player.speed(0)
        player.penup()
        player.shape("square")
        player.shapesize(stretch_len=1)
        player.color("white")
        player.goto(-340, -60)

        while True:
            win.update()
            #if player.ycor() > grass.ycor():
            #    player.sety(player.ycor()-1)

def mainMenu():
    global root
    root = Tk()
    root.configure(background = "light green")
    root.title("Runner")
    root.geometry("720x240")
    title = Label(root, text = "Main Menu", bg = "light green")
    title.pack(side = TOP)
    runner = Button(root, text = "Play Runner", command = lambda: generateRunner(root))
    runner.pack(side = TOP)
    Tic = Button(root, text = "Play Tic Tac Toe", command = lambda: generateBoard(root))
    Tic.pack(side = TOP)
    mainloop()
