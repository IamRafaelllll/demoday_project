import tkinter as tk
from PIL import ImageTk, Image
import os
import sys

window = tk.Tk()
window.title("Final Project")
window.geometry("1200x1200")

img_path = 'HomegirlRosa.jpg'

choice = input("Do you want to see Rosa Parks? ")

if choice == 'yes':
	img = ImageTk.PhotoImage(Image.open(img_path))
	panel = tk.Label(window, image = img)
	panel.pack(side = "bottom", fill = "both", expand = "yes")
	





window.mainloop()

# lbl = tk.Label(window, text="Hello")




# def openfn():
#     filename = filedialog.askopenfilename(title='open')
#     return filename
# def open_img():
#     x = openfn()
#     img = Image.open(x)
#     img = img.resize((250, 250), Image.ANTIALIAS)
#     img = ImageTk.PhotoImage(img)
#     panel = Label(root, image=img)
#     panel.image = img
#     panel.pack()


def clicked():
    lbl.configure(text="Button was clicked")

btn = tk.Button(window, text="Click Me", bg="black", fg="white", command=clicked)
btn = tk.Button(window, text="Click Me", command=clicked)
btn.grid(column=1, row=0)
# window.mainloop()
