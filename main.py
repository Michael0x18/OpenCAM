import os
import cv2
import time
import datetime
import threading
import numpy as np

import config
import camera
import backend
import scanner

class COLORS:
    RED = '\u001b[31;1m'
    GREEN = '\u001b[32;1m'
    BLUE = '\u001b[34;1m'
    CYAN = '\u001b[36;1m'
    WHITE = '\u001b[37;1m'
    RESET = '\u001b[0m'
    BOLD = '\u001b[1m'
    BACKGROUND_CYAN = '\u001b[46;1m'

def main():
    print(COLORS.CYAN+ "=========================================")
    print(COLORS.CYAN+ "=       "+COLORS.GREEN+"Open Security Camera V2.0       "+COLORS.CYAN+"=")
    print(COLORS.CYAN+ "=========================================")
    print(COLORS.RESET+"Loading configuration...")
    config.init_config()
    print("Message Backend selected: " + config.MessageBackend)
    print("Initializing backend...")
    backend.init_backend()
    print("Initializing OpenCV...")
    camera.init_cv()
    print("Starting bluetooth scanner...")
    scanner.go()
    print("Starting main logging loop...")
    camera.init_cv()
    camera.mainloop()
main()
