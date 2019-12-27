from tkinter import *
import sys
import time
def times():
    current_time=time.strftime("%H:%M:%S")
    clock.config(text=current_time)
    clock.after(200,times)

root=Tk()
root.geometry("500x200")

clock=Label(root, font="times 50 bold",bg="white")
clock.grid(row=2,column=2,pady=25,padx=100)
times()
digi=Label(root,text="Digital Clock",font="times 20 bold")
digi.grid(row=1,column=2)
nota=Label(root,text="      Hours   :  Minutes   :   Seconds      ",font="times 15 bold")
nota.grid(row=3,column=2)
root.mainloop()

