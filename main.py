import tkinter
import tkinter.messagebox


def test1():
    class MyGUI:
        def __init__(self):
            self.main_window = tkinter.Tk()

            self.my_button = tkinter.Button(self.main_window,
                                            text='Нажми на меня!',
                                            command=self.do_something)

            self.quit_button = tkinter.Button(self.main_window,
                                              text='Выйти!',
                                              command=self.main_window.destroy)

            self.my_button.pack()
            self.quit_button.pack()

            tkinter.mainloop()

        def do_something(self):
            tkinter.messagebox.showinfo('Реакция',
                                        'Благодарю, что нажали кнопку!')

    my_gui = MyGUI()


def test2():
    class KiloConverterGUI:
        def __init__(self):
            self.main_window = tkinter.Tk()

            self.top_frame = tkinter.Frame(self.main_window)
            self.bottom_frame = tkinter.Frame(self.main_window)

            self.prompt_label = tkinter.Label(self.top_frame,
                                              text='Введите растояние в километрах: ')
            self.kilo_entry = tkinter.Entry(self.top_frame,
                                            width=10)

            self.prompt_label.pack(side='left')
            self.kilo_entry.pack(side='left')

            self.calc_button = tkinter.Button(self.bottom_frame, text='Переобразовать',
                                              command=self.convert)
            self.quit_button = tkinter.Button(self.bottom_frame,
                                              text='Выйти',
                                              command=self.main_window.destroy)

            self.calc_button.pack(side='left')
            self.quit_button.pack(side='left')

            self.top_frame.pack()
            self.bottom_frame.pack()

            tkinter.mainloop()

        def convert(self):
            kilo = float(self.kilo_entry.get())

            miles = kilo * 0.6214

            tkinter.messagebox.showinfo('Результаты',
                                        str(kilo)+
                                        ' километров эквивалентно ' +
                                        str(miles) + ' милям.')

    kilo_conv = KiloConverterGUI()


if __name__ == '__main__':
    test2()