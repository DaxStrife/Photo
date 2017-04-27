

#Python 3.6

from tkinter import *

root = Tk()

name = "Name of the photo.png" #A .png extension is added
photo = PhotoImage(file=name)
photo_label = Label(root,image=photo).pack()

root.mainloop()
