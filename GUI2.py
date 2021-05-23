
# importing only those functions
# which are needed
import tkinter
from tkinter import*
from tkinter import messagebox
from PIL import Image, ImageTk

# creating tkinter window
root = Tk()
root.attributes("-fullscreen", True)
root.bind("<F11>", lambda event: root.attributes("-fullscreen",
                                    not root.attributes("-fullscreen")))
root.bind("<Escape>", lambda event: root.attributes("-fullscreen", False))
root.configure(background='white')

#Variable
# choose = 1-Rice,2-Insect,3-Humidity
choose = 0;



def LabelText(textLabel,xl,yl):
    Label(root, text = textLabel, font =('Verdana', 30),bg="white",fg="black").place(x=xl,y=yl)

def img(path,mul):
    imgPic = Image.open(path)
    pix_x,pix_y = tuple([int(mul*x)for x in imgPic.size])
    photo = ImageTk.PhotoImage(imgPic.resize((pix_x,pix_y)))
    #button = Button(root,image = photo).place(x=xl,y=yl)
    return photo

def chooseOption(ch):
    choose = ch
    print('choose = ',choose)
    return choose
    
    


# Adding widgets to the root window

LabelText('Rice',120,75)
LabelText('Insect',345,75)
LabelText('Humidity',560,75)

# Creating a photoimage object to use image
fileRice = "/home/pi/Downloads/rice3.png"
fileInsect = "/home/pi/Downloads/Insect2.png"
fileHumidity = "/home/pi/Downloads/humidity3.png"


# here, image option is used to
# set image on button

photoRice = img(fileRice,1)
photoInsect = img(fileInsect,0.438)
photoHumidity = img(fileHumidity,0.438)


choose=Button(root,image = photoRice,bg="White",command=lambda:chooseOption(1)).place(x=50,y=150)
choose=Button(root,image = photoInsect,bg="White",command=lambda:chooseOption(2)).place(x=290,y=150)
choose=Button(root,image = photoHumidity,bg="White",command=lambda:chooseOption(3)).place(x=530,y=150)





root.mainloop()
