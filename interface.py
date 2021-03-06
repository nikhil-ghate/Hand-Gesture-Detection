from tkinter import *  
from PIL import ImageTk,Image 
from tkinter import ttk 
import os
import sys


def collect():
    os.system('python collect-data.py')
    
def train():
    os.system('python train.py')

def predict():
    os.system('python predict.py')
root = Tk()
#root.configure(background='green')

root.minsize(700, 600)
root.title('Hand Gesture Detection')
root.iconbitmap('images/hand.ico')

canvas =Canvas(root,width=700,height=200)
img = ImageTk.PhotoImage(file=r"images\bg.jpg")
canvas.create_image(0,0,anchor=NW,image=img)
label_msg = canvas.create_text((350, 100), text="Hand Gesture Detection System", font="oemfixed 25 bold", fill="white")
canvas.pack()


im1 = PhotoImage(file=r"images\collect.png")
im2 = PhotoImage(file=r"images\train.png")
im3 = PhotoImage(file=r"images\test.png")
tim1 = im1.subsample(3,3)
tim2 = im2.subsample(3,3)
tim3 = im3.subsample(3,3)

btn = Button(root,text="Collect Data",bg='goldenrod1',font=10,width=20,height=2,activebackground='green',command=collect,border=0,)
btn.place(x=252,y=230)
label = ttk.Label(root, image = tim1)
label.place(x=175,y=205)

btn1 = Button(root,text="Train Data",bg='goldenrod1',font=10,width=20,height=2,activebackground='green',command=train,border=0,)
btn1.place(x=252,y=335)
label1 = ttk.Label(root, image = tim2)
label1.place(x=175,y=315)

btn2 = Button(root,text="Detect Gesture",bg='goldenrod1',font=10,width=20,height=2,activebackground='green',command=predict,border=0,)
btn2.place(x=252,y=440)
label2 = ttk.Label(root, image = tim3)
label2.place(x=175,y=421)

root.mainloop()  


