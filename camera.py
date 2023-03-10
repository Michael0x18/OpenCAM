import cv2
import numpy as np
import time
import datetime
import imutils

import os

import config

import backend

cap = cv2.VideoCapture(0)

cap.set(cv2.CAP_PROP_FRAME_WIDTH, 800)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 600)

counter = 0
lastframe = None

def init_cv():
    pass
    #global cap
    #cap = cv2.VideoCapture(0)

def mainloop():
    global lastframe
    global counter
    while(True):
        if( config.mode == "auto" ):
            a = 1
            # TODO Check phone stuff
        while( config.mode == "disable"):
            time.sleep(5)
        _, frame = cap.read()
        #frame = imutils.resize(frame, width = 800)
        if lastframe is None:
            lastframe = frame
        
        delta = cv2.absdiff(cv2.cvtColor(lastframe, cv2.COLOR_BGR2GRAY), cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)) # subtract
        thresh = cv2.threshold(delta, 25, 255, cv2.THRESH_BINARY)[1]
        cnts = cv2.findContours(thresh.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
        cnts = imutils.grab_contours(cnts) 
    
        found = False

        for c in cnts:
            if(cv2.contourArea(c) < 10000):
                continue
            if(cv2.contourArea(c) >= (frame.shape[0]-10) * (frame.shape[1]-10)):
                print("It's too big")
                continue
            print("MOTION DETECTED")
            (x, y, w, h) = cv2.boundingRect(c)
            cv2.rectangle(frame, (x, y), (x+w, y+ h), (0, 255, 0))
            found = True
        if(found):
            print("Motion")
            string = "drive/" + str(datetime.datetime.now())+"_MOTION.jpg"
            cv2.imwrite(string, frame)
            backend.send(["MotionChannel","image",string])
            counter = 0
        if(counter > config.LogInterval):
            print("Writing frame");
            string = "drive/" + str(datetime.datetime.now())+"_MOTION.jpg"
            cv2.imwrite(string,frame)
            backend.send(["GeneralChannel","image",string])
            counter = 0;
        counter += config.PictureInterval
        time.sleep(config.PictureInterval)
        lastframe = frame;


def getpic():
    _, frame = cap.read()
    #frame = imutils.resize(frame, width = 1920)
    cv2.imwrite("/dev/shm/tmp.png", frame)
    return "/dev/shm/tmp.png"
