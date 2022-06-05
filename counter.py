import cv2
import cvzone
from cvzone.FaceMeshModule import FaceMeshDetector
from cvzone.PlotModule import LivePlot
import time
from datetime import datetime
import firebase_admin
from firebase_admin import db, firestore

cap = cv2.VideoCapture(0)
detector = FaceMeshDetector(maxFaces=1) # max faces for detection is 1
plotY = LivePlot(640,360,[10,40], invert=True)

cred_obj = firebase_admin.credentials.Certificate(r'key.json')
default_app = firebase_admin.initialize_app(cred_obj, {'databaseURL': 'https://ireckon-ce2cb-default-rtdb.firebaseio.com/'})
ref = db.reference('/')
users_ref = ref.child('patients')

name = "George"

blinkCounter = 0
counter = 0
a = 1
idList = [133,155,154,153,145,144,163,7,33,246,161,160,159,158,157,173,
          362,398,384,385,386,387,388,466,263,249,390,373,374,380,381,382]
ratioList = []

l_p = time.time()
last = 0
time.sleep(1)
print("Name   Time                      ", "Blink Count")

while True:

    if cap.get(cv2.CAP_PROP_POS_FRAMES) == cap.get(cv2.CAP_PROP_FRAME_COUNT): # to run the video file infinite times
        cap.set(cv2.CAP_PROP_POS_FRAMES,0)

    success, img = cap.read()
    img, faces = detector.findFaceMesh(img, draw=False)

    if faces:
        face = faces[0] # the only face we have
        for id in idList:
            cv2.circle(img, face[id], 3, (255, 0, 0), cv2.FILLED)

        leftUp = face[159]
        leftDown = face[145]
        leftLeft = face[130]
        leftRight = face[243]
        lengthVer,_ = detector.findDistance(leftUp, leftDown)
        lengthHor,_ = detector.findDistance(leftLeft, leftRight)

        cv2.line(img, leftUp, leftDown, (0,200,0), 2)
        cv2.line(img, leftLeft, leftRight, (0,200,0), 2)


        ratio = int((lengthVer/lengthHor)*100)
        ratioList.append(ratio)
        if len(ratioList) > 4:
            ratioList.pop(0)
        ratioAvg = sum(ratioList)/len(ratioList)


        if ratioAvg < 23 and counter == 0:
            blinkCounter += 1
            counter = 1
        if counter != 0:
            counter += 1
            if counter > 10:
                counter = 0

        cvzone.putTextRect(img, f'Blinks : {blinkCounter}', (50,100), 2, 2, (255,255,255),(0,255,0), cv2.FONT )
        cvzone.putTextRect(img,f'{last}',(100,50))
        imgPlot = plotY.update(ratioAvg)
        img = cv2.resize(img, (640, 360))
        imgStack = cvzone.stackImages([img],1,1)


    else:
        img = cv2.resize(img, (640, 360))
        cvzone.putTextRect(img,f'No face found',(100,50))
        imgStack = cvzone.stackImages([img], 1, 1)


    cv2.imshow("Image", imgStack)
    cv2.waitKey(1)
    if time.time() - l_p >= 5:
        last = blinkCounter
        if blinkCounter >= 3:
            print(name, datetime.now(), blinkCounter)
            dic = {
                'time': datetime.now().timestamp(),
                'BlinkCount': blinkCounter
            }
            users_ref.push().set(dic)
        l_p = time.time()
        blinkCounter = 0
