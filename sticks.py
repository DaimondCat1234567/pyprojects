from tkinter import *
from random import *
diff=0
diffs=['простая','средняя','сложная','очень сложная']
def play():
    s.destroy()
    d.destroy()
    robot.grid(columnspan=2)
    selector.grid(row=1,column=0)
    ok.grid(row=1,column=1)
    stickst.grid(row=2,columnspan=2)
    sticksc.grid(row=3,columnspan=2)
def diffchng():
    global diff
    if diff==2:
        diff=0
    else:
        diff+=1
    d['text']=f'Сложность: {diffs[diff]}'
def p():
    global sticks,ok,selector
    ok['state']=DISABLED
    sticks-=selector.get()
    u('player')
def u(a):
    global sticks,sticksc,stickst,robot
    if sticks>3:
        selector['to']=3
    else:
        selector['to']=sticks-1
    sticksc['text']=sticks
    stickst['text']='I'*sticks
    if sticks==1:
        endscreen=Toplevel()
        endscreen.title('Конeц игры')
        if a=='player':
            endtext=Label(endscreen,fg='green',text='Победа!',font='Arial 15 bold')
        else:
            endtext=Label(endscreen,fg='red',text='Проигрыш!',font='Arial 15 bold')
        ok['state']=DISABLED
        endtext.pack()
    else:
        if a=='player':
            robot['text']='Бот думает'
            w.after(2000,b)
            
def b():
    global sticks,diff
    if (diff==1 and sticks<=3) or (diff==2 and sticks<=4):
        sticks=1
    else:
        sticks-=randint(1,min(3,sticks-1))
    robot['text']=''
    u('bot')
    ok['state']=NORMAL
sticks=20
w=Tk()
w.title('Палочки')
d=Button(command=diffchng,text='Сложность: простая')   
s=Button(command=play,text='ИГРАТЬ')
s.pack()
d.pack()
robot=Label()
selector=Scale(from_=1,to=3)
ok=Button(text='ok',command=p)
stickst=Label(text='I'*20)
sticksc=Label(text=20,font='Arial 15 bold')
w.mainloop()