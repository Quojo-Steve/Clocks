from tkinter import *
from datetime import datetime
from time import strftime
from PIL import ImageTk,Image

root=Tk()
root.geometry('1280x720')
root.minsize(750,200)
root.title("Python clock")

# background setting
img1 = Image.open('Ibiza_Sunset.jpg')
img2 = ImageTk.PhotoImage(img1)
Label(root, image=img2).place(x=0, y=0)

f1=Frame(root, width=750, height=200, bg="#0e1013")
# f1.place(x=0,y=0)
f1.pack(expand=True)

a=datetime.today().strftime("%A")
b=a.upper()
c=b[0:3]

def time():
    a=strftime('%H : %M : %S')
    l1.config(text=a)
    l1.after(1000,time)

l1=Label(f1, font=('Century Gothic', 60),bg= '#0e1013', fg="#d3d3d3")
l1.place(x=300, y=35)
time()

l2=Label(f1, font=('Century Gothic', 60),bg= '#0e1013', fg="#d3d3d3")
l2.config(text=c+" |")
l2.place(x=80, y=35)

def labels():
    l3=Label(f1, font=('Century Gothic', 8), bg= '#0e1013', fg="#7f7f7f", text='DAY')
    l3.place(x=129,y=130)

    l3 = Label(f1, font=('Century Gothic', 8), bg='#0e1013', fg="#7f7f7f", text='HOURS')
    l3.place(x=320, y=130)

    l3 = Label(f1, font=('Century Gothic', 8), bg='#0e1013', fg="#7f7f7f", text='MINUTES')
    l3.place(x=445+35, y=130)

    l3 = Label(f1, font=('Century Gothic', 8), bg='#0e1013', fg="#7f7f7f", text='SECONDS')
    l3.place(x=445+180, y=130)

labels()




root.mainloop()