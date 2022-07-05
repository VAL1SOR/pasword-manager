import random 
import string
from tkinter import *
from tkinter import Tk

root = Tk()
root.title("Password Generator")
root.geometry("400x200")

v = IntVar()
t = IntVar()
c = IntVar()
r = IntVar()
a = 1

c1 = Checkbutton(root, text='lowercase',variable = t, onvalue = random.choice(string.ascii_lowercase), offvalue = 0)
c2 = Checkbutton(root, text='uppercase',variable = v, onvalue = random.choice(string.ascii_uppercase), offvalue = 0)
c3 = Checkbutton(root, text='digits',variable = c, onvalue = random.choice(string.digits), offvalue = 0)
c4 = Checkbutton(root, text='punctuation',variable = r, onvalue = random.choice(string.punctuation), offvalue = 0)
z = Spinbox(root, from_=1, to=2048, textvariable = a)

c1.pack()
c2.pack()
c3.pack()
c4.pack()
z.pack()

lis = [t, v, c, r]

if(t == 0 and v == 0 and c == 0 and r == 0):
    print("Please select at least one character type")

rr = []


def get_random_string():
#    return ''.join(random.choice(rr) for _ in range(a)) 
    result = ""
    i = 0
    while(i < a):
        if(t != 0):
            rr.append(string.ascii_lowercase)
        if(v != 0):
            rr.append(string.ascii_uppercase)

        if(c != 0):
            rr.append(string.digits)

        if(r != 0):
            rr.append(string.punctuation)


        i += 1

        str = "".join(random.choice(rr) for _ in range(a))

    if(i >= a):
        for _ in range(a):
            result = "".join(random.choice(str) for _ in range(a))
            fresult = "".join(random.choice(result) for _ in range(a))
            

    print(fresult)

Button(root, text = "Generate", command = get_random_string).pack()

root.mainloop()
