from time import ctime
from tkinter import *

root = Tk()
root.title("my hour")

lbl = Label(root,font=("times new roman",50),bg="purple",fg="white")

def date():
    strg = ctime()
    lbl.config(text=strg)
    lbl.after(100,date)

lbl.pack()

date()
