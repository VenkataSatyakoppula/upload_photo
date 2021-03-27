from tkinter import *
from PIL import Image,ImageTk
from tkinter import filedialog

base = Tk()
base.title('Image Location viewer')
title_label = Label(base,text="hello :) click upload button")
title_label.grid(row=0,column = 0,columnspan=3) 
def func():
    global img
    base.filename = filedialog.askopenfilename(initialdir="/",title="select",filetypes=(("png files","*.png"),("all files","*.*")))
    loc_print = Label(base,text=base.filename)
    loc_print.grid(row=4,column = 0,columnspan=3) 
    img = ImageTk.PhotoImage(Image.open(base.filename))
    image_print = Label(image=img)
    image_print.grid(row=6,column = 0,columnspan=3) 


butt = Button(base,text="upload image",command=func)
butt.grid(row=2,column = 0,columnspan=3) 

base.mainloop()