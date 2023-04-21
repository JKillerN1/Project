import tkinter as tk
from tkinter import *
from tkinter import ttk

window = Tk()
window.title("дневник")

columns = ("situation","emotion","think")

def sport():
    sportwindow = Tk()
    window.withdraw()
    sportwindow.title("Сфера жизни: Спорт")

    sportwindow.geometry('800x400+{}+{}'.format(w // 2 - 400, h // 2 - 400))

    sportframe = Frame(
        sportwindow,
        padx=10,
        pady=10
    )

    def close():
        window.deiconify()
        sportwindow.destroy()

    sportframe.pack(anchor=NW)

    back = Button(
        sportframe,
        text='Назад',
        command=close
    )

    back.grid(row=1, column=1)

    set = ttk.Treeview(sportwindow)
    set.pack()

    set['columns'] = ('situation', 'emotion', 'think')
    set.column("#0", width=0, stretch=NO)
    set.column("situation", anchor=CENTER, width=200)
    set.column("emotion", anchor=CENTER, width=200)
    set.column("think", anchor=CENTER, width=200)

    set.heading("#0", text="", anchor=CENTER)
    set.heading("situation", text="Ситуация", anchor=CENTER)
    set.heading("emotion", text="Эмоции", anchor=CENTER)
    set.heading("think", text="Мысли", anchor=CENTER)

    sportdata = []

    for data in sportdata:
        set.insert(parent='', index='end', text='', values=(data[0], data[1], data[2]))

    input_frame = Frame(sportwindow)
    input_frame.pack()

    situation = Label(input_frame, text="Ситуация")
    situation.grid(row=0, column=0)

    emotion = Label(input_frame, text="Эмоции")
    emotion.grid(row=0, column=1, padx=10)

    think = Label(input_frame, text="Мысли")
    think.grid(row=0, column=2)

    situation_entry = Entry(input_frame)
    situation_entry.grid(row=1, column=0)

    emotion_entry = Entry(input_frame)
    emotion_entry.grid(row=1, column=1)

    think_entry = Entry(input_frame)
    think_entry.grid(row=1, column=2)

    def input_record():

        set.insert(parent='', index='end', text='',
                   values=(situation_entry.get(), emotion_entry.get(), think_entry.get()))
        sportdata.append([situation_entry.get(), emotion_entry.get(), think_entry.get()])

        situation_entry.delete(0, END)
        emotion_entry.delete(0, END)
        think_entry.delete(0, END)

    input_button = Button(sportwindow, text="Создать новую запись", command=input_record)

    input_button.pack()

    sportwindow.protocol("WM_DELETE_WINDOW", window.deiconify())

    sportwindow.mainloop()


w = window.winfo_screenwidth()
h = window.winfo_screenheight()

window.geometry('400x400+{}+{}'.format(w//2-200, h//2-200))

frame = Frame(
   window,
   padx=10,
   pady=10
)
frame.pack(expand=True)

newnote = Label(
   frame,
   text=" Ввести новую запись ",
)
newnote.grid(row=1, column=2)

sport = Button(
   frame,
   text='Спорт',
    command = sport
)
personallife = Button(
   frame,
   text='Личная жизнь',
)

family = Button(
   frame,
   text='Семья',
)

sport.grid(row=2, column=1,padx=10)
personallife.grid(row=2, column=2,padx=10)
family.grid(row=2, column=3,padx=10)



graphic = Button(
   frame,
   text='График',
)
graphic.grid(row=4, column=1,pady=20)

now = Label(
   frame,
   text="Оценка текущего\nсостояния",
)
now.grid(row=4, column=3)


window.mainloop()
