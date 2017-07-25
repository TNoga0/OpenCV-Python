import cv2
import numpy as np

cap = cv2.VideoCapture(1)

while(True):
    retrn, frame = cap.read()
    drawing = cv2.cvtColor(frame, cv2.CAP_MODE_BGR)

    #cv2.line(drawing,(0,0),(100,100),(255,255,255),10) #rysowanie na drawing, nie frame
    cv2.rectangle(drawing,(20,20),(100,100),(200,200,200),3)
    cv2.circle(drawing,(150,150),20,(255,255,255),-1)

    font = cv2.FONT_HERSHEY_COMPLEX
    cv2.putText(drawing,'No elo',(20,400), font, 1, (255,255,255), 3)

    cv2.imshow('frame', drawing)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()


