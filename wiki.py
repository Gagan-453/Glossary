from tkinter import *
import wikipedia as wk
import search_wiki as sw
import webbrowser as wb
from PIL import Image, ImageDraw
from PIL import ImageTk
import main

class search_wiki:
    def __init__(self, query):
        self.query = query
        self.root = Tk()
        self.root.title('Wikipedia - ' + query)
        self.root.resizable(0, 0)
        self.root.iconbitmap('resources/dictionary.ico')

        self.wiki_window = Frame(self.root, width=500, height=500, bg='white')
        self.wiki_window.propagate(0)
        self.wiki_window.pack()

        self.topic = Label(self.wiki_window, text=query, bg='white', fg='dark blue', font=('Cambria', 16, 'bold italic'))
        self.topic.place(x=10, y=10)

        self.show_summary = Text(self.wiki_window, width=50, height=15, bd=5, wrap=WORD, font=('Calibri', 13))
        self.show_summary.place(x=10, y=50)
        self.show_summary.propagate(0)
        self.vsb = Scrollbar(self.show_summary, orient=VERTICAL, command=self.show_summary.yview)
        self.show_summary.config(yscrollcommand=self.vsb.set)
        self.vsb.pack(side=RIGHT, fill=Y)

        try:
            self.home = Image.open('resources/home.png') #pic
            self.home = self.home.resize((30, 30), Image.ANTIALIAS)
            self.home = ImageTk.PhotoImage(self.home)
            self.home_btn = Button(self.wiki_window, image=self.home, text=' Home', bg='white', fg='#440D64', relief=FLAT, compound=LEFT, font=('Arial', 14, 'bold'), command=self.back_to_home)
            self.home_btn.place(x=0, y=460)
        except:
            pass

        try:
            self.info = wk.summary(query)
            self.show_summary.insert(END, self.info)
            self.show_summary.config(state=DISABLED)
        except:
            self.show_summary.insert(END, 'No articles found...')
            self.show_summary.config(state=DISABLED)

        try:
            self.link = wk.page(query)
            self.web = self.link.url
            self.lnk = Label(self.wiki_window, cursor='hand2', text=self.web, bg='white', fg='blue', font=('Times New Roman', 13))
            self.lnk.place(x=20, y=420)
            self.lnk.bind('<Enter>', self.onlinkenter)
            self.lnk.bind('<Leave>', self.onlinkleave)
            self.lnk.bind('<Button-1>', lambda eff: self.open_link(self.web))
        except:
            self.lnk = Label(self.wiki_window, text='Search a different article...', bg='white', fg='blue', font=('Times New Roman', 13))
            self.lnk.place(x=20, y=420)

        self.search_more = Button(self.wiki_window, text='Search more..', bg='light green', fg='dark blue', font=('Arial', 14, 'bold'), command=self.search_articles)
        self.search_more.place(x=340, y=440)

        self.root.mainloop()

    def onlinkenter(self, event):
        self.lnk.config(font=('Times New Roman', 13, 'underline'))
    
    def onlinkleave(self, event):
        self.lnk.config(font=('Times New Roman', 13))

    def open_link(self, link):
        wb.open(link)

    def search_articles(self):
        self.root.destroy()
        sw.search_wikipedia()

    def back_to_home(self):
        self.root.destroy()
        main.main_window()

if __name__ == '__main__':
    obj = search_wiki('Abstraction')