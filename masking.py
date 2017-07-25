import numpy as np
import cv2

capt = cv2.VideoCapture(1)

while(True):
    retrn, frame = capt.read()
    #masking = cv2.cvtColor(frame, cv2.CAP_MODE_BGR)
    logo = cv2.imread('logo.jpg')

    #region of interest, o odpowiednich wymiarach
    rows,cols,channels = logo.shape
    regOfInt = frame[0:rows,0:cols]

    #maska loga i odwrocona maska
    togray = cv2.cvtColor(logo,cv2.COLOR_BGR2GRAY)

    #threshold
    retrn, mask = cv2.threshold(togray, 240, 255, cv2.THRESH_BINARY_INV)
    mask_inv = cv2.bitwise_not(mask)

    #wyczernienie loga w R.O.I.
    frame_bg = cv2.bitwise_and(regOfInt,regOfInt, mask=mask_inv)

    #wyciecie loga
    logo_fg = cv2.bitwise_and(logo,logo,mask=mask)

    dest = cv2.add(frame_bg,logo_fg)
    #cv2.imshow('logogogogo', dest)
    frame[0:rows,0:cols] = dest

    cv2.imshow('Logomasking', frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

capt.release()
cv2.destroyAllWindows()