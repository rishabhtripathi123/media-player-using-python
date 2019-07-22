import tkinter as tkr
import pygame
import os
from tkinter import filedialog
from tkinter import messagebox

pygame.init()
def playsong():
    try:
        paused
    except NameError:
        
        try:
            song = lb1.curselection()
            song=int(song[0])
            play_it = playlist[song]
            pygame.mixer.music.load(play_it)
            pygame.mixer.music.play()
            statusbar['text']='Playing'+' '+ os.path.basename(filepath)
        except:
            messagebox.showerror('File Not Found','Sorry,the file you were looking for could not be found')
    else:
        pygame.mixer.music.unpause()
    
def exitplayer():
    pygame.mixer.music.stop()
    statusbar['text']='Stopped'

def pausesong():
    global paused
    paused=True
    pygame.mixer.music.pause()
    statusbar['text']='Paused'

def browse():
    global filepath
    filepath=tkr.filedialog.askopenfilename()
    add_to_list(filepath)

def add_to_list(filename):
    filename=os.path.basename(filename)
    index=0
    lb1.insert(index,filename)
    playlist.insert(index,filepath)
    index +=1

def delete():
    song=lb1.curselection()
    song=int(song[0])
    lb1.delete(song)
    playlist.pop(song)

player = tkr.Tk()

menubar = tkr.Menu(player,tearoff=0)
player.config(menu=menubar)

submenu = tkr.Menu(menubar)
menubar.add_cascade(label='Open',menu=submenu)
submenu.add_command(label="Browse",command=browse)

player.title("Audio Player")
player.geometry("600x250+0+0")
player.config(bg="peach puff")

playlist=[]

b1=tkr.Button(player,text='Play',command=playsong ,font=('sans',10),bg="LightPink1")
b1.place(x=300,y=80)

b2=tkr.Button(player,text='Stop',command=exitplayer,font=('sans',10),bg="LightPink1")
b2.place(x=350,y=80)

b3=tkr.Button(player,text='Pause',command=pausesong, font=('sans',10),bg="LightPink1")
b3.place(x=400,y=80)


add = tkr.Button(player,command=browse, text='+ Add',bg='LightPink1')
add.place(x=90,y=190)

d = tkr.Button(player,command=delete, text = '- Delete',bg='LightPink1')
d.place(x=150,y=190)

statusbar = tkr.Label(player,text="Welcome",anchor='w',relief='sunken',bg='LightPink1',font=('sans',10))
statusbar.pack(side='bottom',fill='x')


lb1 = tkr.Listbox(player,bg='LightPink1')
lb1.place(x=90,y=20)

    
player.mainloop()
