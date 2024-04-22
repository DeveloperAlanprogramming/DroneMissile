

from tkinter import ttk
import tkinter as tk
from funciones import *
import cv2


class Laser(metodos):
    
    
    def __init__(self):
        
        super().__init__()
        
        self.start=0
        self.stop=0
        self.button=0
        self.button1=0
        self.button2=0
        self.button3=0
        self.button4=0
        self.button5=0
        self.button6=0
        self.button7=0
        self.label1=0
        self.label2=0
        self.label3=0
        self.label4=0
        self.label5=0
        
        self.image=0
        self.cap = cv2.VideoCapture(1)
        self.root =tk.Tk()
        self.root.title("Laser Applications")
        self.root.geometry('2000x2000')
        
        
    def compontentes(self):
        
        self.caja_botones()
        self.Mensajes()
        self.root.mainloop()
        
    def caja_botones(self):
        
        
        
        self.button1=tk.Button(self.root,text="GENERATIVE AI ON",command=self.systemstart, background="red",width=20,height=2,font=("arial", 20,"bold"))
        self.button1.place(x=30,y=700)
        
        self.button2=tk.Button(self.root,text="GENERATIVE AI OFF",command=self.systemoff,background="blue",width=20,height=2,font=("arial", 20,"bold"))
        self.button2.place(x=30,y=800)
        
        self.button5=tk.Button(self.root,text="MOTOR ON",command=self.motorstart, background="red",width=10,height=2,font=("arial", 20,"bold"))
        self.button5.place(x=400,y=700)
        
        self.button6=tk.Button(self.root,text="MOTOR OFF",command=self.motoroff,background="blue",width=10,height=2,font=("arial", 20,"bold"))
        self.button6.place(x=400,y=800)
        
        self.button3=tk.Button(self.root,text="SYSTEM START",command=self.systemstart, background="red",width=15,height=2,font=("arial", 20,"bold"))
        self.button3.place(x=610,y=700)
        
        self.button4=tk.Button(self.root,text="SYSTEM OFF",command=self.systemoff,background="blue",width=15,height=2,font=("arial", 20,"bold"))
        self.button4.place(x=610,y=800)
       
 
    def Mensajes(self):
        
        self.label1=tk.Label(self.root,text="ARTIFICIAL INTELLIGENCE SYSTEM AI",width=35,height=2,font=("arial",60,"bold"))
        self.label1.place(x=5,y=0)
        self.label3=tk.Label(self.root,text="NORTH MAIN",width=35,height=2,font=("arial",60,"bold"))
        self.label3.place(x=5,y=125)
        self.image=tk.PhotoImage(file="sistema.png")
        self.label2 = ttk.Label(image=self.image)
        self.label2.place(x=1000,y=300)
    
    '''
    def habilitar_boton1(self,mensaje='o'):
        
        self.button1.config(state=tk.DISABLED)
        self.button2.config(state=tk.NORMAL)
        self.motorstart(mensaje)
        
    def habilitar_boton2(self):
        
        self.button1.config(state=tk.NORMAL)
        self.button2.config(state=tk.DISABLED)
        
    def habilitar_botones(self):
        
        self.button1.config(state=tk.NORMAL)
        self.button2.config(state=tk.NORMAL)
        self.button3.config(state=tk.NORMAL)
        self.button4.config(state=tk.NORMAL)
        self.button5.config(state=tk.NORMAL)
        self.button6.config(state=tk.NORMAL)
     '''    

        
        
lase=Laser()
lase.compontentes()