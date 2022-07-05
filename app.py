import random 
import string
from tkinter import *
import clipboard
from tkinter import ttk

root = Tk()
root.title("Password Manager")
root.geometry("400x300")
tabControl = ttk.Notebook(root)

tab1 = ttk.Frame(tabControl)
tab2 = ttk.Frame(tabControl)
  
tabControl.add(tab1, text ='Password Manager')
tabControl.add(tab2, text ='Password Generator')
tabControl.pack(expand = 1, fill ="both")

v = IntVar()
t = IntVar()
c = IntVar()
r = IntVar()
rr = []
result = ""
save = []
f = open("passwords.psdw", "a")
rrr = open("passwords.psdw", "r")

Checkbutton(tab2, text='lowercase', onvalue = 1, offvalue = 0, variable = t).pack()
Checkbutton(tab2, text='uppercase', onvalue = 1, offvalue = 0, variable = v).pack()
Checkbutton(tab2, text='digits', onvalue = 1, offvalue = 0, variable = c).pack()
Checkbutton(tab2, text='punctuation', onvalue = 1, offvalue = 0, variable = r).pack()
z = Spinbox(tab2, from_=1, to=2048)
z.pack()

w = Entry(tab1, width = 20)
w2 = Entry(tab1, width = 20)

Label(tab1, text = "account").grid(column = 0, row = 0)
Label(tab1, text = "password").grid(column = 1, row = 0)

w.grid(column = 0, row = 1, padx = 10, pady = 5)
w2.grid(column = 1, row = 1, padx = 10, pady = 5)

def save_password():
    f = open("passwords.psdw", "a")
    f.write(w.get() + " " + w2.get() + "\n")
    for _ in rrr:
        if (_ not in save):
            save.append(_)
            Label(tab1, text = _, onclick = clipboard.copy(_)).grid(column = 1)

Button(tab1, text = "Save Password", command = save_password).grid(column = 2, row = 1, padx = 10, pady = 30)

for _ in rrr:
        if (_ not in save):
            save.append(_)
            Label(tab1, text = _, onclick = clipboard.copy(_)).grid(column = 1)

def get_random_string():
    a = int(z.get())

    if(t.get() == 1 and t.get() not in rr):
        rr.append(string.ascii_lowercase)
    if(v.get() == 1 and v.get() not in rr):
        rr.append(string.ascii_uppercase)
    if(c.get() == 1 and c.get() not in rr):
        rr.append(string.digits)
    if(r.get() == 1 and r.get() not in rr):
        rr.append(string.punctuation)
    if(t.get() == 0 and t.get() in rr):
        rr.remove(string.ascii_lowercase)
    if(v.get() == 0 and v.get() in rr):
        rr.remove(string.ascii_uppercase)
    if(c.get() == 0 and c.get() in rr):
        rr.remove(string.digits)
    if(r.get() == 0 and r.get() in rr):
        rr.remove(string.punctuation)

    result = "".join(random.choice(random.choice(random.choice(rr))) for _ in range(a))
    
    finish = Label(tab2, text = result, onclick = clipboard.copy(result), bg = "gray")
    finish.pack()

    rr.clear()

Button(tab2, text = "Generate", command = get_random_string).pack()

root.mainloop()
