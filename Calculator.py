from tkinter import *
import tkinter
import tkinter.messagebox
def proces():
    number1=Entry.get(A1)
    number2=Entry.get(A2)
    operator=Entry.get(A3)
    number1=float(number1)
    number2=float(number2)
    if operator =="+":
        answer=number1+number2
    if operator =="-":
        answer=number1-number2
    if operator=="*":
        answer=number1*number2
    if operator=="/":
        answer=number1/number2
    Entry.insert(E4,0,answer)
    print(answer)
top = tkinter.Tk()
L1 = Label(top, text="My calculator",).grid(row=0,column=1)
L2 = Label(top, text="Number 1",).grid(row=1,column=0)
L3 = Label(top, text="Number 2",).grid(row=2,column=0)
L4 = Label(top, text="Operator",).grid(row=3,column=0)
L4 = Label(top, text="Answer",).grid(row=4,column=0)
A1 = Entry(top, bd =5)
A1.grid(row=1,column=1)
A2 = Entry(top, bd =5)
A2.grid(row=2,column=1)
A3 = Entry(top, bd =5)
A3.grid(row=3,column=1)
A4 = Entry(top, bd =5)
A4.grid(row=4,column=1)
B=Button(top, text ="Submit",command = proces).grid(row=5,column=1,)
top.mainloop()
