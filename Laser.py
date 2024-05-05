

from tkinter import ttk
import tkinter as tk
from funciones import *
from PIL import Image, ImageTk 
import cv2
import pygame
from tkinter import Toplevel
import threading
import multiprocessing
import serial


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
        self.button8=0
        self.button9=0
        self.button10=0
        self.button11=0
        self.buttontake=0
        self.label1=0
        self.label2=0
        self.label3=0
        self.label4=0
        self.label5=0
        
     
        self.image=0
        self.frame_rgb=0
        self.img_tk=0
        self.img=0
        self.capture_thread = None
        
        self.root =tk.Tk()
        self.root.title("Laser Applications")
        self.root.geometry('2000x2000')
        self.is_camera_open = False
        self.frame=0
        self.ret=0
        self.cap = cv2.VideoCapture(1)
        self.frame_gray_init=0
        
        self.video_window = tk.Toplevel(self.root)
        self.video_window.title("Video de la Webcam")
        self.canvas = tk.Canvas(self.video_window, width=640, height=480)
        self.canvas.pack()
        #self.control()
        
        self.compontentes()
        #self.coordenadas()
        
    def compontentes(self):
        
        self.caja_botones()
        self.Mensajes()
        self.root.mainloop()   
        
    def caja_botones(self):
        
        
        self.buttontake=tk.Button(self.root,text="TAKING PHOTO",command=self.tomar_foto,background="dark gray",width=38,height=2,font=("arial", 26,"bold"))
        self.buttontake.place(x=30,y=580)
        
        self.button1=tk.Button(self.root,text="OPEN",command=self.abrir_camara, background="gray",width=10,height=2,font=("arial", 20,"bold"))
        self.button1.place(x=30,y=700)
        
        self.button2=tk.Button(self.root,text="CLOSE",command=self.close_camara,background="gray",width=10,height=2,font=("arial", 20,"bold"))
        self.button2.place(x=30,y=800)
        
        self.button3=tk.Button(self.root,text="GENERATIVE AI OFF",command=self.Serie_dataForward, background="gray",width=20,height=2,font=("arial", 20,"bold"))
        self.button3.place(x=220,y=700)
        
        self.button4=tk.Button(self.root,text="GENERATIVE AI ON",command=self.Test,background="gray",width=20,height=2,font=("arial", 20,"bold"))
        self.button4.place(x=220,y=800)
        
        self.button5=tk.Button(self.root,text="SYSTEM START",command=self.joystickC, background="gray",width=15,height=2,font=("arial", 20,"bold"))
        self.button5.place(x=576,y=700)
        
        self.button6=tk.Button(self.root,text="SYSTEM OFF",command=self.systemoff,background="gray",width=15,height=2,font=("arial", 20,"bold"))
        self.button6.place(x=576,y=800)
        
        self.button7=tk.Button(self.root,text="AUTOMATIC POSITION",command=self.joystick_control, background="dark gray",width=38,height=2,font=("arial", 26,"bold"))
        self.button7.place(x=30,y=900)
                
        '''CONTROL DEL MOTOR PASO A PASO POSICIONAMIENTO'''
        self.button8=tk.Button(self.root,text = u'\u25b2',command=self.systemstart, background="red",width=3,height=1,font=("arial", 20,"bold"))
        self.button8.bind("<Button-1>")
        self.button8.place(x=900,y=780)
        
        self.button9=tk.Button(self.root,text = u'\u25bc',command=self.systemstart, background="red",width=3,height=1,font=("arial", 20,"bold"))
        self.button9.bind("<Button-1>")
        self.button9.place(x=900,y=920)
        
        self.button10=tk.Button(self.root,text = u'\u25b6',command=self.systemstart, background="green",width=3,height=1,font=("arial", 20,"bold"))
        self.button10.bind("<Button-1>")
        self.button10.place(x=930,y=850)
        
        self.button11=tk.Button(self.root,text = u'\u25c0',command=self.systemstart, background="green",width=3,height=1,font=("arial", 20,"bold"))
        self.button11.bind("<Button-1>")
        self.button11.place(x=860,y=850)
        
    def Mensajes(self):
        
        self.label1=tk.Label(self.root,text="ARTIFICIAL INTELLIGENCE SYSTEM AI",width=35,height=2,font=("arial",50,"bold"))
        self.label1.place(x=300,y=0)
        self.label3=tk.Label(self.root,text="NORTH MAIN",width=35,height=2,font=("arial",50,"bold"))
        self.label3.place(x=300,y=125)
        self.image=tk.PhotoImage(file="sistema.png")
        self.label2 = ttk.Label(image=self.image)
        self.label2.place(x=1000,y=300)
 
laser=Laser()

