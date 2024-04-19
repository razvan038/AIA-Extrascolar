from tkinter import *
from tkinter.ttk import *
master=Tk()
master.geometry("200x200")
b1=Button(master,text="click me")
b1.place(relx=1, x=-2, y=2, anchor=NE)
l=Label(master,text='i am a label')
l.place(anchor=NW)
b2=Button(master,text="click me")
b2.place(relx=0.5, rely=0.5, anchor=CENTER)
mainloop()