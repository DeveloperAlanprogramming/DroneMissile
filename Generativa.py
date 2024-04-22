import pandas as pd
import numpy as np
import tensorflow as tf
import os
import cv2
import matplotlib.pyplot as plt
from keras.models import Sequential,Model
from keras.layers import Dense,Dropout,Flatten,Conv2D,MaxPooling2D,BatchNormalization,Activation,Input,Reshape,LeakyReLU,Conv2DTranspose
from keras.datasets import mnist,fashion_mnist
from keras.utils import to_categorical
from sklearn.model_selection import train_test_split




class Generative_IAS:
    
    def __init__(self):
        
        self.path=0
        self.directorio=0
        self.imagenes=0
        self.img=0
        
        self.width=224
        self.height=224
        self.channels=1
        self.class_name=0
        self.clases=[]
        self.imagenes=[]
        self.fullpath=0
        
        self.x=0
        self.y=0
        
        self.width2=10
        self.height2=10
        self.fig=0
        self.axs=0
        self.index=0
        
        self.i=0
        self.buffer_size=0
        self.batch_size=0
        self.network=0
        self.generator=0
        self.noise=0
        self.generated_image=0
        self.generator=0
        self.image_to_show=0
          
        
    def start_directorio(self):
        
        pd.set_option('display.width', 800)
        pd.set_option('display.max_columns', 700)
        
        self.path=r'C:/Users/desca/Downloads/archive/data/todo'
        self.directorio=os.listdir(self.path)
        print(self.directorio)

    def lectura_imagnes(self):
        
        for self.img in self.directorio:
            self.fullpath=self.path+'/'+self.img

            if self.img.endswith('.jpg') or self.img.endswith('.png') or self.img.endswith('.jpeg') or self.img.endswith('.bmp'):

                try:
                    self.img=cv2.imread(self.fullpath)
                    self.img=cv2.cvtColor(self.img,cv2.COLOR_BGR2GRAY)
                    self.img=cv2.resize(self.img,(self.width,self.height))

                except:
        
                    pass

                cv2.imshow('imagen',self.img)
                cv2.waitKey(2)
                self.img=self.img.ravel()
                print(self.img.shape)
                self.imagenes.append(self.img)
                self.class_name=1
                self.clases.append(self.class_name)
                print(self.class_name)
                
    def imprimir_datos(self):
        
        print(self.imagenes)
        print("\n\n")
        print(self.clases)
        print("\n\n")
        print(type(self.imagenes))
        print("\n\n")
        print(type(self.clases))
        
    def transformacion(self):
        
        self.x=np.array(self.imagenes)
        self.y=np.array(self.clases)
        print(f'imprimiendo los datos {self.x.shape}')
        print("\n\n")

        #print(self.x[0].reshape(self.height,self.width,1).shape)
        #print("IMPRIMIENDO LOS DATOS")
        cv2.imshow('imagen',self.x[10].reshape(224,224,1))
        cv2.waitKey(5)
        
    def char(self):
        
        self.width2=10
        self.height2=10
        self.fig,self.axs=plt.subplots(self.width2,self.height2,figsize=(50,50))
        self.axs=self.axs.ravel()
        for self.i in range(0,self.width2*self.height2):
        
          self.index=np.random.randint(0,len(self.x))
          self.axs[self.i].imshow(self.x[self.index].reshape(self.height,self.width,1))
          self.axs[self.i].axis('off')
        cv2.waitKey(20)
        
        
    def Normalizacion(self):
        
        print(f'{self.x.max()}, {self.x.min()}')
        print("\n")
        self.x=(self.x-127.5)/127.5
        print(f'{self.x.max()}, {self.x.min()}')
        print("\n")
        
    def Reshape_format(self):
        
        self.x=self.x.reshape(self.x.shape[0],self.height,self.width,1).astype('float32')
        print(self.x.shape)
        
    def parametros(self):
        
        self.buffer_size=self.x.shape[0]
        self.batch_size=256
        print(f'{self.buffer_size}, {self.batch_size}')
        self.x=tf.data.Dataset.from_tensor_slices(self.x).shuffle(self.buffer_size).batch(self.batch_size)
        print(self.x)
        
        
    def Build_generator(self):
        
          self.network =Sequential()

          self.network.add(Dense(7*7*256, use_bias=False, input_shape=(100, )))
          self.network.add(BatchNormalization())
          self.network.add(LeakyReLU())
        
          self.network.add(Reshape((7, 7, 256)))
        
          # 7x7x128
          self.network.add(Conv2DTranspose(128, (5,5), padding='same', use_bias=False))
          self.network.add(BatchNormalization())
          self.network.add(LeakyReLU())
        
          # 14x14x64
          self.network.add(Conv2DTranspose(64, (5,5), strides = (2,2), padding='same', use_bias=False))
          self.network.add(BatchNormalization())
          self.network.add(LeakyReLU())
        
          # 28x28x1
          self.network.add(Conv2DTranspose(32, (5,5), strides = (2,2), padding='same', use_bias=False))
          self.network.add(BatchNormalization())
          self.network.add(LeakyReLU())
        
          # 56x56x1
          self.network.add(Conv2DTranspose(16, (5,5), strides = (2,2), padding='same', use_bias=False))
          self.network.add(BatchNormalization())
          self.network.add(LeakyReLU())
        
          # 112x112x1
          self.network.add(Conv2DTranspose(8, (5,5), strides = (2,2), padding='same', use_bias=False))
          self.network.add(BatchNormalization())
          self.network.add(LeakyReLU())
        
          # 224x224x3
          self.network.add(Conv2DTranspose(1, (5,5), strides = (2,2), padding='same', use_bias=False,activation='tanh'))
        
        
          self.network.summary()
        
          return self.network
      
    def Generator(self):
        
        self.generator=self.Build_generator()
        
    def Noise_generator(self):
        
        self.noise=tf.random.normal([1,100])
        print(self.noise)
        
    def Generated_image(self):
        
        self.generated_image=self.generator(self.noise,training=False)
        print(f'{self.generated_image},{self.generated_image.shape}')
        
    def Plot_Image(self):
        
        print(self.generated_image[0,:,:,0].shape)
        self.image_to_show=np.array(self.generated_image[0,:,:,0])
        plt.imshow(self.image_to_show,cmap='gray')
        plt.show()
        
     
        
        
        
        
        
        