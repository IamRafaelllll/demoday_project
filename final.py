from tkinter import *
from PIL import Image, ImageTk
import os

root = Tk()
root.title("Activists")
root.geometry("600x600")

def changeimage(*args):
    path = heroes[variable.get()]
    img = ImageTk.PhotoImage(Image.open(path))
    panel.configure(image = img)
    panel.img = img


def writeimage(*args):
    info = heroes_information[variable.get()]
    print(info)
    T = tk.Text(root, HEIGHT = 50, WIDTH = 200)
    T.insert(tk.END, info)



def show():
    label.config( text =clicked.get())

frame1 = Frame(root)
frame2 = Frame(root)
frame3 = Frame(root)
frame4 = Frame(root)
frame5 = Frame(root)

options = [
"Home Page",
"Rosa Parks",
"MLK",
"Hariet Tubman",
"Sojourner Truth",
"Malcolm X"
]

heroes = {'Home Page': 'HomePage.jpg','Rosa Parks': 'HomegirlRosa.jpg', 'MLK': 'HomeboyMLK.jpg', 'Hariet Tubman': 'HomegirlHariet.jpg', 'Sojourner Truth': 'HomegirlTruth.jpg', 'Malcolm X': 'HomeboyMalcolm.jpg'}

heroes_information = {'Rosa Parks': 'Rosa Parks Information', 'MLK': 'MLK Information', 'Hariet Tubman': 'Hariet Tubman Information', 'Sojourner Truth': 'Sojourner Truth Information', 'Malcolm X': 'Malcolm X Information'}

variable = StringVar(root)
variable.set(options[0])

w = OptionMenu(root, variable, *options)
path = heroes[variable.get()]

img = ImageTk.PhotoImage(Image.open(path))

panel = Label(frame2, image = img)
panel.pack()

w.pack()
frame1.pack()

frame2.pack()
variable.trace_add('write', changeimage)
root.mainloop()
