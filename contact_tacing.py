import cv2
from pyzbar.pyzbar import decode
import numpy as np
from datetime import datetime

#camera
cap = cv2.VideoCapture(0)
cap.set(3,640) #width
cap.set(4,480) #height

while True:
    data, img = cap.read()
    for qr_code in decode(img):
        my_data = qr_code.data.decode("utf-8")

        #add lines to qrcode
        color = np.array([qr_code.polygon], np.int32)
        color = color.reshape((-1,1,2))
        cv2.polylines(img,[color], True,(0,0,225),3)

        #date and time
        now = datetime.now()
        date_time = now.strftime("Time: %H:%M:%S %p %z \n Date: %B %d, %Y")

        my_data_text = open('Nieto.txt', 'w')
        my_data_text.write(f'{my_data}\n\n{date_time}')

        cv2.imshow('QRCodeScanner App', img)
        if cv2.waitKey(1) == ord('q'):
            break