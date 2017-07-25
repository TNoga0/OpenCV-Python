import cv2
import numpy as np

cap = cv2.VideoCapture(1)

while(True):
    retrn, frame = cap.read()
    drawing = cv2.cvtColor(frame, cv2.CAP_MODE_BGR)

    piksele = drawing[250:450,150:350]

    #wrzucenie czesci wyswietlanego obrazu w jakas inna czesc obrazu
    # drawing[0:200, 0:200] = piksele

    #wykolorowanie czesci pikseli na obrazie
    piksele = [[255 for i in range(4)] for j in range(int(len(piksele)))]
    drawing[0:200, 0:200] = piksele


    cv2.imshow('frame', drawing)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()