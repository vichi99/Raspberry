import cv2
import numpy as np
from picamera.array import PiRGBArray
from picamera import PiCamera
import time
import cv2
import argparse
import imutils
from imutils import perspective
from imutils import contours
from scipy.spatial import distance as dist
from time import sleep
import copy
import RPi.GPIO as GPIO
height=3280
width=2464

import os

GPIO.setmode(GPIO.BCM)
GPIO.setup(26,GPIO.OUT)
GPIO.setup(21,GPIO.OUT)

##camera = PiCamera()
##camera.resolution = (height, width)
##camera.framerate = 15
##rawCapture = PiRGBArray(camera, size=(height, width))
a=200
b=2000
c=750
d=2600
e=d-c

while True:
    try:
        # allow the camera to warmup
##        time.sleep(3)
##        camera.capture('testiik.png')
##        time.sleep(3)
##        image = cv2.imread('/home/pi/Desktop/testiik.png')
##        image = image[a:b, c:d]
        os.system("raspistill -t 1000 -o /home/pi/Desktop/pokus11.png -w 3280 -h 2464")


        image = cv2.imread('/home/pi/Desktop/pokus11.png')
        image = image[a:b, c:d]

        
        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        blur = cv2.GaussianBlur(gray, (7, 7), 0)
        _, thresh = cv2.threshold(blur,150,255,cv2.THRESH_BINARY_INV+cv2.THRESH_OTSU)
        
        diry = np.ones((5,5),np.uint8)
        close = cv2.morphologyEx(thresh, cv2.MORPH_CLOSE, diry)          
        des = cv2.bitwise_not(close)


        _,contour,hier = cv2.findContours(des,cv2.RETR_CCOMP,cv2.CHAIN_APPROX_SIMPLE)
        if hier != None:
            #print(contour) 
            for cnt in contour:               
                if cv2.contourArea(cnt) > 50000:
                    cv2.drawContours(des,[cnt],0,255,-1)
                    #delka = cv2.arcLength(cnt,True)
                    #print(delka)
                    #print(cv2.contourArea(cnt ))
                else:                    
                    cv2.drawContours(des,[cnt],0,0,0)
        grays = cv2.bitwise_not(des)
        diry1 = np.ones((15,15),np.uint8)
        grays = cv2.morphologyEx(grays, cv2.MORPH_OPEN, diry1)
        
##        rows,cols = grays.shape[:2]
##        print("row",rows)
##        print("cols",cols)
##        print("e",e)
        delka1=e-cv2.countNonZero(grays[200,:])
        delka2=e-cv2.countNonZero(grays[300,:])
        delka3=e-cv2.countNonZero(grays[400,:])
        delka4=e-cv2.countNonZero(grays[500,:])
        delka5=e-cv2.countNonZero(grays[600,:])
        delka6=e-cv2.countNonZero(grays[700,:])
        delka7=e-cv2.countNonZero(grays[900,:])
        delka8=e-cv2.countNonZero(grays[1100,:])
        delka9=e-cv2.countNonZero(grays[1400,:])
        delka10=e-cv2.countNonZero(grays[1600,:])
        delka_mean=np.mean([delka1,delka2,delka3,delka4,delka5,delka6,delka7,delka8,delka9,delka10])
        print("delka",delka_mean)
        cv2.imwrite('/home/pi/Desktop/grays.png',grays)
        
        if delka_mean > 1535:
            GPIO.output(21,1)
            GPIO.output(26,1)
        if delka_mean < 1535 and delka_mean > 1300:
            GPIO.output(21,1)
            GPIO.output(26,0)
        if delka_mean < 1300:
            GPIO.output(21,0)
            GPIO.output(26,0)
##        else:
##            GPIO.output(26,0)
##            GPIO.output(21,0)

               
        key = cv2.waitKey(200)
        #rawCapture.truncate(0)
        # clear the stream in preparation for the next frame

    except: pass
        ##print("chyba")





