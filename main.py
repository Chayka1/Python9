import tkinter


class MyGUI:
    def __init__(self):
        self.main_window = tkinter.Tk()

        self.main_window.title('Мой первый GUI!')

        self.label_1 = tkinter.Label(self.main_window, text='Привет мир!')
        self.label_2 = tkinter.Label(self.main_window, text='Это моя программа!')

        self.label_1.pack()
        self.label_2.pack()

        tkinter.mainloop()


if __name__ == '__main__':
    my_gui = MyGUI()
