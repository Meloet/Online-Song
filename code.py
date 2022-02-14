import pywhatkit
from tkinter import *
tk=Tk()
tk.title('onlinesong')
tk.geometry('500x300')
def listensong():
    song=song_text.get()
    pywhatkit.playonyt(song)
heading=Label(tk,text='Online Song',font=('bold',15)).place(x=195,y=50)
song_text=StringVar()
song_entrey=Entry(tk,textvariable=song_text)
song_entrey.place(x=185,y=90)
listen=Button(tk,text='Listen',width=12,command=listensong)
listen.place(x=210,y=120)
tk.mainloop()