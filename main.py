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

window = Tk()
window.title("дневник")

columns = ("situation", "emotion", "think")


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

    back.place(x=w - 77, y=47)
    app.mainloop()


def life():
    app = demo("Life")
    app.attributes("-fullscreen", True)

    def close():
        wr(app, "Life")
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

def family():
    app = demo("Family")
    app.attributes("-fullscreen", True)

    def close():
        wr(app, "Family")
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

'''функция создающая окно в котором рисуются графики эмоц. состояния'''
def graf():
    grafwind = tk.Toplevel()
    grafwind.attributes("-fullscreen", True)
    grafwind['bg'] = '#D1C1B4'
    lable = Label(master=grafwind, text="Отследите изменение вашего эмоционального состояния",
                  font=("Impact", 24),
                  bg='#D1C1B4', fg='#4D220E')
    lable.pack()

    '''функция создающая график состояния. в качестве аргумента - файл из которого будет читаться информация'''
    def plot(file):
        places = {'SportMood': [50, 150], 'FamilyMood': [610, 150], 'LifeMood': [1180, 150], 'All': [610, 565]}

        fig = Figure(figsize=(3, 3),
                     dpi=100, facecolor='#D1C1B4')

        if file == 'All':
            sport = list(map(int, open(f'files/SportMood').read().split()))
            life = list(map(int, open(f'files/LifeMood').read().split()))
            family = list(map(int, open(f'files/FamilyMood').read().split()))
            all = [sport, life, family]
            for i in all:
                if i == []:
                    all.remove(i)
            data = list(map(statistics.mean, all))
        else:
            data = list(map(int, open(f'files/{file}').read().split()))

        plot1 = fig.add_subplot(111)
        plot1.set_facecolor('#DEB28D')
        plot1.plot(data, color='#4D220E')
        canvas = FigureCanvasTkAgg(fig,
                                   master=grafwind)
        canvas.draw()
        canvas.get_tk_widget().place(x=places[file][0], y=places[file][1])

    '''создание кнопок. каждая вызывает функцию построения графика с соответстующим аргументом'''
    plot_button_sport = Button(master=grafwind,
                               command=partial(plot, 'SportMood'),
                               height=2,
                               width=15,
                               bg='#DEB28D',
                               font='Impact 20',
                               fg='#4D220E',
                               text="Спорт")

    plot_button_sport.place(x=100, y=50)

    plot_button_family = Button(master=grafwind,
                                command=partial(plot, 'FamilyMood'),
                                height=2,
                                width=15,
                                bg='#DEB28D',
                                font='Impact 20',
                                fg='#4D220E',
                                text="Семья")

    plot_button_family.place(x=660, y=50)

    plot_button_life = Button(master=grafwind,
                              command=partial(plot, 'LifeMood'),
                              height=2,
                              width=15,
                              bg='#DEB28D',
                              font='Impact 20',
                              fg='#4D220E',
                              text="Личная жизнь")

    plot_button_life.place(x=1225, y=50)

    plot_button_all = Button(master=grafwind,
                             command=partial(plot, 'All'),
                             height=2,
                             width=15,
                             bg='#DEB28D',
                             font='Impact 20',
                             fg='#4D220E',
                             text="Общее\nсостояние")

    plot_button_all.place(x=660, y=475)

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

    grafwind.mainloop()


'''фцнкция создающая окно для выставления оценок эмоц. состояния'''
def smile():
    moodrate = tk.Toplevel()
    moodrate.attributes('-fullscreen', True)
    moodrate['bg'] = '#D1C1B4'
    moodrate.title("Оценка состояния")
    moodrate.resizable(0, 0)

    def close():
        moodrate.destroy()

    label = Label(moodrate, text="Оцените ваше текущее состояние в сфере:",
                  font=("Impact", 24),
                  bg='#D1C1B4',
                  fg='#4D220E')
    label.pack()

    '''функция добавляющая в файл новую оценку'''
    def addmood(num, file):
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

    '''создание переменных содержащих картинки определенного размера'''
    imgcalm = PhotoImage(file='images/calm_pr.png').subsample(3, 3)
    imgangry = PhotoImage(file='images/angry_pr.png').subsample(3, 3)
    imgcool = PhotoImage(file='images/cool_pr.png').subsample(3, 3)
    imghappy = PhotoImage(file='images/happy_pr.png').subsample(3, 3)
    imgsad = PhotoImage(file='images/sad_pr.png').subsample(3, 3)

    lable_sport = Label(moodrate, text="Спорт", font=("Impact", 20), bg='#D1C1B4', fg='#4D220E')
    lable_life = Label(moodrate, text="Личная жизнь", font=("Impact", 20), bg='#D1C1B4', fg='#4D220E')
    lable_family = Label(moodrate, text="Семья", font=("Impact", 20), bg='#D1C1B4', fg='#4D220E')

    lable_sport.place(x=150, y=75)
    lable_life.place(x=680, y=75)
    lable_family.place(x=1300, y=75)

    '''создание кнопок для оценки состояния каждая кнопка вызывает функцию 
       добавления в файл с сферой жизни соответсвующей оценки'''
    angry = Button(
        moodrate,
        bg='#D1C1B4',
        activebackground='#DEB28D',
        border=0,
        image=imgangry,
        command=partial(addmood, '1', 'Sport')
    )

    angry.place(x=20, y=130)

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
        command=partial(addmood, '2', 'Sport')
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
        command=partial(addmood, '3', 'Sport')
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

    cool = Button(
        moodrate,
        bg='#D1C1B4',
        activebackground='#DEB28D',
        border=0,
        image=imgcool,
        command=partial(addmood, '4', 'Sport')
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
        command=partial(addmood, '5', 'Sport')
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

'''создание главного окна программы'''
w = window.winfo_screenwidth()
h = window.winfo_screenheight()

window.attributes("-fullscreen", True)
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

graphic = Button(
    window,
    text='Графики состояния',
    font='Impact 18',
    bg='#AF8678',
    fg='#4D220E',
    command=graf
)

now = Button(
    window,
    text="Оценка текущего\nсостояния",
    font='Impact 18',
    bg='#AF8678',
    fg='#4D220E',
    command=smile
)

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

window.mainloop()
