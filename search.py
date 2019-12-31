import wikipedia
from tkinter import *
from tkinter.messagebox import showinfo
wi=Tk()
wi.title('Search')
wi.geometry("600x200")
def searchs():
    search=entry.get()
    ans=wikipedia.summary(search,sentences=6)
    showinfo("Answer is",ans)
label1=Label(wi,text="Enter the content what you need to serach",font="times 20 bold")
label1.grid(row=0,column=1,padx=10)
label2=Label(wi)
label2.grid(row=1)
label2.grid(row=2)
label=Label(wi,text="Search:",font="Times 15 bold")
label.grid(row=3,column=0)
entry=Entry(wi,bd=5)
entry.grid(row=3,column=1)
label2.grid(row=4)
label2.grid(row=5)
button=Button(wi,text="Search",font="times 15 bold",command=searchs)
button.grid(row=6,column=1,padx=10)
wi.mainloop()