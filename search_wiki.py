from tkinter import *
import tkinter as tk
import wikipedia as wk
import wiki
from PIL import Image, ImageDraw
from PIL import ImageTk
import main

class search_wikipedia(tk.Frame):
    def __init__(self):
        self.root = Tk()
        self.root.title('Search Wikipedia')
        self.root.resizable(0, 0)
        self.root.iconbitmap('resources/dictionary.ico')
        tk.Frame.__init__(self, self.root)

        self.search_bar_window = Frame(self.root, width=500, height=70, bg='white')
        self.search_bar_window.pack()

        self.search_window = Frame(self.root, width=500, height=400, bg='white')
        self.search_window.pack()

        self.vcmd = (self.register(self.show_suggestions),'%P')

        self.bar = Entry(self.search_bar_window, width=40, fg='dark green', highlightthickness=3, highlightcolor='Green', validate='key', validatecommand=self.vcmd, font=('Arial', 13, 'bold'))
        self.bar.place(x=50, y=10)
        self.bar.focus()

        try:
            self.back = Image.open('resources/back.png') #pic
            self.back = self.back.resize((25, 25), Image.ANTIALIAS)
            self.back = ImageTk.PhotoImage(self.back)
            self.back_btn = Button(self.search_bar_window, image=self.back, bg='white', fg='black', command=self.back_to_main)
            self.back_btn.place(x=0, y=0)
        except:
            pass

        try:
            self.search = Image.open('resources/search.png') #pic
            self.search = self.search.resize((25, 25), Image.ANTIALIAS)
            self.search = ImageTk.PhotoImage(self.search)
            self.search_btn = Button(self.search_bar_window, image=self.search, bg='white', fg='black')
            self.search_btn.place(x=420, y=10)
        except:
            pass

    def show_suggestions(self, P):
        self.search_window.destroy()
        self.search_window = Frame(self.root, width=500, height=400, bg='white')
        self.search_window.propagate(0)
        self.search_window.pack()

        self.suggestions_lbl = Label(self.search_window, text='Suggestions', bg='white', fg='black', font=('Courier', 13, 'bold underline'))
        self.suggestions_lbl.pack()

        try:
            self.suggestions_list = wk.search(P)
            for i in range(8):
                self.sugg = Button(self.search_window, text=self.suggestions_list[i], cursor='hand2', width=30, relief=GROOVE, bg='light yellow', fg='dark blue', activebackground='light green', activeforeground='blue', font=('Verdana', 13, 'bold'))
                self.sugg.pack(pady=5)
                self.sugg['command'] = lambda question=self.suggestions_list[i]: self.open_wiki_ref(question)
        except:
            pass

        return True
    
    def open_wiki_ref(self, q):
        self.root.destroy()
        wiki.search_wiki(query=q)

    def back_to_main(self):
        self.root.destroy()
        main.main_window()


if __name__ == '__main__':
    obj = search_wikipedia()
    obj.root.mainloop()