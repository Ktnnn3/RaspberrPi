# Write your code here :-)
#age = 21
#input = int(input("Enter your number"))
#print("random number is", age-input)
import tkinter
from tkinter import*
from tkinter import messagebox
from winsound import *
import pygame

def hello():
    messagebox.showinfo("Information","Hello World")
    
def cancel():
    messagebox.askokcancel("Cancel","Cancel?")

def warning():
    messagebox.showwarning("Show warning","warning")
    
def error():
    messagebox.showerror("Error","Program error")
    
def question():
    messagebox.askquestion("Ask question","OK?")

def DisplayShow():
    global button33 , play
    button33 = Button(root,text="Play",command=play)
    button33.pack()

def play():
    pygame.init()
    pygame.mixer.music.load("path")
    pygame.mixer.music.play()
    while pygame.mixer.music.get_busy()==True:
        continue

    
root = Tk()
root.geometry("400x400")
root.title("Test")
#btn
btn = Button(root,text="OK",width=10,height=3)
btn.pack()
btn2 = Button(root,text="Cancel",width=10,height=3)
btn2.pack()
#label
label_1=Label(root,text="Python GUI",fg="green")
label_1.pack()
#ช่องเติมข้อความ
textbox = Entry(root,width=15)
textbox.pack()
#choose things
R1 = Radiobutton(root,text="Man",value = 1)
R1.pack()
R2 = Radiobutton(root,text="Woman",value=2)
R2.pack()
#message box //dont forget to import more
MB1 = Button(text="Say Hello",command = hello())
MB1.pack()
MB5 = Button(text="Cancel",command = cancel())
MB5.pack()
#Grid //images as Row and Column
#label_1.grid(row=0,column=0)
#label_2 = Label(root,text="Python2")
#label_2.grid(row=1,column=1)

#import image
logo = PhotoImage(file='/home/pi/Downloads/pic.png')
w1 = Label(root,image=logo).pack(side = "right")

#music //dont forget to import
#DisplayShow()




root.mainloop()
