#!/usr/bin/env python
from time import time
import cv2 as cv
import numpy as np


class Camera(object):
    def __init__(self):
        self.video = cv.VideoCapture(0)
        # self.frames = [open('static\\' + f + '.jpg', 'rb').read() for f in ['1', '2', '3']]

    def get_frame(self):
        if self.video.isOpened():
            return np.array(cv.imencode('.jpg', self.video.read()[1])[1]).tobytes()
        return np.array(cv.imencode('.jpg', np.ones((5, 5)))[1]).tobytes()
