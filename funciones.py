import time
import serial
from tkinter import ttk,messagebox
import tkinter as tk
import cv2
import math
from Generativa import *
import threading
import multiprocessing
import pygame 



class metodos(Generative_IAS):
    

    def __init__(self):
        
        super().__init__()
        
  
        self.portSerial='COM30'
        self.baudrate=9600
        self.ser=0
        self.ret=0
        self.frame=0
        self.cap=0
        self.messaje=0
        self.color=0
        self.position=0
        self.frame_gray_init=0
        self.i=0
        self.messagebox=0
       
        self.is_camera_open = False
        self.is_capturing = False
        self.control = False
        self.generative=False
        
        self.joystick_count=0
        self.joystick=0
        self.event=0
        self.num_joysticks=0
        self.x_axis =0
        self.y_axis =0
        
        
        
        #self.ser=serial.Serial(self.portSerial, self.baudrate)
    def motorstart(self):
            
        print("Sensor")
        
    def Test(self):
        
        if not self.generative:
            
            self.generative = True

            threading.Thread(target=self.Testing).start()
            print("Entro")
        
    def Testing(self):
            
       self.start_directorio()
       self.lectura_imagnes()
       self.imprimir_datos()
       self.transformacion()
       self.Char()
       self.Normalizacion()
       self.Reshape_format()
       self.parametros()
       self.Build_generator()
       self.Generator()
       #self.Noise_generator()
       #self.Generated_image()
       #self.Plot_Image()
       
    def abrir_camara(self):
        if not self.is_camera_open:
            self.is_camera_open = True
            print("Entro en la camara")
            threading.Thread(target=self.mostrar_video).start()
            
    def mostrar_video(self):
        self.cap = cv2.VideoCapture(1)  # Cambia el número según tu dispositivo de cámara
        while self.is_camera_open:
            self.ret, self.frame = self.cap.read()
            if self.ret:
                # Muestra el fotograma en una ventana
                cv2.putText(self.frame, f'TRACKING SYSTEM', (220,100), cv2.FONT_HERSHEY_SIMPLEX, 1, (250, 0, 250), 3)
                cv2.imshow('Video', self.frame)
            if cv2.waitKey(1) & 0xFF == ord('q'):  # Presiona 'q' para salir
                break
        self.cap.release()
        cv2.destroyAllWindows()
        
    def tomar_foto(self):
        
        if not self.is_capturing:
            
            self.is_camera_open = True

            threading.Thread(target=self.capturar_foto).start()
            print("Entro")

    def capturar_foto(self):
        
        self.cap = cv2.VideoCapture(1)
        self.ret, self.frame = self.cap.read()
        
        if self.ret:
            
            cv2.imwrite(f"foto_{self.i}.png", self.frame)
            print("Foto tomada correctamente")
            self.i+=1
            print(self.i)
        self.is_capturing = False
        
        
    def close_camara(self):
        self.is_camera_open = False
        if self.capture_thread and self.capture_thread.is_alive():
            self.capture_thread.join() 
        
    
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
            
            
    def control(self):
        
        pygame.init()
        pygame.joystick.init()
        self.joystick_count = pygame.joystick.get_count()
        
        if self.joystick_count == 0:
            
            print("No se encontraron joysticks.")
            return

        self.joystick = pygame.joystick.Joystick(0)
        self.joystick.init()
        print("Joystick detectado:", self.joystick.get_name())
        
        try:
           
            while pygame.event.get():
                
                for self.event in pygame.event.get():
                    if self.event.type == pygame.QUIT:
                        return
  
                    if self.event.type == pygame.JOYBUTTONDOWN:
                        print("Botón presionado:", self.event.button)
                        
            self.is_capturing = False
                        
        finally:
            
            pygame.quit()
            
    def joystick_control(self):
        if not self.control:
            self.control = True
            print("Entro jostick")
            threading.Thread(target=self.coordenadas).start()
    
    
    def coordenadas(self):
        
        pygame.init()
        self.num_joysticks = pygame.joystick.get_count()
        
        if self.num_joysticks > 0:
            print("Se encontraron {} joysticks.".format(self.num_joysticks))
            # Inicializar el primer joystick
            self.joystick = pygame.joystick.Joystick(0)
            self.joystick.init()
        
            # Ciclo principal
            while True:
                # Manejar eventos
                for self.event in pygame.event.get():
                    if self.event.type == pygame.QUIT:
                        pygame.quit()
                        exit()
        
                # Obtener las coordenadas X e Y del joystick
                self.x_axis = self.joystick.get_axis(0)
                self.y_axis = self.joystick.get_axis(1)
        
                # Imprimir las coordenadas
                print("Coordenada X: {:.2f}, Coordenada Y: {:.2f}".format(self.x_axis, self.y_axis))
        
        else:
            print("No se encontraron joysticks conectados.")
                    

    def systemstart(self):
        
        pass
     
    def systemoff(self):
            
        pass
            
    def propulsion(self):
            
        print("Sistema de lanzamiento")
             

        
        