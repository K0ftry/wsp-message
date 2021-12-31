import pyautogui, webbrowser
from time import sleep
import os
from tkinter import *
 
def enviar():
    webbrowser.open("https://web.whatsapp.com/send?phone="+numero.get())
    sleep(15)
    pyautogui.click(975,694)
    for i in range(0,int(valor.get())): 
            pyautogui.typewrite(texto.get())
            pyautogui.press("enter")

ventana= Tk()
ventana.geometry("500x300")
ventana.title("WspSpm")
ventana.resizable(0,0)
numero = StringVar()
texto = StringVar()
valor = StringVar()
numeroLabel = Label(ventana,text="Ingresa el número de destino: ").place(x=10,y=10)
numeroText = Entry(ventana, width=30, textvariable=numero).place(x=200,y=10)
textoLabel = Label(ventana,text="Ingresa texto: ").place(x=10,y=50)
textoText = Entry(ventana, width=30, textvariable=texto).place(x=200,y=50)
valorLabel = Label(ventana, text="Selecciona cantidad a enviar").place(x=10,y=100)
spin = Spinbox(ventana,from_=1, to=50, textvariable=valor).place(x=200,y=100)
boton = Button(ventana, text="Enviar", command=enviar).place(x=150,y=200)

ventana.mainloop()

