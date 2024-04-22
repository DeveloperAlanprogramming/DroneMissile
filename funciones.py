import time
import serial
from tkinter import ttk
import tkinter as tk
import cv2
from Generativa import *

class metodos(Generative_IAS):
    
    def __init__(self):
        
        super().__init__()
        
  
        self.portSerial='COM30'
        self.baudrate=9600
        self.ser=0
        #self.ser=serial.Serial(self.portSerial, self.baudrate)
    def motorstart(self):
            
        
        self.ser.write(b'HOLA\r\n')
        print("Sensor")
        
    def motoroff(self):
            
       self.start_directorio()
       self.lectura_imagnes()
       self.imprimir_datos()
       self.transformacion()
       self.char()
       self.Normalizacion()
       self.Reshape_format()
       self.parametros()
       self.Generator()
       self.Noise_generator()
       self.Generated_image()
       self.Plot_Image()
                
    def systemstart(self):
            
        pass
        
    def systemoff(self):
            
        pass
            
    def propulsion(self):
            
        print("Sistema de lanzamiento")
             
    def ON_LASER(self):
            
        print("ON LASER")
            
    def OFF_LASER(self):
            
        print("OFF LASER")