import random
import requests
from tkinter import *
import pprint

def get_author():

    clear_poem()

    res=requests.get('http://poetrydb.org/author')
    data=res.json()
    
    authors=data['authors']
    rand_author=authors[random.randint(0, 128)]
    

    
    get_poem(rand_author)
    
def get_poem(rand_author):
    global textlabel, authorlabel

    poemnum=0
    
    res=requests.get('http://poetrydb.org/author/{}'.format(rand_author))
    data=res.json()
    
    poems=data[0:]
    
    for word in poems:
        poemnum+=1
        
    rand_poemnum=random.randint(0, poemnum-1)
    
    poem_lines=poems[rand_poemnum]['lines']
    poem_title=poems[rand_poemnum]['title']

    
    final=[]
    for word in poem_lines:
        final.append(word)
        final.append('\n')
        
    authorlabel=Label(midf, text='{} written by {}'.format(poem_title, rand_author))
    authorlabel.grid(row=0, column=0)
    
    textlabel=Label(midf, text=' '.join(final))
    textlabel.grid(row=1, column=0)

def clear_poem():

    try:
        authorlabel.grid_forget()
        textlabel.grid_forget()
    except:
        print('no poems')

root=Tk()

topf=Frame(root)
topf.pack(fill=X)
sidebar=Frame(root)
sidebar.pack(side=RIGHT, fill=Y)

midf=Frame(root)
midf.pack()

title=Label(topf, text='POEM GENERATOR', font=('Consolas',30), fg='purple')
title.pack(fill=X)

gen_button=Button(sidebar, text='Generate Poem', command=get_author)
gen_button.pack()

mainloop()
