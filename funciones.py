import time
import serial
from tkinter import ttk
import tkinter as tk
import cv2
import math
from Generativa import *
import threading

class metodos(Generative_IAS):
    
    def __init__(self):
        
        super().__init__()
        
  
        self.portSerial='COM30'
        self.baudrate=9600
        self.ser=0
        #self.ser=serial.Serial(self.portSerial, self.baudrate)
    def motorstart(self):
            
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
       
       #definicion de las variables cam
       
       self.ret=0
       self.frame=0
       self.cap=0
       self.messaje=0
       self.color=0
       self.position=0
       self.frame_gray_init=0
       
    
    def sendopencam(self,mensaje):
        
        print("Enviando dato {}".format(mensaje))
        
        self.cap = cv2.VideoCapture(1)
        
        if mensaje=="ON":
            self.ret, self.frame = self.cap.read()
            mensaje="OFF"
            self.frame_gray_init = cv2.cvtColor(self.frame, cv2.COLOR_BGR2GRAY)
            cv2.imshow("Frame", self.frame)

        else:
            
            mensaje="ON"
            self.cap.release()
            cv2.destroyAllWindows()
    

            
    def opencam(self):
        
        self.sendopencam("ON")
        
    def cloasecam(self):
        
        self.sendopencam("OFF")
        
       
    def closecam(self):
        
        self.cap.release()
        cv2.destroyAllWindows()
    
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
        
    def abrir_camara(self):
        if not self.is_camera_open:
            self.is_camera_open = True
            self.capture_thread = threading.Thread(target=self.mostrar_video)
            self.capture_thread.start()

    def mostrar_video(self):
        cap = cv2.VideoCapture(1)  # Cambia el número según tu dispositivo de cámara
        while self.is_camera_open:
            ret, frame = cap.read()
            if ret:
                # Muestra el fotograma en una ventana
                cv2.imshow('Video', frame)
            if cv2.waitKey(1) & 0xFF == ord('q'):  # Presiona 'q' para salir
                break
        cap.release()
        cv2.destroyAllWindows()
        
    def close_camara(self):
        self.is_camera_open = False
        if self.capture_thread and self.capture_thread.is_alive():
            self.capture_thread.join() 
        
        