from random import *
from tkinter import *
w=Tk()
el={1:2,2:3,3:1}
elnames=['','камень','ножницы','бумага']
def update(i):
    l['text']=elnames[int(i)]
    if int(i)<1 or int(i)>3:
        b['state']=DISABLED
    else:
        b['state']=NORMAL
def play2():
    play(s.get())
def play(p):
    global bot,pi
    b.config(text='Продолжить',command=cont)
    bot=randint(1,3)
    l2['text']=f'бот выбрал {elnames[bot]}'
    pi=p
def cont():
    global bot,pi,rounds,wins
    b.config(text='Играть',command=play2)
    rounds+=1
    if pi==bot:
        wins+=0.5
        l2['text']='ничья'
    elif el[pi]==bot:
        wins+=1
        l2['text']='победа'
    else:
        l2['text']='проигрыш'
    h['text']=f'{wins}/{rounds}'
w.title('rock, paper, scissors')
w.geometry('500x300')
rounds=0
wins=0
h=Label(text='0/0')
h.pack()
s=Scale(command=update,to=3)
s.pack()
l=Label()
l.pack()
l2=Label()
l2.pack()
b=Button(command=play2,state=DISABLED,text='играть')
b.pack()

w.mainloop()