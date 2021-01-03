from tkinter import *
from english_words import english_words_set
import PyDictionary as pd
from PIL import Image, ImageDraw
from PIL import ImageTk
import search_wiki as sw
import synonyms_antonyms_search as sas
import search_meanings as sm
import notification_settings as ns

class main_window:
    def __init__(self):
        self.root = Tk()
        self.root.title('Glossary')
        self.root.iconbitmap('resources/dictionary.ico')
        self.root.resizable(0, 0)

        self.menu = Frame(self.root, width=170, height=600, bg='white')
        self.menu.propagate(0)
        self.menu.pack(side=LEFT)

        self.main = Frame(self.root, width=600, height=600, bg='white')
        self.main.propagate(0)
        self.main.pack(side=LEFT)

        try:
            self.search = Image.open('resources/search.png') #pic
            self.search = self.search.resize((30, 30), Image.ANTIALIAS)
            self.search = ImageTk.PhotoImage(self.search)
            self.search_btn = Button(self.menu, image=self.search, bg='white', fg='#440D64', compound=LEFT, font=('Arial', 14, 'bold'), command=self.search_meanings)
            self.search_btn.place(x=10, y=50)
            self.search_btn.bind('<Enter>', lambda eff: self.extend(widget=self.search_btn, txt='  Search'))
            self.search_btn.bind('<Leave>', lambda eff: self.extend_back(widget=self.search_btn))
        except:
            pass

        self.synonym = Button(self.menu, text='S', width=2, bg='white', fg='#440D64', font=('Arial', 14, 'bold'), command=self.search_synonyms)
        self.synonym.place(x=10, y=100)
        self.synonym.bind('<Enter>', lambda eff: self.extend(widget=self.synonym, txt='  Synonyms', width=10))
        self.synonym.bind('<Leave>', lambda eff: self.extend_back(widget=self.synonym, width=2, txt='S'))

        self.antonym = Button(self.menu, text='A', width=2, bg='white', fg='#440D64', font=('Arial', 14, 'bold'), command=self.search_antonyms)
        self.antonym.place(x=10, y=150)
        self.antonym.bind('<Enter>', lambda eff: self.extend(widget=self.antonym, txt='  Antonyms', width=10))
        self.antonym.bind('<Leave>', lambda eff: self.extend_back(widget=self.antonym, width=2, txt='A'))

        try:
            self.wiki = Image.open('resources/wikipedia.png') #pic
            self.wiki = self.wiki.resize((30, 30), Image.ANTIALIAS)
            self.wiki = ImageTk.PhotoImage(self.wiki)
            self.wiki_btn = Button(self.menu, image=self.wiki, bg='white', fg='#440D64', compound=LEFT, font=('Arial', 14, 'bold'), command=self.go_to_wiki_search)
            self.wiki_btn.place(x=10, y=200)
            self.wiki_btn.bind('<Enter>', lambda eff: self.extend(widget=self.wiki_btn, txt='  Wikipedia'))
            self.wiki_btn.bind('<Leave>', lambda eff: self.extend_back(widget=self.wiki_btn))
        except:
            pass

        try:
            self.shuffle = Image.open('resources/shuffle.png') #pic
            self.shuffle = self.shuffle.resize((30, 30), Image.ANTIALIAS)
            self.shuffle = ImageTk.PhotoImage(self.shuffle)
            self.shuffle_btn = Button(self.menu, image=self.shuffle, bg='white', fg='#440D64', compound=LEFT, font=('Arial', 14, 'bold'))
            self.shuffle_btn.place(x=10, y=260)
            self.shuffle_btn.bind('<Enter>', lambda eff: self.extend(widget=self.shuffle_btn, txt='  Shuffle'))
            self.shuffle_btn.bind('<Leave>', lambda eff: self.extend_back(widget=self.shuffle_btn))
        except:
            pass

        try:
            self.notification = Image.open('resources/notification.png') #pic
            self.notification = self.notification.resize((30, 30), Image.ANTIALIAS)
            self.notification = ImageTk.PhotoImage(self.notification)
            self.notification_btn = Button(self.menu, image=self.notification, bg='white', fg='#440D64', compound=LEFT, font=('Arial', 14, 'bold'), command=self.open_notifications_settings)
            self.notification_btn.place(x=10, y=310)
            self.notification_btn.bind('<Enter>', lambda eff: self.extend(widget=self.notification_btn, txt=' Notifications'))
            self.notification_btn.bind('<Leave>', lambda eff: self.extend_back(widget=self.notification_btn))
        except:
            pass

        try:
            self.exit = Image.open('resources/exit.png') #pic
            self.exit = self.exit.resize((50, 30), Image.ANTIALIAS)
            self.exit = ImageTk.PhotoImage(self.exit)
            self.exit_btn = Button(self.menu, image=self.exit, bg='white', fg='#440D64', command=self.root.destroy)
            self.exit_btn.place(x=0, y=560)
        except:
            pass

        self.root.mainloop()

    def extend(self, widget, txt, width=None):
        if width==None:
            widget.config(text=txt)
        else:
            widget.config(text=txt, width=width)

    def extend_back(self, widget, width=None, txt=''):
        if width==None:
            widget.config(text=txt)
        else:
            widget.config(width=width, text=txt)

    def go_to_wiki_search(self):
        self.root.destroy()
        sw.search_wikipedia()

    def search_synonyms(self):
        self.root.destroy()
        sas.search_wikipedia()
    
    def search_antonyms(self):
        self.root.destroy()
        sas.search_wikipedia(mode='antonym')

    def search_meanings(self):
        self.root.destroy()
        sm.search_wikipedia()

    def open_notifications_settings(self):
        self.root.destroy()
        ns.notifications()


if __name__ == '__main__':
    obj = main_window()
