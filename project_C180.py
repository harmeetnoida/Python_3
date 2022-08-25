from tkinter import *
from tkinter import ttk
from googletrans import Translator, LANGUAGES

root = Tk()
root.geometry('1080x400')
root.config(bg = '#F2CCC3')
root.title("Language Translator")

title_label = Label(root, text = "LANGUAGE TRANSLATOR", bg='#F2CCC3',font=("Sylfaen",18,"bold","italic"))
title_label.place(relx=0.5,rely=0.1, anchor=CENTER)

input_label = Label(root,text ="Enter Text", font = 'arial 13 bold', bg ='#F2CCC3')
input_label.place(relx=0.02,rely=0.2, anchor=W)

Input_text = Text(root,font = 'arial 10', height = 11, wrap = WORD, padx=5, pady=5, width = 60, bg="#FFFCF9", bd=0)
Input_text.place(relx=0.02,rely=0.5, anchor=W)

root.mainloop()  