from random import *
from tkinter import *
w=Tk()
w.title('Guess the Number!')
w.geometry('250x100')
a=randint(1,1000)
i=0
t=1
def t1ry():
    global i,intry,t,a
    i=int(intry.get())
    t+=1
    att['text']=f'Attempt {t}'
    if i<a:
        sign['text']=">"
    if i>a:
        sign['text']="<"
    if i==a:
        sign['text']="="
att=Label(text="Attempt 1")
intry=Entry()
btn=Button(command=t1ry,text="Guess")
sign=Label(text="?")
att.pack()
intry.pack()
btn.pack()
sign.pack()
w.mainloop()