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
    # T = tk.Text(root, HEIGHT = 50, WIDTH = 200)
    # T.insert(tk.END, info)



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

heroes = {'Home Page': './assets/HomePage.jpg','Rosa Parks': './assets/HomegirlRosa.jpg', 'MLK': './assets/HomeboyMLK.jpg', 'Hariet Tubman': './assets/HomegirlHariet.jpg', 'Sojourner Truth': './assets/HomegirlTruth.jpg', 'Malcolm X': './assets/HomeboyMalcolm.jpg'}

heroes_information = {'Rosa Parks': 'Rosa Louise Parks was a civil rights activist born on February 4th, 1913 in Tuskegee Alabama. She was born at a time where people had preconceived thoughts and labels on people who looked like her. Because of these differences in mindsets, it held her back and made her want to stand against the system. Parks was well respected in her community and many people looked up to her.  She worked as a seamstress until she joined the Montgomery chapter for the NAACP and became a secretary. One of rosa’s most impactful experiences was her refusing to give up her seat on the bus to a white passenger. Because of her actions and the odds being against her,  she got thrown into jail. Because she was being put on trail, the black population put up over 35,000 posters initiating a boycott of buses. This boycott ended 15 days after. As a result of the bus boycotts the court issued an order declaring that bus segration was unconstitutional. Rosa parks has inspired many and to this day the things she fought for has in impact on all of us.', 'MLK': 'MLK Information', 'Hariet Tubman': 'Hariet Tubman Information', 'Sojourner Truth': 'Sojourner Truth Information', 'Malcolm X': 'Malcolm X Information'}

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
