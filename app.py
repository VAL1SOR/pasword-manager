from asyncio.windows_events import NULL
import random 
import string
from tkinter import *
from tkinter import Tk
from webbrowser import get

root = Tk()

v = NULL

t = NULL

c = NULL

r = NULL



Checkbutton(root, text='lowercase',variable = t, onvalue = string.ascii_lowercase, offvalue = NULL).pack()
Checkbutton(root, text='uppercase',variable = v, onvalue = string.ascii_uppercase, offvalue = NULL).pack()
Checkbutton(root, text='digits',variable = c, onvalue = string.digits, offvalue = NULL).pack()
Checkbutton(root, text='punctuation',variable = r, onvalue = string.punctuation, offvalue = NULL).pack()
z = Spinbox(root, from_=1, to=2048, values = 5).pack()

def get_random_string():
    return ''.join(random.choice(t + v + c + r) for _ in range(z.get                    ))

Button(root, text = "Generate", command = get_random_string).pack()

root.mainloop()