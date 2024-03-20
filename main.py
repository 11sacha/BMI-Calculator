#Importing necesary libraries and modules
from tkinter import *
import tkinter as tk
from tkinter import ttk, Button
from PIL import Image,ImageTk

# Basic Settings
root = Tk()
root.title("BMI Calculator")
root.geometry("460x580+300+200")
root.resizable(False,False)
root.configure(bg="#f0f1f5")

#BMI calculations
def BMI():
    h = float(Height.get())
    w = float(Weight.get())

    if h != 0:
        m = h / 100
        bmi = round(float(w / (m ** 2)), 1)
        return bmi
    else:
        return "Error: Height cannot be zero for BMI calculation."

    # m = h/100
    # bmi = round(float(w/m**2),1)
    # label1.config(text=bmi)


def update_bmi():
    bmi = BMI()
    print('works')
    label1.config(text=f"{bmi}")
    if bmi <= 18.5:
        label2.config(text="Underweight!")
        label3.config(text="You have lower weight than average bodytype!")
    elif bmi > 18.5 and bmi <= 25:
        label2.config(text="Normal weight!")
        label3.config(text="It indicates that you are healthy!")
    elif bmi > 25 and bmi <= 30:
        label2.config(text="Overweight!")
        label3.config(text="It indicates that you are slightly overweight!")
    else:
        label2.config(text="Obes!")
        label3.config(text="Health may be at risk, if you do not loose weight!")


## Aesthetic Design ##
#Icon
image_icon = PhotoImage(file="resources/icon.png")
root.iconphoto(False, image_icon)

#Top
top = PhotoImage(file="resources/top.png")
top_image = Label(root, image=top, background="#f0f1f5")
top_image.place(x=-10, y=-10)

#Bottom Box
Label(root, width=72, height=18, bg="lightblue").pack(side=BOTTOM)

#Two boxes
box = PhotoImage(file="resources/box_2.png")
Label(root, image=box).place(x=20, y=80)
Label(root, image=box).place(x=240, y=80)

label4 = Label(root, text="Height (cm):", font="arial 15 bold", bg="#fff", fg="#000").place(x=80, y=100)
label5 = Label(root, text="Weight (kg):", font="arial 15 bold", bg="#fff", fg="#000").place(x=300, y=100)

#Scale
scale = PhotoImage(file="resources/scale.png")
Label(root, image=scale, bg="lightblue").place(x=20, y=315)

## Slider 1 ##
current_value = tk.DoubleVar()

def get_current_value():
    return '{: .2f}'.format(current_value.get())

def slider_changed(event):
    Height.set(get_current_value())

    size = int(float(get_current_value()))
    img = (Image.open("resources/man.png"))
    resized_image = img.resize((50,10+size))
    photo2 = ImageTk.PhotoImage(resized_image)
    man_image.config(image=photo2)
    man_image.place(x=70, y=550-size)
    man_image.image = photo2

slide = ttk.Style()
slide.configure("TScale", background="white")   
slider = ttk.Scale(root, from_=0, to=220, orient='horizontal', style="TScale", command=slider_changed, variable=current_value)
slider.place(x=70, y=250)

## Slider 2 ##
current_value2 = tk.DoubleVar()
def get_current_value2():
    return '{: .2f}'.format(current_value2.get())

def slider_changed2(event):
    Weight.set(get_current_value2())

slide2 = ttk.Style()
slide2.configure("TScale", background="white")   
slider2 = ttk.Scale(root, from_=0, to=200, orient='horizontal', style="TScale", command=slider_changed2, variable=current_value2)
slider2.place(x=290, y=250)

#Boxes Input
Height = StringVar()
Weight = StringVar()

height = Entry(root, textvariable=Height, width=5, font='arial 50', bg='#fff', fg='#000', bd=0, justify=CENTER)
height.place(x=45, y=150)
Height.set(get_current_value())

weight = Entry(root, textvariable=Weight, width=5, font='arial 50', bg='#fff', fg='#000', bd=0, justify=CENTER)
weight.place(x=265, y=150)
Weight.set(get_current_value2())

#Man image
man_image = Label(root, bg="lightblue")
man_image.place(x=70, y=560)

Button(root, text="View Report", width=15, height=2, font="arial 10 bold", bg='#1f6e68', fg='black',command=update_bmi).place(x=280, y=340)

label1 = Label(root, font="arial 60 bold", bg="lightblue", fg="#000")
label1.place(x=125, y=305)

label2 = Label(root, font="arial 20 bold", bg="lightblue", fg="#3b3a3a")
label2.place(x=280, y=430)

label3 = Label(root, font="arial 10 bold", bg="lightblue", fg="#3b3a3a")
label3.place(x=200, y=500)

root.mainloop()

