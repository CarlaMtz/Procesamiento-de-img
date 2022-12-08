from email.mime import image
import numpy as np
import cv2
from matplotlib import pyplot as plt
#print(cv2.__version__)

from tkinter import Label, messagebox, ttk
import tkinter as tk
from tkinter import*
class Application(ttk.Frame):
    
    def __init__(self, main_window):
        super().__init__(main_window)
        main_window.title("Procesamiento digital deimagenes")
        main_window.geometry("900x600")
        #main_window.configure(background='blue')

        self.combo = ttk.Combobox(
            self,
            state="readonly",
            values=["Operaor de identidad", 
            "OPerador inverso o negativo", 
            "Operador umbral", 
            "Operador intervalo umbral binario",
            "Operador intervalo umbral binario invertido",
            "Operador umbral de la escala grises",
            "Operador umbral escala grises invertido",
            "Operador extensión",
            "Operador reduccion nivel gris"],
            width=40
        )
        self.combo.bind("<<ComboboxSelected>>", self.selection_changed)
        self.combo.place(x=50, y=80)
        main_window.config(width=1200, height=600)
        self.place(width=1200, height=600)

        self.labelP2 = tk.Label(
                    text = "P2")
        self.labelP2.place(x=150,y=50)
       
        p2= tk.IntVar()
        
        self.entryP2 = tk.Entry(width=10, textvariable=p2)

        
        self.entryP2.place(x=170, y=50)

        self.imagenlbl=tk.PhotoImage(file='imagen_WB.png')
        self.lblimagen=tk.Label(image=self.imagenlbl)
        self.lblimagen.pack()
        self.lblimagen.place(x=30, y=130)


    def selection_changed(self, event):
        selection = self.combo.get()
        if selection == "Operaor de identidad":
            image = cv2.imread('imagen_WB.png')
            img1= np.asarray(image)
            print(img1)
            #img1= np.zeros((354,379), np.uint8)
            cv2.imwrite("img1.png",img1)
            self.imagenlbl1=tk.PhotoImage(file='img1.png')
            self.lblimagen1=tk.Label(image=self.imagenlbl1)
            self.lblimagen1.pack()
            self.lblimagen1.place(x=480, y=130)
        else:
            self.lblimagen1.pack_forget()

            if selection == "OPerador inverso o negativo":
                image = cv2.imread('imagen_WB.png')
                img2= 255-np.asarray(image)
                print(img2)
                #img2= np.zeros((354,379), np.uint8)
                cv2.imwrite("img2.png",img2)
                self.imagenlbl2=tk.PhotoImage(file='img2.png')
                self.lblimagen2=tk.Label(image=self.imagenlbl2)
                self.lblimagen2.pack()
                self.lblimagen2.place(x=480, y=130)
            else:
                self.lblimagen2.pack_forget()

            if selection == "Operador umbral":
                
                def transformar():
                 self.umbr1.set(self.p1.get())

                self.labelP1 = tk.Label(text = "P1")
                self.labelP1.place(x=50,y=50)
                self.p1= tk.IntVar()
                self.umbr1=tk.IntVar()
                self.entryP1 = tk.Entry(textvariable=self.p1)
                self.entryP1.pack()
                self.entryP1.place(x=70, y=50)
                self.boton=tk.Button(text="Transformar", command=transformar)
                self.boton.place(x=250, y=50)
                image = cv2.imread('imagen_WB.png',0)
                img3= np.asarray(image)
                
                print(image)
                ret,img3 = cv2.threshold(image,254,255,cv2.THRESH_BINARY)
                print(img3)
                cv2.imwrite("img3.png",img3)
                self.imagenlbl3=tk.PhotoImage(file='img3.png')
                self.lblimagen3=tk.Label(image=self.imagenlbl3)
                self.lblimagen3.pack()
                self.lblimagen3.place(x=480, y=130)
            else:
                self.lblimagen3.pack_forget()

                if selection == "Operador intervalo umbral binario":
                    image=cv2.imread('imagen_WB.png',0)
                    img4= np.asarray(image)
                    print(image)
                    ret,img4 = cv2.threshold(image,0,255,cv2.THRESH_BINARY)
                    print(img4)
                    cv2.imwrite("img4.png",img4)
                    self.imagenlbl4=tk.PhotoImage(file='img4.png')
                    self.lblimagen4=tk.Label(image=self.imagenlbl4)
                    self.lblimagen4.pack()
                    self.lblimagen4.place(x=480, y=130)

                else:
                    self.lblimagen4.pack_forget()
        
                    if selection == "Operador intervalo umbral binario invertido":
                        image=cv2.imread('imagen_WB.png',0)
                        img5= np.asarray(image)
                        print(image)
                        ret,img5 = cv2.threshold(image,254,255,cv2.THRESH_BINARY_INV)
                        print(img5)
                        
                        cv2.imwrite("img5.png",img5)
                        self.imagenlbl5=tk.PhotoImage(file='img5.png')
                        self.lblimagen5=tk.Label(image=self.imagenlbl5)
                        self.lblimagen5.pack()
                        self.lblimagen5.place(x=480, y=130)
                    else:
                        self.lblimagen5.pack_forget()

                        if selection == "Operador umbral de la escala grises":
                            img6= np.zeros((354,379), np.uint8)
                            cv2.imwrite("img6.png",img6)
                            self.imagenlbl6=tk.PhotoImage(file='img6.png')
                            self.lblimagen6=tk.Label(image=self.imagenlbl6)
                            self.lblimagen6.pack()
                            self.lblimagen6.place(x=480, y=130)
                        else:
                            self.lblimagen6.pack_forget()

                            if selection == "Operador umbral escala grises invertido":
                                img7= np.zeros((354,379), np.uint8)
                                cv2.imwrite("img7.png",img7)
                                self.imagenlbl7=tk.PhotoImage(file='img7.png')
                                self.lblimagen7=tk.Label(image=self.imagenlbl7)
                                self.lblimagen7.pack()
                                self.lblimagen7.place(x=480, y=130)
                            else:
                                self.lblimagen7.pack_forget()

                                if selection == "Operador extensión":
                                    img8= np.zeros((354,379), np.uint8)
                                    cv2.imwrite("img8.png",img8)
                                    self.imagenlbl8=tk.PhotoImage(file='img8.png')
                                    self.lblimagen8=tk.Label(image=self.imagenlbl8)
                                    self.lblimagen8.pack()
                                    self.lblimagen8.place(x=480, y=130)
                                else:
                                    self.lblimagen8.pack_forget()

                                    if selection == "Operador reduccion nivel gris":
                                        img9= np.zeros((354,379), np.uint8)
                                        cv2.imwrite("img9.png",img9)
                                        self.imagenlbl9=tk.PhotoImage(file='img9.png')
                                        self.lblimagen9=tk.Label(image=self.imagenlbl9)
                                        self.lblimagen9.pack()
                                        self.lblimagen9.place(x=480, y=130)
                                    else:
                                        self.lblimagen9.pack_forget()


main_window = tk.Tk()
app = Application(main_window)

app.mainloop()