import os
from english_words import *
import random as r
from PyDictionary import *
from plyer import notification 
import time 

dictionary = PyDictionary()
file = open('resources/time.txt', 'r')
content = (file.read()).strip()

if content == 'Never':
    t = 0
elif content == '5 minutes':
    t = 60*5
elif content == '10 minutes':
    t = 60*10
elif content == '30 minutes':
    t = 60*30
elif content == '1 hour':
    t = 60*60
elif content == '2 hours':
    t = 60*120
elif content == '1 day':
    t = 60*60*24

while True:
    if t == 0:
        break
    
    words = list(english_words_set)
    rand_word = r.choice(words)

    try:
        meaning = dictionary.meaning(rand_word)
        mean = list(meaning.keys())
        first = mean[0]
        word_meaning = meaning[first][0]
        title = rand_word
        msg = word_meaning
        icon = 'resources/dictionary.ico'

        notification.notify(title, message=msg, timeout=10)

        time.sleep(t)
    except:
        pass

