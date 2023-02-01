import cv2 as cv
import numpy as np
from time import time, sleep
from WindowCapture import WindowCapture
from peopleDetectedGta import PeopleDetected


win = WindowCapture()
sleep(5)
peopleDetect=PeopleDetected()
frametime=time()
while(True):
    # get an updated image of the game
    screenshot = win.get_screenshot()
    # Recognition of 3 classes of objects:
    # Cops
    # Corpses
    # GangB
    # GangV
    result=peopleDetect.detect(screenshot)
    detection_image=peopleDetect.drawBoxes(result,screenshot)
    fps = 1 / np.round(time() - frametime, 2)
    cv.putText(detection_image, f'FPS: {int(fps)}', (20, 70), cv.FONT_HERSHEY_SIMPLEX, 1.5, (0, 255, 0), 2)
    cv.imshow('Matches', detection_image)
    frametime=time()
    if cv.waitKey(1) == ord('q'):
        cv.destroyAllWindows()
        break