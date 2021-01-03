from tkinter import *
import webbrowser as wb
from PIL import Image, ImageDraw
from PIL import ImageTk
import main
import search_meanings as sm
from PyDictionary import *

def view_another_meaning(root, query):
    root.destroy()
    search_words(query)

class search_words:
    def __init__(self, query):
        self.dictionary = PyDictionary()

        self.query = query
        self.root = Tk()
        self.root.title('Glossary - ' + query)
        self.root.resizable(0, 0)
        self.root.iconbitmap('resources/dictionary.ico')

        self.wiki_window = Frame(self.root, width=500, height=550, bg='white')
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
            self.home_btn.place(x=0, y=510)
        except:
            pass

        self.show_less()
        self.search_more = Button(self.wiki_window, text='Search more..', bg='light green', fg='dark blue', font=('Garamond', 13, 'bold'), command=self.search_articles)
        self.search_more.place(x=380, y=510)

        try:
            self.lnk = Label(self.wiki_window, cursor='hand2', text='more...', bg='white', fg='blue', font=('Times New Roman', 13))
            self.lnk.place(x=420, y=380)
            self.lnk.bind('<Enter>', self.onlinkenter)
            self.lnk.bind('<Leave>', self.onlinkleave)
            self.lnk.bind('<Button-1>', lambda eff: self.open_link())
        except:
            pass

        self.similar_words = LabelFrame(self.wiki_window, text='Similar', width=490, height=80, bd=5, bg='white', font=('Verdana', 12))
        self.similar_words.place(x=10, y=400)

        self.synonyms = self.dictionary.synonym(self.query)

        self.c = 5

        if self.synonyms == None:
            self.lbl = Label(self.similar_words, text='No Words found...', bg='white', fg='grey', font=('Calibri', 13, 'italic'))
            self.lbl.place(x=10, y=10)
        else:
            try:
                for i in range(5):
                    self.btns = Button(self.similar_words, cursor='hand2', text=self.synonyms[i], bg='#E6EE71', width=8, fg='blue', relief=RAISED, activebackground='yellow', activeforeground='blue', font=('Cambria', 12, 'bold'))
                    self.btns.place(x=self.c, y=10)
                    self.btns['command'] = lambda syn=self.synonyms[i]: view_another_meaning(self.root, syn)
                    self.c+=98
            except:
                pass

        self.root.mainloop()

    def search_articles(self):
        self.root.destroy()
        sm.search_wikipedia()

    def back_to_home(self):
        self.root.destroy()
        main.main_window()

    def onlinkenter(self, event):
        self.lnk.config(font=('Times New Roman', 13, 'underline'))
    
    def onlinkleave(self, event):
        self.lnk.config(font=('Times New Roman', 13))

    def open_link(self):
        self.show_summary.config(state=NORMAL)
        self.show_summary.delete(0.0, END)

        try:
            self.info = self.dictionary.meaning(self.query)
            if self.info == None:
                self.show_summary.insert(END, 'No meanings found...')

            self.keys = list(self.info.keys())
            self.show_summary.insert(END, self.keys[0])

            self.v1 = self.info[self.keys[0]]
            self.show_summary.tag_add('highlight', 1.0, 1.19)
            self.show_summary.tag_config('highlight', foreground='blue', font=('Cambria', 14, 'italic'))

            for i in range(len(self.v1)):
                self.mean = '\n' + str(i+1) + '. ' + self.v1[i]
                self.show_summary.insert(END, self.mean)

            self.show_summary.insert(END, '\n \n')

            self.lines = int(self.show_summary.index('end-1c').split('.')[0])
            self.show_summary.insert(END, self.keys[1])
            self.v2 = self.info[self.keys[1]]
            self.show_summary.tag_add('highlight', float(self.lines), self.lines+0.19)
            self.show_summary.tag_config('highlight', foreground='blue', font=('Cambria', 14, 'italic'))

            for i in range(len(self.v2)):
                self.mean = '\n' + str(i+1) + '. ' + self.v2[i]
                self.show_summary.insert(END, self.mean)
            self.show_summary.insert(END, '\n \n')

            self.lines = int(self.show_summary.index('end-1c').split('.')[0])
            self.show_summary.insert(END, self.keys[2])
            self.v3 = self.info[self.keys[2]]
            self.show_summary.tag_add('highlight', float(self.lines), self.lines+0.19)
            self.show_summary.tag_config('highlight', foreground='blue', font=('Cambria', 14, 'italic'))

            for i in range(len(self.v3)):
                self.mean = '\n' + str(i+1) + '. ' + self.v3[i]
                self.show_summary.insert(END, self.mean)
            self.show_summary.insert(END, '\n \n')
            

            self.lines = int(self.show_summary.index('end-1c').split('.')[0])
            self.show_summary.insert(END, self.keys[3])
            self.v4 = self.info[self.keys[3]]
            self.show_summary.tag_add('highlight', float(self.lines), self.lines+0.19)
            self.show_summary.tag_config('highlight', foreground='blue', font=('Cambria', 14, 'italic'))

            for i in range(len(self.v4)):
                self.mean = '\n' + str(i+1) + '. ' + self.v4[i]
                self.show_summary.insert(END, self.mean)
            self.show_summary.insert(END, '\n \n')
            
            
        except:
            pass
        
        self.lnk.config(text='less...' )
        self.lnk.bind('<Button-1>', lambda eff: self.show_less())

        self.show_summary.config(state=DISABLED)

    def show_less(self):
        self.show_summary.config(state=NORMAL)
        self.show_summary.delete(0.0, END)

        try:
            self.info = self.dictionary.meaning(self.query)
            if self.info == None:
                self.show_summary.insert(END, 'No meanings found...')

            self.keys = list(self.info.keys())
            self.show_summary.insert(END, self.keys[0])

            self.v1 = self.info[self.keys[0]]
            self.show_summary.tag_add('highlight', 1.0, 1.19)
            self.show_summary.tag_config('highlight', foreground='blue', font=('Cambria', 14, 'italic'))

            for i in range(3):
                self.mean = '\n' + str(i+1) + '. ' + self.v1[i]
                self.show_summary.insert(END, self.mean)

            self.show_summary.insert(END, '\n \n')

            self.lines = int(self.show_summary.index('end-1c').split('.')[0])
            self.show_summary.insert(END, self.keys[1])
            self.v2 = self.info[self.keys[1]]
            self.show_summary.tag_add('highlight', float(self.lines), self.lines+0.19)
            self.show_summary.tag_config('highlight', foreground='blue', font=('Cambria', 14, 'italic'))

            for i in range(3):
                self.mean = '\n' + str(i+1) + '. ' + self.v2[i]
                self.show_summary.insert(END, self.mean)
            self.show_summary.insert(END, '\n \n')
            

            self.lines = int(self.show_summary.index('end-1c').split('.')[0])
            self.show_summary.insert(END, self.keys[2])
            self.v3 = self.info[self.keys[2]]
            self.show_summary.tag_add('highlight', float(self.lines), self.lines+0.19)
            self.show_summary.tag_config('highlight', foreground='blue', font=('Cambria', 14, 'italic'))

            for i in range(3):
                self.mean = '\n' + str(i+1) + '. ' + self.v3[i]
                self.show_summary.insert(END, self.mean)
            self.show_summary.insert(END, '\n \n')

            self.lines = int(self.show_summary.index('end-1c').split('.')[0])
            self.show_summary.insert(END, self.keys[3])
            self.v4 = self.info[self.keys[3]]
            self.show_summary.tag_add('highlight', float(self.lines), self.lines+0.19)
            self.show_summary.tag_config('highlight', foreground='blue', font=('Cambria', 14, 'italic'))

            for i in range(3):
                self.mean = '\n' + str(i+1) + '. ' + self.v4[i]
                self.show_summary.insert(END, self.mean)
            self.show_summary.insert(END, '\n \n')

        except:
            pass

        try:
            self.lnk.config(text='more...' )
            self.lnk.bind('<Button-1>', lambda eff: self.open_link())
        except:
            pass

        self.show_summary.config(state=DISABLED)

if __name__ == '__main__':
    obj = search_words('surface')