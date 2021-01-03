from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import main

class notifications:
    def __init__(self):
        self.root = Tk()
        self.root.title('Notifications Settings')
        self.root.resizable(0, 0)
        self.root.iconbitmap('resources/dictionary.ico')

        self.notify = Frame(self.root, width=400, height=200, bg='white')
        self.notify.propagate(0)
        self.notify.pack()

        self.head = Label(self.notify, text='Notifications', bg='white', fg='dark blue', font=('Cooper Black', 17))
        self.head.pack()

        self.info = Label(self.notify, text='Get notified of meanings of random words after every interval..', bg='white', fg='dark green', font=('Times new roman', 12))
        self.info.place(x=10, y=40)

        self.choose_interval_lbl = Label(self.notify, text='Choose interval: ', bg='white', fg='black', font=('Georgia', 14, 'bold'))
        self.choose_interval_lbl.place(x=10, y=100)

        self.n = StringVar()
        self.choose_interval = ttk.Combobox(self.notify, width=24, textvariable=self.n)
        self.vals = ['Never', '5 minutes', '10 minutes', '30 minutes', '1 hour', '2 hours', '1 day']
        self.choose_interval['values'] = self.vals
        self.choose_interval.place(x=200, y=105)

        self.save = Button(self.notify, text='Save', bg='light yellow', fg='dark blue', width=10, cursor='hand2', font=('Arial', 13, 'bold'), command=self.save_details)
        self.save.place(x=20, y=160)

        self.back = Button(self.notify, text='Back', bg='light yellow', fg='dark blue', width=10, cursor='hand2', font=('Arial', 13, 'bold'), command=self.back_to_main)
        self.back.place(x=150, y=160)

        self.exit = Button(self.notify, text='Exit', bg='light yellow', fg='dark blue', width=10, cursor='hand2', font=('Arial', 13, 'bold'), command=self.root.destroy)
        self.exit.place(x=280, y=160)

        try:
            self.f = open('resources/time.txt', 'r')
            self.content = (self.f.read()).strip()
            self.f.close()
            self.index = self.vals.index(self.content)
            self.choose_interval.current(self.index)
        except:
            pass
        self.root.mainloop()

    def back_to_main(self):
        self.root.destroy()
        main.main_window()

    def save_details(self):
        self.file = open('resources/time.txt', 'w')
        self.given = self.n.get()
        print(self.given)
        self.file.write(self.given)
        self.file.close()
        messagebox.showinfo('Details saved', 'Time interval saved successfully')
        self.root.destroy()
        main.main_window()

if __name__ == '__main__':
    obj = notifications()