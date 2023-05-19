import statistics
import tkinter
import tkinter as tk
import os
from functools import partial
from tkinter import *
from tkinter import ttk
from PIL import ImageTk, Image
import numpy as np
import matplotlib.pyplot as plt
import matplotlib
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg,
NavigationToolbar2Tk)

matplotlib.use('TkAgg')
import numpy as np
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure

window = Tk()
window.title("дневник")

columns = ("situation", "emotion", "think")


def win(sportwindow, name_file):
    sportwindow.geometry('1000x400+{}+{}'.format(w // 2 - 400, h // 2 - 400))

    sportframe = Frame(
        sportwindow,
        padx=10,
        pady=10
    )

    def close():
        window.deiconify()
        sportwindow.destroy()

    sportframe.pack(anchor=CENTER)

    back = Button(
        sportframe,
        text='Назад',
        command=close
    )

    back.grid(row=1, column=1)

    set = ttk.Treeview(sportwindow)
    set.pack()

    set['columns'] = ('data', 'situation', 'emotion', 'think', 'mark')
    set.column("#0", width=0, stretch=NO)
    set.column("data", anchor=CENTER, width=200)
    set.column("situation", anchor=CENTER, width=200)
    set.column("emotion", anchor=CENTER, width=200)
    set.column("think", anchor=CENTER, width=200)
    set.column("mark", anchor=CENTER, width=200)

    set.heading("#0", text="", anchor=CENTER)
    set.heading("data", text="Дата", anchor=CENTER)
    set.heading("situation", text="Ситуация", anchor=CENTER)
    set.heading("emotion", text="Эмоции", anchor=CENTER)
    set.heading("think", text="Мысли", anchor=CENTER)
    set.heading("mark", text="Оценка", anchor=CENTER)

    sportdata = []

    '''for data in sportdata:
        set.insert(parent='', index='end', text='', values=(data[0], data[1], data[2], data[3]))'''

    input_frame = Frame(sportwindow)
    input_frame.pack()

    data = Label(input_frame, text="Дата")
    data.grid(row=0, column=0)

    situation = Label(input_frame, text="Ситуация")
    situation.grid(row=0, column=1)

    emotion = Label(input_frame, text="Эмоции")
    emotion.grid(row=0, column=2)

    think = Label(input_frame, text="Мысли")
    think.grid(row=0, column=3)

    mark = Label(input_frame, text="Оценка")
    mark.grid(row=0, column=4)

    data_entry = Entry(input_frame)
    data_entry.grid(row=1, column=0)

    situation_entry = Entry(input_frame)
    situation_entry.grid(row=1, column=1)

    emotion_entry = Entry(input_frame)
    emotion_entry.grid(row=1, column=2)

    think_entry = Entry(input_frame)
    think_entry.grid(row=1, column=3)

    mark_entry = Entry(input_frame)
    mark_entry.grid(row=1, column=4)

    with open(f"files/{name_file}.txt", "r") as f:
        for i in f.readlines():
            set.insert(parent='', index='end', text='',
                        values=i)

    def input_record():
        if(int(mark_entry.get())<=2):
            lable = Label(master=sportwindow, text='Вам следует обсудить эту ситуацию с психологом')
            lable.pack()
        set.insert(parent='', index='end', text='',
                   values=(data_entry.get(), situation_entry.get(), emotion_entry.get(), think_entry.get(),
                           mark_entry.get()))
        sportdata.append([data_entry.get(), situation_entry.get(), emotion_entry.get(), think_entry.get(),
                          mark_entry.get()])

        with open(f"files/{name_file}.txt", "a") as f:
            for x in sportdata:
                for y in x:
                    f.write(y)
                    f.write("!")
                f.write("\n")

        data_entry.delete(0, END)
        situation_entry.delete(0, END)
        emotion_entry.delete(0, END)
        think_entry.delete(0, END)
        mark_entry.delete(0, END)

    input_button = Button(sportwindow, text="Создать новую запись", command=input_record)

    input_button.pack()

    sportwindow.protocol("WM_DELETE_WINDOW", window.deiconify())

    sportwindow.mainloop()


def sport():
    sportwindow = Tk()
    window.withdraw()
    sportwindow.title("Сфера жизни: Спорт")
    win(sportwindow, "Sport")


def life():
    lifew = Tk()
    window.withdraw()
    lifew.title("Сфера жизни: Личная жизнь")
    win(lifew, "Life")


def family():
    familyw = Tk()
    window.withdraw()
    familyw.title("Сфера жизни: Семья")
    win(familyw, "Family")

def graf():
    grafwind = tk.Toplevel()
    grafwind.attributes("-fullscreen", True)
    lable = Label(master=grafwind, text="Отследите изменение вашего эмоционального состояния", font=("Arial", 24))
    lable.pack()

    def plot(file):
        places = {'SportMood': [60,150],'FamilyMood': [620,150],'LifeMood': [1190,150],'All': [620,600]}

        fig = Figure(figsize=(3, 3),
                     dpi=100)

        if file == 'All':
            sport = list(map(int, open(f'files/SportMood.txt').read().split()))
            life = list(map(int, open(f'files/LifeMood.txt').read().split()))
            family = list(map(int, open(f'files/FamilyMood.txt').read().split()))
            all = [sport, life, family]
            data = list(map(statistics.mean, all))
        else:
            data = list(map(int, open(f'files/{file}.txt').read().split()))

        plot1 = fig.add_subplot(111)

        plot1.plot(data)
        canvas = FigureCanvasTkAgg(fig,
                                   master=grafwind)
        canvas.draw()
        canvas.get_tk_widget().place(x=places[file][0],y=places[file][1])

        toolbar = NavigationToolbar2Tk(canvas,
                                       grafwind)
        toolbar.update()

        canvas.get_tk_widget().place(x=places[file][0],y=places[file][1])

    plot_button_sport = Button(master=grafwind,
                         command=partial(plot, 'SportMood'),
                         height=5,
                         width=30,
                         text="Plot sport")

    plot_button_sport.place(x=100, y=50)

    plot_button_family = Button(master=grafwind,
                               command=partial(plot, 'FamilyMood'),
                               height=5,
                               width=30,
                               text="Plot family")

    plot_button_family.place(x=660, y=50)

    plot_button_life = Button(master=grafwind,
                               command=partial(plot, 'LifeMood'),
                               height=5,
                               width=30,
                               text="Plot life")

    plot_button_life.place(x=1225, y=50)

    plot_button_all = Button(master=grafwind,
                                command=partial(plot, 'All'),
                                height=5,
                                width=30,
                                text="Plot all")

    plot_button_all.place(x=660, y=500)

    '''grafframe = Frame(
        grafwind,
        padx=10,
        pady=10
    )'''

    # grafframe.pack(anchor=CENTER)
    def close():
        window.deiconify()
        grafwind.destroy()

    back = Button(
        grafwind,
        text='Назад',
        font='Impact 10',
        bg='black',
        fg='white',
        command=close
    )

    back.place(x=w - 67, y=5)

    '''sport1.grid(row=2, column=1, padx=10)
    life1.grid(row=2, column=2, padx=10)
    family11.grid(row=2, column=3, padx=10)
    back.grid(row=2, column=0, padx=10)'''

    grafwind.mainloop()


def smile():
    # spisok = []
    # for filename in os.listdir("files"):
    #     new_lst = {}
    #     with open(os.path.join("files", filename), 'r') as f:
    #         text = f.read()
    #         lines = sum(1 for line in text.split('\n'))
    #         if lines > 30:
    #             tab = text.split('\n')[-30:]
    #         else:
    #             tab = text.split('\n')
    #         for item in tab:
    #             if len(item.split(" ")) > 1:
    #                 new_lst[item.split(" ")[0]] = int(item.split(" ")[-2]) \
    #                     if item.split(" ")[-2] in ['1', '2', '3'] else item.split(" ")[-2]
    #         spisok.append(new_lst)
    # lst = [list(x.values()) for x in spisok]
    # all = []
    # for lstq in lst:
    #     all.extend(lstq)
    # count1 = all.count(1)
    # count2 = all.count(2)
    # count3 = all.count(3)
    #
    # maxall = max(count1,count2,count3)
    # if count1 == maxall:
    #     sm = 'images/no.png'
    # else:
    #     if count2 == maxall:
    #         sm = 'images/so.png'
    #     else:
    #         sm = 'images/klass.png'
    #
    # def resize_image(event):
    #     new_width = event.width
    #     new_height = event.height
    #     image = copy_of_image.resize((new_width, new_height))
    #     photo = ImageTk.PhotoImage(image)
    #     label.config(image=photo)
    #     label.image = photo
    #
    # img = Image.open(sm)
    # copy_of_image = img.copy()
    # img = img.resize((200, 200), Image.LANCZOS)
    # #img = img.convert('L')
    # img = ImageTk.PhotoImage(img)
    # label = Label(window, image=img)
    # label.image = img
    # #label.bind('<Configure>', resize_image)
    # label.pack()
    # label.pack(side=LEFT)

    # imageHead = img
    # imageHand = Image.open('images/so.png')
    #
    # imageHead.paste(imageHand, (20, 40), imageHand)
    # # Convert the Image object into a TkPhoto object
    # tkimage = ImageTk.PhotoImage(imageHead)
    #
    # panel1 = Label(window, image=tkimage)
    # panel1.grid(row=0, column=2, sticky=E)
    moodrate = tk.Toplevel()
    window.withdraw()
    moodrate.attributes('-fullscreen', True)
    moodrate.title("Оценка состояния")
    moodrate.resizable(0, 0)

    def close():
        moodrate.destroy()
        window.deiconify()

    label = Label(moodrate, text="Оцените ваше текущее состояние в сфере:", font=("Arial", 24))
    label.pack()

    def addmood(num,file):
        f = open(f'files/{file}Mood.txt', 'a')
        f.write(f'{num} ')
        f.close()

    back = Button(
        moodrate,
        text='Назад',
        font='Impact 10',
        bg='black',
        fg='white',
        command=close
    )
    back.place(x=w - 67, y=5)

    imgcalm = PhotoImage(file='images/calm.png').subsample(2, 2)
    imgangry = PhotoImage(file='images/angry.png').subsample(2, 2)
    imgcool = PhotoImage(file='images/cool.png').subsample(2, 2)
    imghappy = PhotoImage(file='images/happy.png').subsample(2, 2)
    imgsad = PhotoImage(file='images/sad.png').subsample(2, 2)

    lable_sport = Label(moodrate, text="Спорт", font=("Arial", 20))
    lable_life = Label(moodrate, text="Личная жизнь", font=("Arial", 20))
    lable_family = Label(moodrate, text="Семья", font=("Arial", 20))

    lable_sport.place(x=150, y=100)
    lable_life.place(x=680, y=100)
    lable_family.place(x=1300, y=100)



    angry = Button(
        moodrate,
        image=imgangry,
        command=partial(addmood,'1','Sport')
    )

    angry.place(x=110,y=140)

    angry = Button(
        moodrate,
        image=imgangry,
        command=partial(addmood, '1', 'Life')
    )

    angry.place(x=690, y=140)

    angry = Button(
        moodrate,
        image=imgangry,
        command=partial(addmood, '1', 'Family')
    )

    angry.place(x=1265, y=140)

    sad = Button(
        moodrate,
        image=imgsad,
        command=partial(addmood,'2','Sport')
    )

    sad.place(x=110, y=320)

    sad = Button(
        moodrate,
        image=imgsad,
        command=partial(addmood, '2', 'Life')
    )

    sad.place(x=690, y=320)

    sad = Button(
        moodrate,
        image=imgsad,
        command=partial(addmood, '2', 'Family')
    )

    sad.place(x=1265, y=320)

    calm = Button(
        moodrate,
        image=imgcalm,
        command=partial(addmood,'3', 'Sport')
    )

    calm.place(x=110, y=320)

    calm = Button(
        moodrate,
        image=imgcalm,
        command=partial(addmood, '3', 'Life')
    )

    calm.place(x=690, y=320)

    calm = Button(
        moodrate,
        image=imgcalm,
        command=partial(addmood, '3', 'Family')
    )

    calm.place(x=1265, y=320)


    cool = Button(
        moodrate,
        image=imgcool,
        command=partial(addmood,'4', 'Sport')
    )

    cool.place(x=110, y=500)

    cool = Button(
        moodrate,
        image=imgcool,
        command=partial(addmood, '4', 'Life')
    )

    cool.place(x=690, y=500)

    cool = Button(
        moodrate,
        image=imgcool,
        command=partial(addmood, '4', 'Family')
    )

    cool.place(x=1265, y=500)

    happy = Button(
        moodrate,
        image=imghappy,
        command=partial(addmood,'5', 'Sport')
    )

    happy.place(x=110, y=680)

    happy = Button(
        moodrate,
        image=imghappy,
        command=partial(addmood, '5', 'Life')
    )

    happy.place(x=690, y=680)

    happy = Button(
        moodrate,
        image=imghappy,
        command=partial(addmood, '5', 'Family')
    )

    happy.place(x=1265, y=680)

    moodrate.mainloop()


def close():
    window.destroy()


'''def set_image(name):
    canvas.delete("all")
    #canvas.create_image(100, 115, image=image)
    img = Image.open(name)
    img.thumbnail((200, 200), Image.ANTIALIAS)
    return ImageTk.PhotoImage(img)

def set():
    set_image('фонjpeg.jpeg')

'''
w = window.winfo_screenwidth()
h = window.winfo_screenheight()

window.attributes("-fullscreen", True)

# canvas=Canvas(window,width=w,height=h)
# canvas.config(bg="#848470")
# canvas.pack()
# img = Image.open("images\фонjpeg.jpeg")
# img = img.resize((w,h),Image.LANCZOS)
# img = ImageTk.PhotoImage(img)
# canvas.create_image(0, 0, image=img, anchor="nw")
# window.geometry(f"{w}x{h}+0+0")


'''frame = Frame(
    window,
    padx=10,
    pady=10
)
frame.pack(expand=True)'''

'''newnote = Label(
    frame,
    text=" Ввести новую запись ",
)
newnote.grid(row=1, column=2)'''

#    #000064 - синий

sport = Button(
    window,
    text='Спорт',
    bg='#FF0000',
    font='Impact 20',
    fg='black',
    command=sport
)
personallife = Button(
    window,
    text='Личная жизнь',
    bg='#00FF00',
    font='Impact 20',
    fg='black',
    command=life
)

family = Button(
    window,
    text='Семья',
    bg='#FFFF00',
    font='Impact 20',
    fg='black',
    command=family
)

'''sport.grid(row=2, column=1, padx=10)
personallife.grid(row=2, column=2, padx=10)
family.grid(row=2, column=3, padx=10)'''

graphic = Button(
    window,
    text='График',
    font='Impact 18',
    bg='black',
    fg='white',
    command=graf
)
# graphic.grid(row=4, column=1, pady=20)

now = Button(
    window,
    text="Оценка текущего\nсостояния",
    font='Impact 18',
    bg='black',
    fg='white',
    # command=set
    command=smile
)
# now.grid(row=4, column=3)

close = Button(
    window,
    text="Закрыть",
    font='Impact 10',
    bg='black',
    fg='white',
    command=close
)
# now.grid(row=w, column=h)


sport.place(x=25, y=50)
family.place(x=25, y=150)
personallife.place(x=25, y=250)
graphic.place(x=10, y=h - 175)
now.place(x=10, y=h - 100)
close.place(x=w - 67, y=5)

window.mainloop()
