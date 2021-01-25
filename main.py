# import install_requirements
from tkinter import *
from english_words import english_words_set
import PyDictionary as pd
from PIL import Image, ImageDraw
from PIL import ImageTk
import search_wiki as sw
import synonyms_antonyms_search as sas
import search_meanings as sm
import notification_settings as ns
import view_meaning as vm
import random as r
from threading import *
import shutil
import getpass
import os


def shuffle_words(root):
    root.destroy()
    main_window()

class main_window:
    def __init__(self):
        self.root = Tk()
        self.root.title('Glossary')
        self.root.iconbitmap('resources/dictionary.ico')
        self.root.resizable(0, 0)

        self.dictionary = pd.PyDictionary()

        self.menu = Frame(self.root, width=170, height=600, bg='white')
        self.menu.propagate(0)
        self.menu.pack(side=LEFT)

        self.main = Frame(self.root, width=500, height=600, bg='white')
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
            self.shuffle_btn = Button(self.menu, image=self.shuffle, bg='white', fg='#440D64', compound=LEFT, font=('Arial', 14, 'bold'), command=lambda: shuffle_words(self.root))
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

        self.heading = Label(self.main, text='Suggestions', bg='white', fg='red', font=('Courier', 17, 'bold underline'))
        self.heading.pack()

        self.t = Thread(target=self.suggestions)
        self.t.start()

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

    def suggestions(self):
        for i in range(4):
            self.words = list(english_words_set)
            self.rand_word = r.choice(self.words)
            try:
                self.meaning = self.dictionary.meaning(self.rand_word)
            except:
                self.meaning = ''
            
            self.lbl = LabelFrame(self.main, text=self.rand_word, width=400, height=110, bd=3, bg='white', fg='dark blue', font=('Georgia', 15, 'bold'))
            self.lbl.propagate(0)
            self.lbl.pack(pady=10)

            self.mean = Text(self.lbl, width=50, height=3, font=('Cambria', 13), wrap=WORD)
            self.mean.pack()

            if self.meaning == None:
                self.mean.insert(END, 'No Meanings found...')
                self.mean.config(fg='grey')
            else:
                self.vals = list(self.meaning.values())
                self.content = '⭐ ' + self.vals[0][0]
                try:
                    self.add = '\n⭐ ' + self.vals[0][1]
                    self.content+=self.add
                except:
                    pass

                self.mean.insert(END, self.content)
            self.mean.config(state=DISABLED)

            self.more = Button(self.lbl, text='more..', bg='white', fg='blue', relief=FLAT, activebackground='white', activeforeground='red', cursor='hand2', font=('Calibri', 13))
            self.more.pack(side=RIGHT)
            self.more['command'] = lambda q=self.rand_word: self.open_word_meaning(query=q)

    def open_word_meaning(self, query):
        self.root.destroy()
        vm.search_words(query=query)

    def run_in_bg(self):
        # This can be included but not included
        os.system(r'cmd /c "pyw notifier.py"')


if __name__ == '__main__':
    obj = main_window()
