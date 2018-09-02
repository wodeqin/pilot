import cv2
import os
import PIL.Image as image
import numpy as np
import datetime
import time
import upload as up

cap = cv2.VideoCapture(0)
face_cascade = cv2.CascadeClassifier(r'./haarcascade_frontalface_default.xml')

while(1):

    ret, img = cap.read()

    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # 探测图片中的人脸
    faces = face_cascade.detectMultiScale(
        gray,
        scaleFactor=1.15,
        minNeighbors=5,
        minSize=(5, 5),
        flags=cv2.IMREAD_GRAYSCALE
    )

    print("发现%d个人脸!" % len(faces))

    for (x, y, w, h) in faces:
        nowTime = datetime.datetime.now().strftime('%Y%m%d%H%M%S')
        if os.path.exists(r'./storage/%s" % nowTime + ".jpg"') :
            continue
        imgArray = np.array(img)
        outputImg = image.fromarray(imgArray)
        file = "./storage/%s" % nowTime + ".jpg"
        outputImg.save(file)
        cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2)
        # cv2.circle(image,((x+x+w)/2,(y+y+h)/2),w/2,(0,255,0),2)
        up.imagesUpload(file)
        time.sleep(5)
        break

    cv2.imshow("Find Faces!", img)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release

cv2.destroyAllWindows
