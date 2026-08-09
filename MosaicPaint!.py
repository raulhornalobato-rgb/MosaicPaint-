import keyboard
import tkinter as tk
import random
import time

Xvalue = 295
Yvalue = 295

root = tk.Tk()
root.geometry("600x600")
root.resizable(False,False)
root.title("Mosaic")

cube = tk.Canvas(root, bg="Black", width=10, height=10)
cube.pack(pady=250)

BackgroundChange = tk.Button(root, bg="Red", text="Change Background", command=lambda: Change())
BackgroundChange.place(x=0, y=575)

def Right():
    global Xvalue
    Var1 = keyboard.is_pressed("D")
    if Var1:
        Xvalue += 1
        cube.place(x=Xvalue)
    root.after(25, Right)

def Left():
    global Xvalue
    Var2 = keyboard.is_pressed("A")
    if Var2:
        Xvalue -= 1
        cube.place(x=Xvalue)
    root.after(25, Left)

def Up():
    global Yvalue
    Var3 = keyboard.is_pressed("W")
    if Var3:
        Yvalue -= 1
        cube.place(y=Yvalue)
    root.after(25, Up)

def Down():
    global Yvalue
    Var4 = keyboard.is_pressed("S")
    if Var4:
        Yvalue += 1
        cube.place(y=Yvalue)
    root.after(25, Down)

def Draw():
    Var5 = keyboard.is_pressed("Space")
    if Var5:
        Paint = tk.Canvas(root, bg="Black", width=10, height=10)
        Paint.place(x=Xvalue, y=Yvalue)
        Var6 = random.randint(1,8)
        print(Var6)
        if Var6 == 1:
            Paint.config(bg="Red")
        elif Var6 == 2:
            Paint.config(bg="Green")
        elif Var6 == 3:
            Paint.config(bg="Blue")
        elif Var6 == 4:
            Paint.config(bg="Yellow")
        elif Var6 == 5:
            Paint.config(bg="Orange")
        elif Var6 == 6:
            Paint.config(bg="Purple")
        elif Var6 == 7:
            Paint.config(bg="Indigo")
        elif Var6 == 8:
            Paint.config(bg="Pink")
    root.after(300, Draw)

def Change():
    Var7 = random.randint(0,8)
    print(Var7)
    if Var7 == 0:
        root.config(bg="White")
    elif Var7 == 1:
        root.config(bg="Light Green")
    elif Var7 == 2:
        root.config(bg="Light Blue")
    elif Var7 == 3:
        root.config(bg="Firebrick1")
    elif Var7 == 4:
        root.config(bg="SlateBlue1")
    elif Var7 == 5:
        root.config(bg="Hot Pink")
    elif Var7 == 6:
        root.config(bg="light goldenrod")
    elif Var7 == 7:
        root.config(bg="NavajoWhite4")
    elif Var7 == 8:
        root.config(bg="medium purple")
Right()
Left()
Up()
Down()
Draw()

root.mainloop()