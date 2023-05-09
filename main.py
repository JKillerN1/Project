import tkinter as tk
import os
from tkinter import *
from tkinter import ttk
from PIL import ImageTk, Image
import numpy as np
import matplotlib.pyplot as plt

window = Tk()
window.title("дневник")

columns = ("situation", "emotion", "think")

def win(sportwindow, name_file):
    sportwindow.geometry('800x400+{}+{}'.format(w // 2 - 400, h // 2 - 400))

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

    with open(f"files/{name_file}", "r") as f:
        for i in f.readlines():
            set.insert(parent='', index='end', text='',
                       values=i)

    def input_record():
        set.insert(parent='', index='end', text='',
                   values=(data_entry.get(), situation_entry.get(), emotion_entry.get(), think_entry.get(),
                           mark_entry.get()))
        sportdata.append([data_entry.get(), situation_entry.get(), emotion_entry.get(), think_entry.get(),
                          mark_entry.get()])

        with open(f"files/{name_file}", "a") as f:
            for x in sportdata:
                for y in x:
                    f.write(y)
                    f.write(" ")
                f.write("\n")

        data_entry.delete(0,END)
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
    win(sportwindow,"Sport")

def life():
    lifew = Tk()
    window.withdraw()
    lifew.title("Сфера жизни: Личная жизнь")
    win(lifew,"Life")

def family():
    familyw = Tk()
    window.withdraw()
    familyw.title("Сфера жизни: Семья")
    win(familyw, "Family")




def graf():
    grafwind = Tk()
    window.withdraw()
    grafwind.title("Графики")
    grafwind.geometry('800x400+{}+{}'.format(w // 2 - 400, h // 2 - 400))

    grafframe = Frame(
        grafwind,
        padx=10,
        pady=10
    )

    grafframe.pack(anchor=CENTER)

    spisok = []
    for filename in os.listdir("files"):
        new_lst = {}
        with open(os.path.join("files", filename), 'r') as f:
            text = f.read()
            lines = sum(1 for line in text.split('\n'))
            if lines>30:
                tab=text.split('\n')[-30:]
            else:
                tab=text.split('\n')
            for item in tab:
                if len(item.split(" ")) > 1:
                    new_lst[item.split(" ")[0]] = int(item.split(" ")[-2]) \
                        if item.split(" ")[-2] in ['1','2','3'] else item.split(" ")[-2]
            spisok.append(new_lst)


    def draw(data):
        names = list(data.keys())
        values = list(data.values())
        with plt.rc_context({'xtick.color': 'white'}):
            fig, axs = plt.subplots(1, 2, figsize=(10, 3), sharey=True)
            axs[0].bar(names, values)
            # axs[1].scatter(names, values)
            axs[1].plot(names, values)
        # fig.suptitle('Categorical Plotting')
        plt.yticks(np.arange(1,4,1))
        plt.show()


    def sport_graf():
        data = spisok[2]
        draw(data)

    def life_graf():
        data = spisok[1]
        draw(data)

    def family_graf():
        data = spisok[0]
        draw(data)

    sport1 = Button(
        grafframe,
        text='Спорт',
        command=sport_graf
    )
    life1 = Button(
        grafframe,
        text='Личная жизнь',
        command=life_graf
    )
    family11 = Button(
        grafframe,
        text='Семья',
        command=family_graf
    )

    def close():
        window.deiconify()
        grafwind.destroy()

    back = Button(
        grafframe,
        text='Назад',
        command=close
    )

    sport1.grid(row=2, column=1, padx=10)
    life1.grid(row=2, column=2, padx=10)
    family11.grid(row=2, column=3, padx=10)
    back.grid(row=2, column=0, padx=10)

    grafwind.mainloop()


w = window.winfo_screenwidth()
h = window.winfo_screenheight()

window.geometry('400x400+{}+{}'.format(w // 2 - 200, h // 2 - 200))

frame = Frame(
    window,
    padx=10,
    pady=10
)
frame.pack(expand=True)

'''newnote = Label(
    frame,
    text=" Ввести новую запись ",
)
newnote.grid(row=1, column=2)'''

sport = Button(
    frame,
    text='Спорт',
    command=sport
)
personallife = Button(
    frame,
    text='Личная жизнь',
    command=life
)

family = Button(
    frame,
    text='Семья',
    command=family
)

sport.grid(row=2, column=1, padx=10)
personallife.grid(row=2, column=2, padx=10)
family.grid(row=2, column=3, padx=10)

graphic = Button(
    frame,
    text='График',
    command=graf
)
graphic.grid(row=4, column=1, pady=20)

now = Label(
    frame,
    text="Оценка текущего\nсостояния",
)
now.grid(row=4, column=3)

window.mainloop()



'''spisok=[]
for filename in os.listdir("files"):
    new_lst={}
    with open(os.path.join("files", filename), 'r') as f:
        text = f.read()
        for item in text.split('\n'):
            new_lst[item.split(" ")[0]]=item.split(" ")[-1]
            print(int(item.split(" ")[-1]) if item.split(" ")[-1] in ['1','2','3'] else item.split(" ")[-1])

        spisok.append(new_lst)
print(spisok)
'''
