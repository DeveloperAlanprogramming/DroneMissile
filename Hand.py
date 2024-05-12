import cv2
import mediapipe as mp
import serial
import pandas as pd 
import numpy as np 
import matplotlib.pyplot as plt



mp_drawing = mp.solutions.drawing_utils
mp_drawing_styles = mp.solutions.drawing_styles
mp_hands = mp.solutions.hands
cap = cv2.VideoCapture(1)
ser=serial.Serial(port="COM6", baudrate=9600)

with mp_hands.Hands(
    
    static_image_mode=False,
    max_num_hands=2,
    min_detection_confidence=0.5
   ) as hands:
    
    while True:
        
        ret,frame=cap.read()
        fingerCount = 0
        if ret==False:
            
            break
        
        height,width,_=frame.shape
        frame=cv2.flip(frame,1)
        frame_rgb=cv2.cvtColor(frame,cv2.COLOR_BGR2RGB)
        results=hands.process(frame_rgb)
        
        if results.multi_hand_landmarks:

            for hand_landmarks in results.multi_hand_landmarks:
                
                handIndex = results.multi_hand_landmarks.index(hand_landmarks)
                handLabel = results.multi_handedness[handIndex].classification[0].label
                mp_drawing.DrawingSpec(color=(255,0,0),thickness=4)
                handLandmarks = []

                for landmarks in hand_landmarks.landmark:
                  handLandmarks.append([landmarks.x, landmarks.y])
                  
                if handLabel == "Left" and handLandmarks[4][0] > handLandmarks[3][0]:
          
                    fingerCount = fingerCount+1
                elif handLabel == "Right" and handLandmarks[4][0] < handLandmarks[3][0]:
          
                    fingerCount = fingerCount+1
                
                if handLandmarks[8][1] < handLandmarks[6][1]:       #Index finger
                  fingerCount = fingerCount+1
                if handLandmarks[12][1] < handLandmarks[10][1]:     #Middle finger
                  fingerCount = fingerCount+1
                if handLandmarks[16][1] < handLandmarks[14][1]:     #Ring finger
                  fingerCount = fingerCount+1
                if handLandmarks[20][1] < handLandmarks[18][1]:     #Pinky
                  fingerCount = fingerCount+1
                  
                mp_drawing.draw_landmarks(frame,
                                            hand_landmarks,
                                            mp_hands.HAND_CONNECTIONS,
                                         )
        
        cv2.putText(frame, str(fingerCount), (50, 450), cv2.FONT_HERSHEY_SIMPLEX, 3, (255, 0, 0), 10)
        
        if fingerCount==1:
            
            cv2.rectangle(frame,(0,0),(80,80),(125,220,0),-1)
            ser.write(b'1')
        if fingerCount==2:
            
            ser.write(b'2')
            cv2.rectangle(frame,(0,0),(80,80),(125,220,0),-1)
            cv2.rectangle(frame,(82,0),(170,80),(255,0,0),-1)
            
        if fingerCount==3:
            
            ser.write(b'3')
            cv2.rectangle(frame,(0,0),(80,80),(125,220,0),-1)
            
        if fingerCount==4:
            ser.write(b'4')
            cv2.rectangle(frame,(0,0),(80,80),(125,220,0),-1)
            
        if fingerCount==5:
            ser.write(b'5')
            cv2.rectangle(frame,(0,0),(80,80),(125,220,0),-1)
        
        cv2.imshow("frame",frame)
        if cv2.waitKey(1) & 0XFF==27:
            
            break

cap.release()
cv2.destroyAllWindows()
        
        
        
        