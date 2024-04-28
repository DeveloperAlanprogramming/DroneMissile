import tkinter
import cv2
import numpy as np
import math
import time

cap = cv2.VideoCapture(1)
ret, frame = cap.read()
frame_gray_init = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

parameters = dict(winSize=(85, 85),
                               maxLevel=2,
                               criteria=(cv2.TERM_CRITERIA_EPS | cv2.TERM_CRITERIA_COUNT, 10, 0.05))


def select_point(event, x, y, flags, params):
    
    global point, selected_point, old_points
    if event == cv2.EVENT_LBUTTONDOWN or cv2.EVENT_MOUSEMOVE:
        point = (x, y)
        selected_point = True
        old_points = np.array([[x, y]], dtype=np.float32)
        
cv2.namedWindow('Frame')
cv2.setMouseCallback('Frame', select_point)
selected_point = False
point = ()
old_points = np.array([[]])
mask = np.zeros_like(frame)

x=0
y=0
coord_x=0
coord_y=0
while True:
    ret, frame = cap.read()
    
    frame_gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    cv2.putText(frame, "Positioning System", (50,50), cv2.FONT_HERSHEY_SIMPLEX, 2, (0, 0, 255), 5)
    if selected_point is True:
        cv2.circle(frame, point, 5, (0, 0, 255), 2)

        new_points, status, errors = cv2.calcOpticalFlowPyrLK(frame_gray_init,
                                                              frame_gray,
                                                              old_points,
                                                              None,
                                                             **parameters)    
        frame_gray_init = frame_gray.copy()
        old_points = new_points

        x, y = new_points.ravel()
        j, k = old_points.ravel()

        coord_x="{:.2f}".format(x)
        coord_y="{:.2f}".format(y)
        mask = cv2.line(mask, (int(x), int(y)), (int(j), int(k)), (0, 255, 255), 5)
        
        frame = cv2.circle(frame, (int(x), int(y)), 10, (0, 255, 0), -1)
        img = cv2.add(frame, mask)

        cv2.putText(frame, f'Target XY:: {coord_x}, {coord_y}', (0,150), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 0, 0), 2)
        #cv2.putText(frame, f'Y::{coord_y}', (0,210), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 0, 0), 2)
        
        if float(coord_x) > 280 and float(coord_y) >280:
            
            cv2.putText(frame, f'TRACKING SYSTEM', (250,100), cv2.FONT_HERSHEY_SIMPLEX, 1, (250, 0, 250), 3)
        
            
    cv2.imshow("Frame", frame)
    cv2.imshow("Frame 2", mask)

    key = cv2.waitKey(1)
    if key == 27:
        break

cap.release()
cv2.destroyAllWindows()
    