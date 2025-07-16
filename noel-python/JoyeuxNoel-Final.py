from tkinter import *

REP_IMG = "./images/"


images_boules = ["boule1.png", "boule2.png", "boule3.png", "boule4.png"]
current_boule = 0

boules = []


def onClique(event):
    image_boule = PhotoImage(file=REP_IMG + images_boules[current_boule])
    boules.append(image_boule)
    canvas.create_image(event.x, event.y, image=image_boule)
    # Si pas gardé, la boule est détruite dès que l'on sort !


def onEfface(event):
    if len(boules) > 0:
        bouleAEffacer = boules.pop()
        canvas.delete(bouleAEffacer)


def onChangeBoule(event):
    global current_boule
    current_boule += 1
    if current_boule >= len(images_boules):
        current_boule = 0


maFenetre = Tk()
maFenetre.title("Joyeux Noël")

canvas = Canvas(maFenetre, width=800, height=800, bg="black")

image_fond = PhotoImage(file=REP_IMG + "sapin.png")
canvas.create_image(400, 400, image=image_fond)

canvas.pack()

canvas.bind("<Button-1>", onClique)
maFenetre.bind("e", onEfface)
maFenetre.bind("<space>", onChangeBoule)

maFenetre.mainloop()
