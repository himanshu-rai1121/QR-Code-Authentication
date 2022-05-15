import cv2 #read image / camera / video input
from pyzbar.pyzbar import decode
import time
cap = cv2.VideoCapture(0)
cap.set(3, 640) #3 - width
cap.set(4, 480) #4 - Height
used_codes = []

camera = True
while camera == True:
    success, frame = cap.read()

    for code in decode(frame):
        if code.data.decode('utf-8') not in used_codes:
            print('Approved you can enter:')
            print(code.type)
            print(code.data.decode('utf-8'))
            used_codes.append(code.data.decode('utf-8'))
            time.sleep(2)
        elif code.data.decode('utf-8') in used_codes:
            print('Sorry this code has allready been used')
            time.sleep(2)
        else:
            pass

    cv2.imshow('Testing-code-scan', frame)
    cv2.waitKey(1)
