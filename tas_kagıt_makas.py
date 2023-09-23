import random
from tkinter import *

import tkinter as tk
from tkinter import messagebox

root = Tk()
root.geometry("800x500")
root.title("OrangeHat")
root.resizable(width=False, height=False)

FONT = ("Arial", 10, "bold")

image_tas = PhotoImage(file="Taş.png")
image_kagit = PhotoImage(file="kagit.png")
image_makas = PhotoImage(file="makas.png")

image_list = [image_tas, image_makas, image_kagit]

frame_ust = Frame(root, width=800, height=100, bg='black')
frame_ust.place(x=0, y=0)

layer_logo = Label(frame_ust, width=20, height=10, bg='black')
layer_logo.place(x=35, y=10)

yazi = "Hamleni seç ve başla.."

layer_yazi = Label(frame_ust, width=70, height=5, bg='black', fg='white', text=yazi, font=FONT)
layer_yazi.place(x=200, y=10)

def tas_sec():
    layer_orta.configure(image=image_tas)
    layer_orta.image = image_tas

def kagit_sec():
    layer_orta.configure(image=image_kagit)
    layer_orta.image = image_kagit

def makas_sec():
    layer_orta.configure(image=image_makas)
    layer_orta.image = image_makas

def basla():

    def Kazandın():
        messagebox.showinfo("OrangeHat", "Kazandın!!")

    def Kaybettin():
        messagebox.showinfo("OrangeHat", "Kaybettin!!")

    def Berabere():
        messagebox.showinfo("OrangeHat", "Berabere, devam et!!")

    secim = random.choice(image_list)
    layer_sag.configure(image=secim)
    layer_sag.image = secim

    if secim == layer_orta.image:
        Berabere()
    elif (secim == image_tas and layer_orta.image == image_makas or
            secim == image_kagit and layer_orta.image == image_tas or
            secim == image_makas and layer_orta.image == image_kagit):
        Kaybettin()
    else:
        Kazandın()

# -------------------------------------------
frame_orta = Frame(root, width=800, height=300, bg='black')
frame_orta.place(x=0, y=100)

layer_sol = Label(frame_orta, width=200, height=300, bg='black')
layer_sol.place(x=0, y=0)

layer_orta = Label(frame_orta, width=300, height=300, bg='white')
layer_orta.place(x=200, y=0)

layer_sag = Label(frame_orta, width=300, height=300, bg='white')
layer_sag.place(x=500, y=0)

tas = Button(layer_sol, text='Taş', width=20, height=5, bg='#D2691E', font=FONT, command=tas_sec)
tas.place(x=20, y=5)

kagit = Button(layer_sol, text='Kağıt', width=20, height=5, bg='#D2691E', font=FONT, command=kagit_sec)
kagit.place(x=20, y=105)

makas = Button(layer_sol, text='Makas', width=20, height=5, bg='#D2691E', font=FONT, command=makas_sec)
makas.place(x=20, y=205)

# ----------------------------------
frame_alt = Frame(root, width=800, height=100, bg='black')
frame_alt.place(x=0, y=400)

baslamak = Button(frame_alt, width=15, height=2, text='Başla', font=FONT, bg='#D2691E', command=basla)
baslamak.place(x=430, y=5)

root.mainloop()
