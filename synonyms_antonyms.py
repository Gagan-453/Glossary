from tkinter import *
import synonyms_antonyms_search as sas
from PyDictionary import *
import webbrowser as wb
from PIL import Image, ImageDraw
from PIL import ImageTk
import main
import view_meaning as vm

def change_mode(mode_name, root, query):
    root.destroy()
    synonyms_and_antonyms(query=query, mode=mode_name)

class synonyms_and_antonyms:
    def __init__(self, query, mode):
        self.dictionary = PyDictionary()

        self.mode = mode
        self.query = query
        self.root = Tk()
        self.root.title('Glossary - ' + query)
        self.root.resizable(0, 0)
        self.root.iconbitmap('resources/dictionary.ico')

        self.wiki_window = Frame(self.root, width=530, height=500, bg='white')
        self.wiki_window.propagate(0)
        self.wiki_window.pack()

        self.topic = Label(self.wiki_window, text=query, bg='white', fg='dark blue', font=('Cambria', 16, 'bold italic'))
        self.topic.place(x=10, y=10)

        if mode == 'synonym':
            self.head = Label(self.wiki_window, text='Synonyms', bg='white', fg='red', font=('Courier', 13, 'bold underline'))
            self.head.place(x=220, y=30)
        else:
            self.head = Label(self.wiki_window, text='Antonyms', bg='white', fg='red', font=('Courier', 13, 'bold underline'))
            self.head.place(x=220, y=30)

        try:
            self.home = Image.open('resources/home.png') #pic
            self.home = self.home.resize((30, 30), Image.ANTIALIAS)
            self.home = ImageTk.PhotoImage(self.home)
            self.home_btn = Button(self.wiki_window, image=self.home, text=' Home', bg='white', fg='#440D64', relief=FLAT, compound=LEFT, font=('Arial', 14, 'bold'), command=self.back_to_home)
            self.home_btn.place(x=0, y=460)
        except:
            pass

        if mode == 'synonym':
            self.required_words = self.dictionary.synonym(query)
        else:
            self.required_words = self.dictionary.antonym(query)

        self.search_more = Button(self.wiki_window, text='Search more..', bg='light green', fg='dark blue', font=('Arial', 14, 'bold'), command=self.search_other_word)
        self.search_more.place(x=340, y=450)

        if mode == 'synonym':
            self.change_mode = Button(self.wiki_window, text='Antonyms..', bg='light green', fg='dark blue', font=('Arial', 14, 'bold'), command=lambda: change_mode('antonym', self.root, query))
            self.change_mode.place(x=180, y=450)
        else:
            self.change_mode = Button(self.wiki_window, text='Synonyms..', bg='light green', fg='dark blue', font=('Arial', 14, 'bold'), command=lambda: change_mode('synonym', self.root, query))
            self.change_mode.place(x=180, y=450)

        try:
            self.btn1 = Button(self.wiki_window, text=self.required_words[0][0:12], bg='light yellow', fg='purple', relief=GROOVE, width=10, activebackground='light yellow', font=('Bookman old style', 14, 'bold'), command=lambda: self.open_meaning(self.required_words[0]))
            self.btn1.place(x=20, y=100)
            self.btn1.bind('<Enter>', lambda eff, bg='light green': self.onenter(self.btn1, bg))
            self.btn1.bind('<Leave>', lambda eff, bg='light yellow': self.onleave(self.btn1, bg))

            self.btn2 = Button(self.wiki_window, text=self.required_words[1][0:12], bg='light yellow', fg='purple', relief=GROOVE, width=10, activebackground='light yellow', font=('Bookman old style', 14, 'bold'), command=lambda: self.open_meaning(self.required_words[1]))
            self.btn2.place(x=200, y=100)
            self.btn2.bind('<Enter>', lambda eff, bg='light green': self.onenter(self.btn2, bg))
            self.btn2.bind('<Leave>', lambda eff, bg='light yellow': self.onleave(self.btn2, bg))

            self.btn3 = Button(self.wiki_window, text=self.required_words[2][0:12], bg='light yellow', fg='purple', relief=GROOVE, width=10, activebackground='light yellow', font=('Bookman old style', 14, 'bold'), command=lambda: self.open_meaning(self.required_words[2]))
            self.btn3.place(x=380, y=100)
            self.btn3.bind('<Enter>', lambda eff, bg='light green': self.onenter(self.btn3, bg))
            self.btn3.bind('<Leave>', lambda eff, bg='light yellow': self.onleave(self.btn3, bg))

            self.btn4 = Button(self.wiki_window, text=self.required_words[3][0:12], bg='light yellow', fg='purple', relief=GROOVE, width=10, activebackground='light yellow', font=('Bookman old style', 14, 'bold'), command=lambda: self.open_meaning(self.required_words[3]))
            self.btn4.place(x=20, y=180)
            self.btn4.bind('<Enter>', lambda eff, bg='light green': self.onenter(self.btn4, bg))
            self.btn4.bind('<Leave>', lambda eff, bg='light yellow': self.onleave(self.btn4, bg))

            self.btn5 = Button(self.wiki_window, text=self.required_words[4][0:12], bg='light yellow', fg='purple', relief=GROOVE, width=10, activebackground='light yellow', font=('Bookman old style', 14, 'bold'), command=lambda: self.open_meaning(self.required_words[4]))
            self.btn5.place(x=200, y=180)
            self.btn5.bind('<Enter>', lambda eff, bg='light green': self.onenter(self.btn5, bg))
            self.btn5.bind('<Leave>', lambda eff, bg='light yellow': self.onleave(self.btn5, bg))

            self.btn6 = Button(self.wiki_window, text=self.required_words[5][0:12], bg='light yellow', fg='purple', relief=GROOVE, width=10, activebackground='light yellow', font=('Bookman old style', 14, 'bold'), command=lambda: self.open_meaning(self.required_words[5]))
            self.btn6.place(x=380, y=180)
            self.btn6.bind('<Enter>', lambda eff, bg='light green': self.onenter(self.btn6, bg))
            self.btn6.bind('<Leave>', lambda eff, bg='light yellow': self.onleave(self.btn6, bg))

            self.btn7 = Button(self.wiki_window, text=self.required_words[6][0:12], bg='light yellow', fg='purple', relief=GROOVE, width=10, activebackground='light yellow', font=('Bookman old style', 14, 'bold'), command=lambda: self.open_meaning(self.required_words[6]))
            self.btn7.place(x=20, y=260)
            self.btn7.bind('<Enter>', lambda eff, bg='light green': self.onenter(self.btn7, bg))
            self.btn7.bind('<Leave>', lambda eff, bg='light yellow': self.onleave(self.btn7, bg))

            self.btn8 = Button(self.wiki_window, text=self.required_words[7][0:12], bg='light yellow', fg='purple', relief=GROOVE, width=10, activebackground='light yellow', font=('Bookman old style', 14, 'bold'), command=lambda: self.open_meaning(self.required_words[7]))
            self.btn8.place(x=200, y=260)
            self.btn8.bind('<Enter>', lambda eff, bg='light green': self.onenter(self.btn8, bg))
            self.btn8.bind('<Leave>', lambda eff, bg='light yellow': self.onleave(self.btn8, bg))

            self.btn9 = Button(self.wiki_window, text=self.required_words[8][0:12], bg='light yellow', fg='purple', relief=GROOVE, width=10, activebackground='light yellow', font=('Bookman old style', 14, 'bold'), command=lambda: self.open_meaning(self.required_words[8]))
            self.btn9.place(x=380, y=260)
            self.btn9.bind('<Enter>', lambda eff, bg='light green': self.onenter(self.btn9, bg))
            self.btn9.bind('<Leave>', lambda eff, bg='light yellow': self.onleave(self.btn9, bg))

            self.btn10 = Button(self.wiki_window, text=self.required_words[9][0:12], bg='light yellow', fg='purple', relief=GROOVE, width=10, activebackground='light yellow', font=('Bookman old style', 14, 'bold'), command=lambda: self.open_meaning(self.required_words[9]))
            self.btn10.place(x=20, y=340)
            self.btn10.bind('<Enter>', lambda eff, bg='light green': self.onenter(self.btn10, bg))
            self.btn10.bind('<Leave>', lambda eff, bg='light yellow': self.onleave(self.btn10, bg))

            self.btn11 = Button(self.wiki_window, text=self.required_words[10][0:12], bg='light yellow', fg='purple', relief=GROOVE, width=10, activebackground='light yellow', font=('Bookman old style', 14, 'bold'), command=lambda: self.open_meaning(self.required_words[10]))
            self.btn11.place(x=200, y=340)
            self.btn11.bind('<Enter>', lambda eff, bg='light green': self.onenter(self.btn11, bg))
            self.btn11.bind('<Leave>', lambda eff, bg='light yellow': self.onleave(self.btn11, bg))

            self.btn12 = Button(self.wiki_window, text=self.required_words[11][0:12], bg='light yellow', fg='purple', relief=GROOVE, width=10, activebackground='light yellow', font=('Bookman old style', 14, 'bold'), command=lambda: self.open_meaning(self.required_words[11]))
            self.btn12.place(x=380, y=340)
            self.btn12.bind('<Enter>', lambda eff, bg='light green': self.onenter(self.btn12, bg))
            self.btn12.bind('<Leave>', lambda eff, bg='light yellow': self.onleave(self.btn12, bg))
        except:
            pass

        if self.required_words == None:
            if self.mode == 'synonym':
                self.show_msg = Label(self.wiki_window, text='No synonyms found...', bg='white', fg='grey', font=('Calibri', 13, 'italic'))
                self.show_msg.place(x=200, y=70)
            else:
                self.show_msg = Label(self.wiki_window, text='No antonyms found...', bg='white', fg='grey', font=('Calibri', 13, 'italic'))
                self.show_msg.place(x=200, y=70)

        self.root.mainloop()

    def search_other_word(self):
        self.root.destroy()
        if self.mode == 'synonym':
            sas.search_wikipedia()
        else:
            sas.search_wikipedia(mode='antonym')

    def back_to_home(self):
        self.root.destroy()
        main.main_window()
    
    def open_word_meaning(self):
        pass

    def onenter(self, button, bg='light grey'):
        button.config(bg=bg)

    def onleave(self, button, bg='#E0F8C8'):
        button.config(bg=bg)

    def open_meaning(self, qry):
        vm.search_words(query=qry)

if __name__ == '__main__':
    obj = synonyms_and_antonyms('Run', mode='synonym')