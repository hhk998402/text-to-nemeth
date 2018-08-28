import main as brl
import tkinter
from tkinter import *

master = Tk()

e = Entry(master)
e.pack()

e.focus_set()

def callback():
    example=brl.text2nemeth(e.get())
    #print(example)
    T.delete("1.0", tkinter.END)
    T.insert(END,example)
    #print e.get()

b = Button(master, text="Convert to Braille", width=20, command=callback)
b.pack()
T = Text(master, height=10, width=30)
T.pack()

mainloop()
e = Entry(master, height = 10,width=1000)
e.pack()


text = e.get()