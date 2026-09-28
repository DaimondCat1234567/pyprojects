from random import *
from time import *
from tkinter import *
w=Tk() # конфигурация окна
w.geometry('1435x770')
w.title('PyOS')
note=[]
def pa_randball():
        print('В свой ход ты берешь шарик из мешка. Если зеленый, игра продолжается а если белый - ты проиграешь.')
        green=int(input('Число зеленых шариков:'))
        p=input('Имена:\n').split()
        i=1
        while True:
            if i==len(p):
                i=1
            else:
                i+=1
            i-=1
            print(f'Ход {p[i]}')
            input('Нажми Enter чтобы достать шарик')
            if randint(1,green+1)==1:
                print(f'Взят белый шарик. {p[i]} проиграл(а)')
                break
            else:
                print('Взят зеленый шарик')
                green-=1
            i+=1
def pa_python():
        print('Python 4.0 by Kirill')
        while True:
            a=input('python>')
            if a=='quit()':
                break
            else:
                try:
                    eval(a)
                except SyntaxError:
                    print('Syntax error')
                except NameError:
                    print('Command not found')
        print('Exiting Python')
def pa_agio():
        
        print('''Добро пожаловать в Лабиринт с Айтигеником!
        Айтигеник попал в лабиринт и его задача - выбраться из него.
        На пути будут возникать различные препятствия,
        которые нужно преодолеть.
        Нажми ENTER, чтобы начать!''')
        input()
        s=1
        r=['Летает без крыльев и плачет без глаз','название файла с игрой без .pyapp']
        ans=['туча','aytiGAMEio']
        i=0
        hp=10
        while s <= 5:
            print(f'Уровень {s}')
            if randint(1,4)==1:
                print('Я встретил тупик!')
                a=input('1-идти обратно, 2-Пытаться найти выход')
                if a=='1':
                    print('Иду обратно')
                if a=='2':
                    if randint(1,3)==1:
                        print('Я не нашел выход и вернулся назад')
                    elif randint(1,2)==2:
                        print('Я упал в яму (проигрыш)')
                        break
                    else:
                        print('Я нашел выход!')
                        s+=1
            elif randint(1,3)==1:
                print('Там магическая дверь! нужно отгадать загадку!')
                try:
                    a=input(r[i])
                    if a==ans[i]:
                        s+=1
                        i+=1
                        print('Ты отгадал загадку')
                except IndexError:
                    i=0
                    a=input(r[i])
                    if a==ans[i]:
                        s+=1
                        i+=1
                        print('Ты отгадал загадку')
            elif randint(1,2)==1:
                print('тут монстр...')
                a=input('1-идти обратно, 2-Сразиться')
                if a=='1':
                    print('Иду обратно')
                if a=='2':
                    a=randint(1,100)
                    if a>50:
                        print('победа')
                        s+=1
                    else:
                        print('проигрыш (-1 hp). hp:',end=' ')
                        hp-=1
                        print(hp)
                        if hp==0:
                            print('ты проиграл')
                            break
            else:
                print('секретный проход')
                a=input('1-Пойти дальше, 2-Пойти через проход')
                if a=='1':
                    print('Иду дальше')
                    s+=1
                if a=='2':
                    if randint(1,4)==1:
                        print('Я не нашел выход, иду дальше')
                        s+=1
                    elif randint(1,3)==2:
                        print('Я упал в яму (проигрыш)')
                        break
                    elif randint(1,2)==1:
                        print('Я нашел выход!')
                        s=6
                    else:
                        print('я нашел сокровище!')
                        s+=1
            if s>5:
                print('победа')
                break
def pa_type():
        phrases=['Не буди лихо, пока оно тихо','Друг познается в беде','В тихом омуте черти водятся','В гостях хорошо, а дома лучше.']
        print('Тебе нужно ввести эту фразу:')
        p=choice(phrases)
        print(p)

        input('Нажмите на enter чтобы начать')
        print('На старт')
        sleep(1)
        print('Внимание')
        sleep(1)
        print('Марш!')
        t1=time()
        u=input()
        t2=time()
        t=t2-t1
        l=len(p)
        print(f'за {t} секунд введено {l} символов')
        print(f'{l/t} CPS')
        mist=0
        for a,b in zip(u,p):
            if a!=b:
                print(f'Ошибка: вместо {b} написано {a}')
                mist+=1
        print(f'{mist} ошибок')
def pa_note():
        for i in note:
            print(i)
        while True:
            a=input()
            if a=='' or a=='np.Close':
                print('Closed')
                break
            else:
                note.append(a)
        
def pa_pynote():
        for i in note:
            try:
                eval(i)
            except SyntaxError:
                print('Syntax error')
            except NameError:
                print('Command not found')
def pa_dragon():
        t=0
        print('''Ты находишься в земле, полной драконов. Перед собой ты видишь две пещеры.

        В одной пещере дракон дружелюбен и поделится с тобой своим сокровищем.

        Другой дракон жадный и голодный, и он с удовольствием тебя съест.
        ''')
        def roll(sides=6):
            return(randint(1,sides))
        def wait2():
            sleep(2)
        while True:
            a=0
            print('В какую пещеру идем? (в пещеру слева - A, справа - D)')
            while a!='a' and a!='d' and a!='x':
                a=input('>')
            if a=='x':
                break
            print('Ты приближаешься к пещере…')
            wait2()
            print('Она темная и жуткая…')
            wait2()
            print('Большой дракон выпрыгивает прямо перед вами! Он открывает свои челюсти и…')
            wait2()
            if roll(2)==1:
                print('Дракон даёт тебе своё сокровище')
                t+=1
            else:
                print('Дракон съедает тебя за один укус')
                break
            print('Чтобы завершить игру, нажми X и Enter')
        print(f'Ты получил {t} сокровищ!')
def pa_notedialog():
    print('Чтобы запустить в Блокноте, введите N')
    print('В Python - P')
    a=input()
    if a=='n':
        pa_note
    if a=='p':
        pa_pynote
def pa_dragon_n():
    global scoredisplay, score
    wd=Toplevel()
    wd.title('Dragon')
    btn_d_1=Button(wd,text='Левая пещера',command=dragon_choosecave)
    score=0
    scoredisplay=Label(text='0 сокровищ')
def dragon_choosecave():
    global score
    #if randint 
t=Label(text='pyOS v1.0.1')
t.pack()
f1=LabelFrame(text='Игры',width=300,height=100)
f1.pack()
rb=Button(f1,text='randomball.pyapp', command=pa_randball, width=20)
rb.grid(row=0,column=0,padx=10,pady=10)
py=Button(text='python.pyapp', command=pa_python, width=20)
py.pack()
ay=Button(f1,text='aytigameio.pyapp', command=pa_agio, width=20)
ay.grid(row=1,column=0,padx=10,pady=10)
tcb=Button(f1,text='typecbat.pyapp', command=pa_type, width=20)
tcb.grid(row=0,column=1,padx=10,pady=10)
dr=Button(f1,text='dragon.pyapp', command=pa_dragon, width=20)
dr.grid(row=1,column=1,padx=10,pady=10)
drn=Button(f1,text='dragon-n.pyapp', command=pa_dragon_n, width=20)
drn.grid(row=1,column=1,padx=10,pady=10)
sd=Button(text='Shutdown', command=quit, width=20)
sd.pack()
w.mainloop() # конец