<<<<<<< HEAD
import statistics
from functools import partial
from tkinter import *
from PIL import ImageTk, Image
import matplotlib
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure
from tksheet import Sheet
import tkinter as tk

matplotlib.use('TkAgg')
=======

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
>>>>>>> 5ddbe6181d6bb8f98984cefc4154c416969b1b9f

window = Tk()
window.title("дневник")

columns = ("situation", "emotion", "think")

<<<<<<< HEAD

class demo(tk.Tk):
    def __init__(self, name):
        tk.Tk.__init__(self)
        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(0, weight=1)
        self.frame = tk.Frame(self)
        self.frame.grid_columnconfigure(0, weight=1)
        self.frame.grid_rowconfigure(0, weight=1)
        self.data = ([[c for c in open(f'files/{name}').read().split("\n")[(r * 5 + r) - 6:r * 6 - 1]]
                      for r in range(1, open(f'files/{name}').read().split("\n").count('') + 1)])
        self.header = (['Дата', 'Ситуация', 'Эмоции', 'Мысли', 'Оценка'])
        self.sheet = Sheet(self.frame,
                           data=self.data,
                           header_bg='#566F5F',
                           header_fg='#4D220E',
                           table_bg='#D1C1B4',
                           table_fg='#4D220E',
                           font="Arial 14",
                           header_font="Impact 18",
                           empty_horizontal=1,
                           column_width=295,
                           empty_vertical=100,
                           expand_sheet_if_paste_too_big=True,
                           header_height='3',
                           max_column_width='200',
                           row_height='5',
                           headers=self.header
                           )
        self.sheet.enable_bindings()
        self.frame.grid(row=0, column=0, sticky="nswe")
        self.sheet.grid(row=0, column=0, sticky="nswe")

        self.sheet.create_header_dropdown(c=4,
                                          values=["1", "2", "3"],
                                          set_value="all",
                                          selection_function=self.header_dropdown_selected,
                                          text="Оценка"
                                          )

    def header_dropdown_selected(self, event=None):
        hdrs = self.sheet.headers()

        hdrs[event.column] = event.text

        rows = [rn for rn, row in enumerate(self.data) if hdrs[event.column] == row[-1]]

        self.sheet.display_rows(rows=rows,
                                all_displayed=False)
        self.sheet.redraw()


def wr(app, name):
    sheet_data = app.sheet.get_sheet_data(get_displayed=False,
                                          get_header=False,
                                          get_index=False,
                                          get_index_displayed=True,
                                          get_header_displayed=True,
                                          only_rows=None,
                                          only_columns=None)
    #функция удаляет появляющуюся надпись и кнопку с экрана
    def del_canv(canv):
        canvas.delete(canv)
        delete_canv.destroy()

    with open(f"files/{name}", "w") as f:
        for i in sheet_data:
            if i != [] and i != ['']:
                for k in i:
                    f.write(k)
                    f.write('\n')
                    #если оценка соответсует значениям то высвечиваются надписи и кнопка чтобы их убрать
                    try:
                        if int(k) < 3:
                            bad_news = canvas.create_text(300, 440)
                            canvas.itemconfig(bad_news, text="Вам стоит обсудить эту ситуацию с психологом",
                                                        font='Impact 20',
                                                        fill='#4D220E')
                            delete_canv = Button(
                                                window,
                                                text='Ок',
                                                bg='#DEB28D',
                                                font='Impact 20',
                                                fg='#4D220E',
                                                command=partial(del_canv, bad_news)
                                            )
                            delete_canv.place(x=300, y=460)
                        if int(k) > 7:
                            good_news = canvas.create_text(150, 440)
                            canvas.itemconfig(good_news, text="Мы очень рады за Вас!",
                                              font='Impact 20',
                                              fill='#4D220E')
                            delete_canv = Button(
                                window,
                                text='Ок',
                                bg='#DEB28D',
                                font='Impact 20',
                                fg='#4D220E',
                                command=partial(del_canv, good_news)
                            )
                            delete_canv.place(x=100, y=460)

                    except ValueError:
                        continue
                f.write('\n')


'''функция создания окна'''
def sport():
    app = demo("Sport")
    app.attributes("-fullscreen", True)
=======
from tksheet import Sheet
import tkinter as tk
import textwrap




'''def wrap(string, lenght=32):
    return '\n'.join(textwrap.wrap(string, lenght))


def win(sportwindow, name_file):
    sportwindow.geometry('1000x1000+{}+{}'.format(w // 2 - 400, h // 2 - 400))
    s = ttk.Style(sportwindow)
    s.theme_use('clam')
    s.configure('Treeview', rowheight= 50)


    sportframe = Frame(
        sportwindow,
        padx=10,
        pady=10
    )
>>>>>>> 5ddbe6181d6bb8f98984cefc4154c416969b1b9f

    def close():
        wr(app, "Sport")
        app.destroy()

    back = Button(
        app,
        text='Назад',
        font='Impact 10',
        bg='#D1C1B4',
        fg='white',
        command=close
    )

<<<<<<< HEAD
    back.place(x=w - 77, y=47)
    app.mainloop()


def life():
=======
    back.grid(row=1, column=1)

    set = ttk.Treeview(sportwindow, height = 10)
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

    #for data in sportdata:
     #   set.insert(parent='', index='end', text='', values=(data[0], data[1], data[2], data[3]))

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
                        values=list(map(wrap,i.split('!'))))
            #print(list(map(wrap,i.split('!'))))

    def input_record():
        if(int(mark_entry.get())<=2):
            lable = Label(master=sportwindow, text='Вам следует обсудить эту ситуацию с психологом')
            lable.pack()
        set.insert(parent='', index='end', text='',
                   values=(data_entry.get(), situation_entry.get(), emotion_entry.get(), think_entry.get(),
                           mark_entry.get()))
        sportdata.append([data_entry.get(), situation_entry.get(), emotion_entry.get(), think_entry.get(),
                          mark_entry.get()])

        with open(f"files/{name_file}", "a") as f:
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
    '''

class demo(tk.Tk):
    def __init__(self, name):
        tk.Tk.__init__(self)
        self.grid_columnconfigure(0, weight = 1)
        self.grid_rowconfigure(0, weight = 1)
        self.frame = tk.Frame(self)
        self.frame.grid_columnconfigure(0, weight = 1)
        self.frame.grid_rowconfigure(0, weight = 1)
        self.data = ([[c for c in open(f'files/{name}').read().split("\n")[(r*5+r)-6:r*6-1]]
                                   for r in range(1,open(f'files/{name}').read().split("\n").count('')+1)])
        self.header = (['Дата','Ситуация','Эмоции','Мысли','Оценка'])
        self.sheet = Sheet(self.frame,
                           data=self.data,
                           #theme="dark",
                           header_bg='#566F5F',
                           header_fg='#4D220E',
                           table_bg='#D1C1B4',
                           table_fg='#4D220E',
                           font ="Arial 14",
                           header_font="Impact 18",
                           #height=100,
                           empty_horizontal=1,
                           column_width=295,
                           empty_vertical=100,
                           expand_sheet_if_paste_too_big=True,
                           header_height='3',
                           max_column_width='200',
                           row_height='5',
                           headers=self.header
                           )
        #self.sheet.font(newfont=None)
        '''self.data =([[c for c in open(f'files/{name}').read().split("\n")[(r*5+r)-6:r*6-1]]
                                   for r in range(1,open('files/Sport').read().split("\n").count('')+1)])
        self.sheet = Sheet(self.frame,
                           data = self.data,
                           show_y_scrollbar = False,
                           #width=1025,
                           height=100,
                           empty_horizontal=1,
                           column_width=300 =()
                           empty_vertical=100,
                           expand_sheet_if_paste_too_big=True,
                           header_height='3',
                           max_column_width='200',
                           row_height='5',
                           headers=['Дата',
                            'Ситуация',
                            'Эмоции',
                            'Мысли',
                            'Оценка']
                           )'''

        #self.sheet.set_row_data(r, values=tuple(), add_columns=True, redraw=False)
        #self.sheet.insert_rows(rows: Union[list, int] = 1,
         #   idx: Union[str, int] = "end",
          #  heights = None,
           # deselect_all = False,
            #add_columns = True,
            #mod_row_positions = True,
            #redraw = True)

        self.sheet.enable_bindings()
        self.frame.grid(row=0, column=0, sticky="nswe")
        self.sheet.grid(row=0, column=0, sticky="nswe")

        '''self.sheet.highlight_cells(0,5,
                                   bg='#DEB28D',
                                   fg="white")'''

        #self.sheet.set_all_cell_sizes_to_text()

        #self.show_selections = tk.Label(self)

        self.sheet.create_header_dropdown(c=4,
                                          values=[ "1", "2", "3"],
                                          set_value="all",
                                          selection_function=self.header_dropdown_selected,
                                          text="Оценка"
                                          )


    def header_dropdown_selected(self, event=None):
        hdrs = self.sheet.headers()

        hdrs[event.column] = event.text

        '''for dd in hdrs:
            if dd =="all":
                print(111111111)
                r = [rn for rn, row in enumerate(self.data) ]
                self.sheet.display_rows(rows=[2, 4, 7], all_displayed = False)



        else:'''
        rows = [rn for rn, row in enumerate(self.data) if hdrs[event.column]==row[-1]]

        self.sheet.display_rows(rows=rows,
                                all_displayed=False)
        self.sheet.redraw()







def wr(app,name):
    aaa = app.sheet.get_sheet_data(get_displayed=False,
                                   get_header=False,
                                   get_index=False,
                                   get_index_displayed=True,
                                   get_header_displayed=True,
                                   only_rows=None,
                                   only_columns=None)

    with open(f"files/{name}", "w") as f:
        for i in aaa:
            if i != [] and i != ['']:
                for k in i:
                    f.write(k)
                    f.write('\n')
                f.write('\n')



def sport():
    '''sportwindow = Tk()
    window.withdraw()
    sportwindow.title("Сфера жизни: Спорт")
    win(sportwindow, "Sport")
    '''

    app = demo("Sport")
   # print(wr(app, "Sport"))
    #print(wr(app, "Sport"))
    app.attributes("-fullscreen", True)

    def close():
        #window.deiconify()
        app.destroy()

    back = Button(
        app,
        text='Назад',
        font='Impact 10',
        bg='#D1C1B4',
        fg='white',
        command=close
    )


    back.place(x=w - 77, y=47)

    #print(wr(app, "Sport"))
    app.mainloop()
    wr(app, "Sport")
    #app.destroy()
    #print(wr(app, "Sport"))





def life():
    '''lifew = Tk()
    window.withdraw()
    lifew.title("Сфера жизни: Личная жизнь")
    win(lifew, "Life")'''
>>>>>>> 5ddbe6181d6bb8f98984cefc4154c416969b1b9f
    app = demo("Life")
    app.attributes("-fullscreen", True)

    def close():
<<<<<<< HEAD
        wr(app, "Life")
=======
        # window.deiconify()
>>>>>>> 5ddbe6181d6bb8f98984cefc4154c416969b1b9f
        app.destroy()

    back = Button(
        app,
        text='Назад',
        font='Impact 10',
        bg='#D1C1B4',
        fg='white',
        command=close
    )

    back.place(x=w - 77, y=47)
    app.mainloop()
<<<<<<< HEAD

def family():
=======
    wr(app,"Life")


def family():
    '''familyw = Tk()
    window.withdraw()
    familyw.title("Сфера жизни: Семья")
    win(familyw, "Family")'''
>>>>>>> 5ddbe6181d6bb8f98984cefc4154c416969b1b9f
    app = demo("Family")
    app.attributes("-fullscreen", True)

    def close():
<<<<<<< HEAD
        wr(app, "Family")
=======
        # window.deiconify()
>>>>>>> 5ddbe6181d6bb8f98984cefc4154c416969b1b9f
        app.destroy()

    back = Button(
        app,
        text='Назад',
        font='Impact 10',
        bg='#D1C1B4',
        fg='white',
        command=close
    )

    back.place(x=w - 77, y=47)
    app.mainloop()
<<<<<<< HEAD

'''функция создающая окно в котором рисуются графики эмоц. состояния'''
=======
    wr(app,"Family")


>>>>>>> 5ddbe6181d6bb8f98984cefc4154c416969b1b9f
def graf():
    grafwind = tk.Toplevel()
    grafwind.attributes("-fullscreen", True)
    grafwind['bg'] = '#D1C1B4'
    lable = Label(master=grafwind, text="Отследите изменение вашего эмоционального состояния",
                  font=("Impact", 24),
<<<<<<< HEAD
                  bg='#D1C1B4', fg='#4D220E')
    lable.pack()

    '''функция создающая график состояния. в качестве аргумента - файл из которого будет читаться информация'''
    def plot(file):
        places = {'SportMood': [50, 150], 'FamilyMood': [610, 150], 'LifeMood': [1180, 150], 'All': [610, 565]}

        fig = Figure(figsize=(3, 3),
                     dpi=100, facecolor='#D1C1B4')
=======
                  bg='#D1C1B4',fg='#4D220E')
    lable.pack()

    def plot(file):
        places = {'SportMood': [50,150],'FamilyMood': [610,150],'LifeMood': [1180,150],'All': [610,565]}

        fig = Figure(figsize=(3, 3),
                     dpi=100,facecolor='#D1C1B4')
>>>>>>> 5ddbe6181d6bb8f98984cefc4154c416969b1b9f

        if file == 'All':
            sport = list(map(int, open(f'files/SportMood').read().split()))
            life = list(map(int, open(f'files/LifeMood').read().split()))
            family = list(map(int, open(f'files/FamilyMood').read().split()))
            all = [sport, life, family]
            for i in all:
<<<<<<< HEAD
                if i == []:
                    all.remove(i)
            data = list(map(statistics.mean, all))
=======
                if i==[]:
                    all.remove(i)
            data = list(map(statistics.mean, all))
            #print(data)
>>>>>>> 5ddbe6181d6bb8f98984cefc4154c416969b1b9f
        else:
            data = list(map(int, open(f'files/{file}').read().split()))

        plot1 = fig.add_subplot(111)
<<<<<<< HEAD
        plot1.set_facecolor('#DEB28D')
        plot1.plot(data, color='#4D220E')
        canvas = FigureCanvasTkAgg(fig,
                                   master=grafwind)
        canvas.draw()
        canvas.get_tk_widget().place(x=places[file][0], y=places[file][1])

    '''создание кнопок. каждая вызывает функцию построения графика с соответстующим аргументом'''
    plot_button_sport = Button(master=grafwind,
                               command=partial(plot, 'SportMood'),
=======

        plot1.plot(data)
        canvas = FigureCanvasTkAgg(fig,
                                   master=grafwind)
        canvas.draw()
        #canvas.get_tk_widget().configure(bg='black')
        canvas.get_tk_widget().place(x=places[file][0],y=places[file][1])

        '''toolbar = NavigationToolbar2Tk(canvas,
                                      grafwind)
        toolbar.set_message(False)
        toolbar.config(background='black')
        toolbar._message_label.config(background='black')
        toolbar.lift()
        toolbar.pack(side=tk.X)


        toolbar.update()'''

        #canvas.get_tk_widget().place(x=places[file][0],y=places[file][1])

    plot_button_sport = Button(master=grafwind,
                         command=partial(plot, 'SportMood'),
>>>>>>> 5ddbe6181d6bb8f98984cefc4154c416969b1b9f
                               height=2,
                               width=15,
                               bg='#DEB28D',
                               font='Impact 20',
                               fg='#4D220E',
<<<<<<< HEAD
                               text="Спорт")
=======
                         text="Plot sport")
>>>>>>> 5ddbe6181d6bb8f98984cefc4154c416969b1b9f

    plot_button_sport.place(x=100, y=50)

    plot_button_family = Button(master=grafwind,
<<<<<<< HEAD
                                command=partial(plot, 'FamilyMood'),
=======
                               command=partial(plot, 'FamilyMood'),
>>>>>>> 5ddbe6181d6bb8f98984cefc4154c416969b1b9f
                                height=2,
                                width=15,
                                bg='#DEB28D',
                                font='Impact 20',
                                fg='#4D220E',
<<<<<<< HEAD
                                text="Семья")
=======
                               text="Plot family")
>>>>>>> 5ddbe6181d6bb8f98984cefc4154c416969b1b9f

    plot_button_family.place(x=660, y=50)

    plot_button_life = Button(master=grafwind,
<<<<<<< HEAD
                              command=partial(plot, 'LifeMood'),
=======
                               command=partial(plot, 'LifeMood'),
>>>>>>> 5ddbe6181d6bb8f98984cefc4154c416969b1b9f
                              height=2,
                              width=15,
                              bg='#DEB28D',
                              font='Impact 20',
                              fg='#4D220E',
<<<<<<< HEAD
                              text="Личная жизнь")
=======
                               text="Plot life")
>>>>>>> 5ddbe6181d6bb8f98984cefc4154c416969b1b9f

    plot_button_life.place(x=1225, y=50)

    plot_button_all = Button(master=grafwind,
<<<<<<< HEAD
                             command=partial(plot, 'All'),
=======
                                command=partial(plot, 'All'),
>>>>>>> 5ddbe6181d6bb8f98984cefc4154c416969b1b9f
                             height=2,
                             width=15,
                             bg='#DEB28D',
                             font='Impact 20',
                             fg='#4D220E',
<<<<<<< HEAD
                             text="Общее\nсостояние")

    plot_button_all.place(x=660, y=475)

=======
                                text="Plot all")

    plot_button_all.place(x=660, y=475)

    '''grafframe = Frame(
        grafwind,
        padx=10,
        pady=10
    )'''

    # grafframe.pack(anchor=CENTER)
>>>>>>> 5ddbe6181d6bb8f98984cefc4154c416969b1b9f
    def close():
        window.deiconify()
        grafwind.destroy()

    back = Button(
        grafwind,
        text='Назад',
        font='Impact 10',
        bg='#DEB28D',
        fg='#4D220E',
        command=close
    )

    back.place(x=w - 67, y=5)

<<<<<<< HEAD
    grafwind.mainloop()


'''фцнкция создающая окно для выставления оценок эмоц. состояния'''
def smile():
    moodrate = tk.Toplevel()
=======
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
    #window.withdraw()
>>>>>>> 5ddbe6181d6bb8f98984cefc4154c416969b1b9f
    moodrate.attributes('-fullscreen', True)
    moodrate['bg'] = '#D1C1B4'
    moodrate.title("Оценка состояния")
    moodrate.resizable(0, 0)

    def close():
        moodrate.destroy()
<<<<<<< HEAD

    label = Label(moodrate, text="Оцените ваше текущее состояние в сфере:",
                  font=("Impact", 24),
                  bg='#D1C1B4',
                  fg='#4D220E')
    label.pack()

    '''функция добавляющая в файл новую оценку'''
    def addmood(num, file):
=======
        #window.deiconify()

    label = Label(moodrate, text="Оцените ваше текущее состояние в сфере:", font=("Impact", 24),bg='#D1C1B4',fg='#4D220E')
    label.pack()

    def addmood(num,file):
>>>>>>> 5ddbe6181d6bb8f98984cefc4154c416969b1b9f
        f = open(f'files/{file}Mood', 'a')
        f.write(f'{num} ')
        f.close()

    back = Button(
        moodrate,
        text='Назад',
        font='Impact 10',
        bg='#DEB28D',
        fg='#4D220E',
        command=close
    )
    back.place(x=w - 67, y=5)

<<<<<<< HEAD
    '''создание переменных содержащих картинки определенного размера'''
=======
>>>>>>> 5ddbe6181d6bb8f98984cefc4154c416969b1b9f
    imgcalm = PhotoImage(file='images/calm_pr.png').subsample(3, 3)
    imgangry = PhotoImage(file='images/angry_pr.png').subsample(3, 3)
    imgcool = PhotoImage(file='images/cool_pr.png').subsample(3, 3)
    imghappy = PhotoImage(file='images/happy_pr.png').subsample(3, 3)
    imgsad = PhotoImage(file='images/sad_pr.png').subsample(3, 3)

<<<<<<< HEAD
    lable_sport = Label(moodrate, text="Спорт", font=("Impact", 20), bg='#D1C1B4', fg='#4D220E')
    lable_life = Label(moodrate, text="Личная жизнь", font=("Impact", 20), bg='#D1C1B4', fg='#4D220E')
    lable_family = Label(moodrate, text="Семья", font=("Impact", 20), bg='#D1C1B4', fg='#4D220E')
=======
    lable_sport = Label(moodrate, text="Спорт", font=("Impact", 20),bg='#D1C1B4',fg='#4D220E')
    lable_life = Label(moodrate, text="Личная жизнь", font=("Impact", 20),bg='#D1C1B4',fg='#4D220E')
    lable_family = Label(moodrate, text="Семья", font=("Impact", 20),bg='#D1C1B4',fg='#4D220E')
>>>>>>> 5ddbe6181d6bb8f98984cefc4154c416969b1b9f

    lable_sport.place(x=150, y=75)
    lable_life.place(x=680, y=75)
    lable_family.place(x=1300, y=75)

<<<<<<< HEAD
    '''создание кнопок для оценки состояния каждая кнопка вызывает функцию 
       добавления в файл с сферой жизни соответсвующей оценки'''
    angry = Button(
=======


    angry =  Button(
>>>>>>> 5ddbe6181d6bb8f98984cefc4154c416969b1b9f
        moodrate,
        bg='#D1C1B4',
        activebackground='#DEB28D',
        border=0,
        image=imgangry,
<<<<<<< HEAD
        command=partial(addmood, '1', 'Sport')
    )

    angry.place(x=20, y=130)
=======
        command=partial(addmood,'1','Sport')
    )

    angry.place(x=20,y=130)
>>>>>>> 5ddbe6181d6bb8f98984cefc4154c416969b1b9f

    angry = Button(
        moodrate,
        bg='#D1C1B4',
        activebackground='#DEB28D',
        border=0,
        image=imgangry,
        command=partial(addmood, '1', 'Life')
    )

    angry.place(x=600, y=130)

    angry = Button(
        moodrate,
        bg='#D1C1B4',
        activebackground='#DEB28D',
        border=0,
        image=imgangry,
        command=partial(addmood, '1', 'Family')
    )

    angry.place(x=1175, y=130)

    sad = Button(
        moodrate,
        bg='#D1C1B4',
        activebackground='#DEB28D',
        border=0,
        image=imgsad,
<<<<<<< HEAD
        command=partial(addmood, '2', 'Sport')
=======
        command=partial(addmood,'2','Sport')
>>>>>>> 5ddbe6181d6bb8f98984cefc4154c416969b1b9f
    )

    sad.place(x=195, y=250)

    sad = Button(
        moodrate,
        bg='#D1C1B4',
        activebackground='#DEB28D',
        border=0,
        image=imgsad,
        command=partial(addmood, '2', 'Life')
    )

    sad.place(x=775, y=250)

    sad = Button(
        moodrate,
        bg='#D1C1B4',
        activebackground='#DEB28D',
        border=0,
        image=imgsad,
        command=partial(addmood, '2', 'Family')
    )

    sad.place(x=1350, y=250)

    calm = Button(
        moodrate,
        bg='#D1C1B4',
        activebackground='#DEB28D',
        border=0,
        image=imgcalm,
<<<<<<< HEAD
        command=partial(addmood, '3', 'Sport')
=======
        command=partial(addmood,'3', 'Sport')
>>>>>>> 5ddbe6181d6bb8f98984cefc4154c416969b1b9f
    )

    calm.place(x=20, y=400)

    calm = Button(
        moodrate,
        bg='#D1C1B4',
        activebackground='#DEB28D',
        border=0,
        image=imgcalm,
        command=partial(addmood, '3', 'Life')
    )

    calm.place(x=600, y=400)

    calm = Button(
        moodrate,
        bg='#D1C1B4',
        activebackground='#DEB28D',
        border=0,
        image=imgcalm,
        command=partial(addmood, '3', 'Family')
    )

    calm.place(x=1175, y=400)

<<<<<<< HEAD
=======

>>>>>>> 5ddbe6181d6bb8f98984cefc4154c416969b1b9f
    cool = Button(
        moodrate,
        bg='#D1C1B4',
        activebackground='#DEB28D',
        border=0,
        image=imgcool,
<<<<<<< HEAD
        command=partial(addmood, '4', 'Sport')
=======
        command=partial(addmood,'4', 'Sport')
>>>>>>> 5ddbe6181d6bb8f98984cefc4154c416969b1b9f
    )

    cool.place(x=215, y=500)

    cool = Button(
        moodrate,
        bg='#D1C1B4',
        activebackground='#DEB28D',
        border=0,
        image=imgcool,
        command=partial(addmood, '4', 'Life')
    )

    cool.place(x=795, y=500)

    cool = Button(
        moodrate,
        bg='#D1C1B4',
        activebackground='#DEB28D',
        border=0,
        image=imgcool,
        command=partial(addmood, '4', 'Family')
    )

    cool.place(x=1360, y=500)

    happy = Button(
        moodrate,
        bg='#D1C1B4',
        activebackground='#DEB28D',
        border=0,
        image=imghappy,
<<<<<<< HEAD
        command=partial(addmood, '5', 'Sport')
=======
        command=partial(addmood,'5', 'Sport')
>>>>>>> 5ddbe6181d6bb8f98984cefc4154c416969b1b9f
    )

    happy.place(x=110, y=680)

    happy = Button(
        moodrate,
        bg='#D1C1B4',
        activebackground='#DEB28D',
        border=0,
        image=imghappy,
        command=partial(addmood, '5', 'Life')
    )

    happy.place(x=690, y=680)

    happy = Button(
        moodrate,
        bg='#D1C1B4',
        activebackground='#DEB28D',
        border=0,
        image=imghappy,
        command=partial(addmood, '5', 'Family')
    )

    happy.place(x=1265, y=680)

    moodrate.mainloop()


def close():
    window.destroy()

<<<<<<< HEAD
'''создание главного окна программы'''
=======

'''def set_image(name):
    canvas.delete("all")
    #canvas.create_image(100, 115, image=image)
    img = Image.open(name)
    img.thumbnail((200, 200), Image.ANTIALIAS)
    return ImageTk.PhotoImage(img)

def set():
    set_image('фонjpeg.jpeg')

'''
>>>>>>> 5ddbe6181d6bb8f98984cefc4154c416969b1b9f
w = window.winfo_screenwidth()
h = window.winfo_screenheight()

window.attributes("-fullscreen", True)
<<<<<<< HEAD
window['bg'] = '#D1C1B4'

canvas = Canvas(window, width=w, height=h)
canvas.config(bg="#848470")
canvas.pack()
img = Image.open("img.png")
img = img.resize((w, h), Image.LANCZOS)
img = ImageTk.PhotoImage(img)
canvas.create_image(0, 0, image=img, anchor="nw")
window.geometry(f"{w}x{h}+0+0")
canvas_id = canvas.create_text(350, 20)
canvas.itemconfig(canvas_id, text="Выберите сферу жизни, куда хотите добавить заметку")
canvas.itemconfig(canvas_id, font='Impact 20')
canvas.itemconfig(canvas_id, fill='#4D220E')
=======
window['bg']='#D1C1B4'

canvas=Canvas(window,width=w,height=h)
canvas.config(bg="#848470")
canvas.pack()
img = Image.open("img.png")
img = img.resize((w,h),Image.LANCZOS)
img = ImageTk.PhotoImage(img)
canvas.create_image(0, 0, image=img, anchor="nw")
window.geometry(f"{w}x{h}+0+0")


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
>>>>>>> 5ddbe6181d6bb8f98984cefc4154c416969b1b9f

'''создание кнопок отвечающих за переход на соответствующую возможность программы'''
sport = Button(
    window,
    text='Спорт',
    bg='#DEB28D',
    font='Impact 20',
    fg='#4D220E',
    command=sport
)

personallife = Button(
    window,
    text='Личная жизнь',
    bg='#DEB28D',
    font='Impact 20',
    fg='#4D220E',
    command=life
)

family = Button(
    window,
    text='Семья',
    bg='#DEB28D',
    font='Impact 20',
    fg='#4D220E',
    command=family
)

<<<<<<< HEAD
graphic = Button(
    window,
    text='Графики состояния',
=======
'''sport.grid(row=2, column=1, padx=10)
personallife.grid(row=2, column=2, padx=10)
family.grid(row=2, column=3, padx=10)'''

graphic = Button(
    window,
    text='График',
>>>>>>> 5ddbe6181d6bb8f98984cefc4154c416969b1b9f
    font='Impact 18',
    bg='#AF8678',
    fg='#4D220E',
    command=graf
)
<<<<<<< HEAD
=======
# graphic.grid(row=4, column=1, pady=20)
>>>>>>> 5ddbe6181d6bb8f98984cefc4154c416969b1b9f

now = Button(
    window,
    text="Оценка текущего\nсостояния",
    font='Impact 18',
    bg='#AF8678',
    fg='#4D220E',
<<<<<<< HEAD
    command=smile
)
=======
    # command=set
    command=smile
)
# now.grid(row=4, column=3)

close = Button(
    window,
    text="Закрыть",
    font='Impact 10',
    bg='#DEB28D',
    fg='#4D220E',
    command=close
)
# now.grid(row=w, column=h)
>>>>>>> 5ddbe6181d6bb8f98984cefc4154c416969b1b9f

close = Button(
    window,
    text="Закрыть",
    font='Impact 10',
    bg='#DEB28D',
    fg='#4D220E',
    command=close
)

sport.place(x=25, y=50)
family.place(x=25, y=150)
personallife.place(x=25, y=250)
graphic.place(x=10, y=h - 175)
now.place(x=10, y=h - 100)
close.place(x=w - 67, y=5)

sport.place(x=25, y=50)
family.place(x=25, y=150)
personallife.place(x=25, y=250)
graphic.place(x=10, y=h - 175)
now.place(x=10, y=h - 100)
close.place(x=w - 67, y=5)

window.mainloop()