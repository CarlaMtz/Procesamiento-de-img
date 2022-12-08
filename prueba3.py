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
    umbr=p1.get()
    #umbral,img3=cv2.threshold(image,{umbr},255,cv2.THRESH_BINARY)
    #img3=np.uint8((image_gray <= umbr)*255)
    #cv2.imwrite("img3.png",img3)
    #imagenlbl3=tk.PhotoImage(file='img3.png')
    #lblimagen3=tk.Label(image=imagenlbl3)
    #lblimagen3.pack()
    #lblimagen3.place(x=50, y=130)
    img = Image.open('imagen_WB.png')
    img_gray = img.convert('L')
    #img_gray.show()

    img_pixels = list(img_gray.getdata())
    print(img_pixels)

    lst = []

    for i in img_pixels:
        # q = 0 para p <= p
        if i < umbr:
            lst.append(0)
        # q = 255 para p > p
        else:
            lst.append(255)

    img_new = Image.new('L', img_gray.size)
    img_new.putdata(lst)
    img_new.save('img4.png')
    imagenlbl9=tk.PhotoImage(file='img4.png')
    lblimagen9=tk.Label(image=imagenlbl9)
    lblimagen9.pack()
    lblimagen9.place(x=50, y=130)

    
labelP1 = tk.Label(text = "P1")
labelP1.place(x=50,y=50)
p1= tk.IntVar()
#umbral=transformar()
entryP1 = tk.Entry(textvariable=p1)
entryP1.place(x=70, y=50)
boton=tk.Button(text="Transformar", command=transformar)
boton.place(x=250, y=50)


ws.mainloop()
