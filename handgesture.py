# -*- coding: utf-8 -*-
import cv2 
import time
import numpy as np
import HandTrackingModule as htm
import math


width , height= 640,480


cap = cv2.VideoCapture(0)
# cap.set(3,width)
# cap.set(4,height)

detector = htm.HandDetector(detectionCon=0.7)

trigger=False
pTime=0

#def HandGesture:
while True:
    success, img =cap.read()
    img = detector.findHands(img)
    lmList= detector.findPosition(img, draw=False)
    
    cTime=time.time()
    fps= 1/(cTime -pTime)
    pTime= cTime
    
    cv2.putText(img, f'FPS: {int(fps)}', (100,70), cv2.FONT_HERSHEY_PLAIN,1,(0,0,255),1)
    
    if len(lmList) !=0:
        
        thumb=lmList[4]
        index=lmList[8]
        middle=lmList [12]
        ring=lmList[16]
        pinky=lmList[20]
        
       # print("hallo: ",a)
    #     #https://google.github.io/mediapipe/solutions/hands.html 
    #     # Shows the lm (Landmarks) which are interesting
    #     # 4 for example is the thumb
         
        x1, y1 = lmList[4][1],lmList[4][2] # Daumen
        
        x2, y2 = lmList[8][1],lmList[8][2] # Zeigefinger
        cx, cy = (x1+x2)//2, (y1+y2)//2
        
        cv2.circle(img, (x1,y1) , 15, (255,0,0), cv2.FILLED)
        cv2.circle(img, (x2,y2) , 15, (255,0,0), cv2.FILLED)
        cv2.line(img,(x1,y1),(x2,y2),(255,0,255),3)
        
        if index[2] < middle[2] and index[2] < ring[2] and index[2] < thumb[2]:
            if pinky[2] < middle[2] and pinky[2] < ring[2] and pinky[2] < thumb[2]:
                trigger=True
                #return True
        else:
            trigger=False
            #return False     
        print(index[2])
        cv2.putText(img,f'State: {bool(trigger)}', (100,100), cv2.FONT_HERSHEY_PLAIN, 2, (255,0,0),2)
    
        print(trigger)
    cv2.imshow("img", img)
    cv2.waitKey(1)

