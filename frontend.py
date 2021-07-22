from os import error
from tkinter import *
from tkinter import ttk
from typing import List
from colors import *
import backend 

"""
 -------------------------------------------------------
                  READING LIST
 TITLE:                           AUTHOR:
 YEAR:                            STATUS: Read/Unread

                              ^
                              |     VIEW ALL
                              |     SEARCH ENTRY
                              |     ADD ENTRY
                              |     DELETE ENTRY
                              |     UPDATE ENTRY
                              |     CLOSE
 
 ---------------------------------------------------------                                  
"""
def get_selected_row(event):
    try:
        global selected_tuple
        index=list1.curselection()[0]
        selected_tuple=list1.get(index)
        e1.delete(0,END)
        e1.insert(END,selected_tuple[1])
        e2.delete(0,END)
        e2.insert(END,selected_tuple[2])
        e3.delete(0,END)
        e3.insert(END,selected_tuple[3])
        e4.delete(0,END)
        e4.insert(END,selected_tuple[4])
    except IndexError:
        print("No entries yet")

def view_command():
    list1.delete(0, END)
    for row in backend.view():
        print(row)
        list1.insert(END, row)

def search_command():
    list1.delete(0, END)
    for row in backend.search(title_text.get(), author_text.get(), year_text.get(), status_text.get()):
        list1.insert(END, row)

def add_command():
    backend.insert(title_text.get(), author_text.get(), year_text.get(), status_text.get())
    list1.delete(0, END)
    list1.insert(END,(title_text.get(), author_text.get(), year_text.get(), status_text.get()))

def delete_command():
    backend.delete(selected_tuple[0])

def update_command():
    backend.update(selected_tuple[0], title_text.get(), author_text.get(), year_text.get(), status_text.get())

window=Tk()
window.configure(bg=GRAY)
window.title("Reading Bucket-List Inventory",)
l1=Label(window,bg=BLUE,fg=WHITE, font=("Arial bold",15),text='  Reading Bucket List  ',width=20)
l1.grid(row=0,column=1)

l2=Label(window, bg=LIGHT_BLUE,font='Arial',text='TITLE :',width=12,border=0)
l2.grid(row=1,column=0)
l3=Label(window, bg=LIGHT_BLUE, font='Arial',text='AUTHOR :',width=12,border=0)
l3.grid(row=1,column=2)
l4=Label(window, bg=LIGHT_BLUE, font='Arial',text='YEAR :',width=12,border=0)
l4.grid(row=2,column=0)
l5=Label(window, bg=LIGHT_BLUE, font='Arial',text='STATUS :',width=12,border=0)
l5.grid(row=2,column=2)

status_list=['Read','Unread']
title_text=StringVar()
year_text=StringVar()
author_text=StringVar()
status_text=StringVar()
e1=Entry(window,textvariable=title_text,width=25)
e1.grid(row=1,column=1)
e2=Entry(window,textvariable=author_text,width=25)
e2.grid(row=1,column=3)
e3=Entry(window,textvariable=year_text,width=25)
e3.grid(row=2,column=1)
e4=ttk.Combobox(window,textvariable=status_text,values=status_list,width=22)
e4.grid(row=2,column=3)

list1=Listbox(window,height=20,width=40)
list1.grid(row=4,column=1,rowspan=10,columnspan=1)
sb=Scrollbar(window)
sb.grid(row=4,column=2)
list1.configure(yscrollcommand=sb.set)
sb.configure(command=list1.yview)
list1.bind('<<ListboxSelect>>', get_selected_row)

b1=Button(window,bg=LIGHT_BLUE, text="View All", font='Arial',width=12,command=view_command)
b1.grid(row=4,column=3)

b2=Button(window,bg=LIGHT_BLUE, text="Search", font='Arial',width=12,command=search_command)
b2.grid(row=5,column=3)

b3=Button(window,bg=LIGHT_BLUE, text="Add", font='Arial',width=12,command=add_command)
b3.grid(row=6,column=3)

b4=Button(window,bg=LIGHT_BLUE, text="Update", font='Arial',width=12,command=update_command)
b4.grid(row=7,column=3)

b5=Button(window,bg=LIGHT_BLUE, text="Delete", font='Arial',width=12,command=delete_command)
b5.grid(row=8,column=3)

b6=Button(window,bg=LIGHT_BLUE, text="Close", font='Arial',width=12,command=window.destroy)
b6.grid(row=9,column=3)

window.mainloop()