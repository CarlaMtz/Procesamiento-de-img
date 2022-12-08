import cv2
from cv2 import *
from matplotlib import * 
import tkinter as tk
from tkinter import*
import numpy as np
import PIL 
from PIL import Image

ws = Tk()
ws.title('get text demo')
ws.geometry('600x600')


def transformar():
    umbr1=p1.get()
    umbr2=p2.get()
    img = Image.open('imagen_WB.png')
    img_gray = img.convert('L')

    img_pixels = list(img_gray.getdata())
    print(img_pixels)

    lst = []

    for i in img_pixels:
        # q =  255 para p <= p1, ó p >= p2
        if i <= umbr1 or i >= umbr2:
            lst.append(255)
        # q =  0 para p1 < p < p2
        elif umbr1<i<umbr2:
            lst.append(0)

    img_new = Image.new('L', img_gray.size)
    img_new.putdata(lst)
    img_new.save('img4.png')
    imagenlbl9=tk.PhotoImage(file='img4.png')
    lblimagen9=tk.Label(image=imagenlbl9)
    lblimagen9.pack()
    lblimagen9.place(x=50, y=130)

    
labelP1 = tk.Label(text = "P1")
labelP2 = tk.Label(text = "P2")
labelP1.place(x=50,y=50)
labelP2.place(x=150, y=50)
p1= tk.IntVar()
p2= tk.IntVar()
entryP1 = tk.Entry(width=10, textvariable=p1)
entryP2 = tk.Entry(width=10, textvariable=p2)
entryP1.place(x=70, y=50)
entryP2.place(x=170, y=50)
boton=tk.Button(text="Transformar", command=transformar)
boton.place(x=250, y=50)


ws.mainloop()
