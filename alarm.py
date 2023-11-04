# 2nd project from Allocated Project from CodeClause
from tkinter import *
import datetime
import time
from pygame import mixer
import threading
from tkinter import messagebox

root =Tk()
root.title(" Alarm Clock ")
root.geometry("650x350")


head =Label(root,text="Ayan's Alarm Clock",font=('comic sans',24),justify="center")
head.grid(row=0,columnspan=6,pady=10)

clockimg=PhotoImage(file="image.png")

img = Label(root,image=clockimg)
img.grid(rowspan=10,row=2,column=2,pady=12)

inputtime=Label(root,text="Set Alarm Time",font=('Tahoma',20))
inputtime.grid(row=2,column=3)

alarmtime=Entry(root,font=('Tahoma',20),width=10)
alarmtime.grid(row=2,column=4)

msg=Label(root,text="Customize Pop-Up Message",font=('Tahoma',18))
msg.grid(row=5,column=3,columnspan=3)

msginput=Entry(root,font=('Tahoma',22))
msginput.grid(row=7,column=3,columnspan=3)

def th():
	t1 = threading.Thread(target=alarmfun, args=())
	t1.start()

submit=Button(root,text=" Set Alarm ",font=('Tahoma',16),command=th)
submit.grid(row=10,column=4,columnspan=1)

mixer.init()

def alarmfun():
    a = alarmtime.get()
    CURRENTTime = time.strftime("%H:%M")
    while a != CURRENTTime:
        CURRENTTime = time.strftime("%H:%M")

    if(a == CURRENTTime):
        mixer.music.load('ayan.mp3')
        mixer.music.play()
        msg = messagebox.showinfo('It is the time',f'{msginput.get()}')
        if(msg == 'ok'):
            mixer.music.stop()

root.mainloop()
