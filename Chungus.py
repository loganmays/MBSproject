import tkinter.messagebox
from tkinter import *


win=Tk() #creating the main window and storing the window object in 'win'
win.title('Welcome') #setting title of the window
win.geometry('200x100') #setting the size of the window

filestream = open('userinfo.txt', 'w')

def RegAccount():#function of the button
    
    user_id = str(ent.get())
    print(user_id, file= filestream) 
    msg = 'user id'
    tkinter.messagebox.showinfo('User: ',msg)
    #pass_id = str(ent.get())
    # age=int(ent.get())
    # if(age<18):
    #     msg='Sorry, you are not eligible to vote'
    # else:
    #     msg='You are eligible to vote!'
    # tkinter.messagebox.showinfo('Eligibility',msg)
    
text=Label(win, text='Enter your username')
ent = Entry(win) 
    
btn=Button(win,text="Click Me",command=RegAccount)
text.pack()
ent.pack()
btn.pack()
win.mainloop() #running the loop that works as a trigger

