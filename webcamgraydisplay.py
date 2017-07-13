import cv2
from matplotlib import pyplot as plt
import numpy

cap = cv2.VideoCapture(1)

while(True):
    retrn, frame = cap.read()
    gryscale = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    cv2.imshow('frame', gryscale)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()