import numpy as np
import pandas as pd
import cv2
import csv
from datetime import datetime

now = datetime.now()
time = now.strftime("%S")


object_detector = cv2.createBackgroundSubtractorMOG2(history=300, varThreshold=40)

def detect(frame):

    frame = object_detector.apply(frame)
    ret, frame = cv2.threshold(frame, 254, 255, cv2.THRESH_BINARY)
    contours, ret = cv2.findContours(frame, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

    centers = []

    for cnt in contours:
        area = cv2.contourArea(cnt)
        if area > 500:
            x, y, w, h = cv2.boundingRect(cnt)
            centers.append(np.array([[x],[y]]))

    return centers, frame
