# 1st Project from Allocated Project from CodeClause
from tkinter import *
import pyshorteners
import webbrowser

root = Tk()
root.title("URL Shortner API")
root.geometry("990x350")

head = Label(root, text="URL Shortner", font=('comic sans', 24))
head.grid(row=0, column=0, columnspan=3, pady=10)

inputurl_label = Label(root, text="Here Enter your long URL format:-", font=('Tahoma', 20))
inputurl_label.grid(row=1, column=0,pady=10)

entry = Entry(root,font=('Tahoma',16),width=42)
entry.grid(row=1, column=1)

inputurl_label = Label(root, text="Your URL in short format", font=('Tahoma', 20))
inputurl_label.grid(row=3, column=0,pady=10)

output_text = Text(root, height=1,font=('Tahoma',18), width=25)
output_text.grid(row=3, column=1)

def shorten_url():
    longurl = entry.get()
    type_tiny = pyshorteners.Shortener()
    shorturl = type_tiny.tinyurl.short(longurl)
    output_text.delete(1.0, END)
    output_text.insert(END, shorturl)

def open_url():
    shorturl = output_text.get(1.0, END).strip()
    webbrowser.open(shorturl)

submit = Button(root, text="Convert", font=('Tahoma', 16), command=shorten_url)
submit.grid(row=2, column=1, pady=20)

show = Button(root, text="Show", font=('Tahoma', 16), command=open_url)
show.grid(row=3, column=2)

root.mainloop()
