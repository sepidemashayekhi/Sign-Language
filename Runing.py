from tkinter import Frame
import cv2 
import numpy as np 

cam=cv2.VideoCapture(0)
while True:
    _,frame=cam.read()
    frame=cv2.flip(frame,1)
   
    
    frame=cv2.rectangle(frame,(100,100),(350,350),(0,255,0),2)
    
    cv2.imshow('Frame',frame)
    
    if cv2.waitKey(1)==27:
        break

