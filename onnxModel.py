import cv2
from ultralytics import YOLO
import numpy as np
import random

model = YOLO('best.onnx',task='pose')
vid = cv2.VideoCapture(0)
thicc = 2

while (True):
    color = (0,0,255)
    _, image =  (vid.read())
    image = np.array(image)
    pred = model(image)

    tPoints = []
    keypoints = pred[0].keypoints.xy

    j = 0
    for person in keypoints:
        tPoints.append([])
        for i in range(len(person)):
            try:
                point = (int(person[i][0]), int(person[i][1]))
                cv2.circle(image, point, radius=3, color=(0,255,0),thickness=thicc)
                tPoints[j].append(point)
            except Exception as e:
                print(e)
        j+=1

    for i in range(len(tPoints)):
        # face
        try:
            cv2.line(image, tPoints[i][3], tPoints[i][1], color=color, thickness=thicc)
        except:
            pass
        try:
            cv2.line(image, tPoints[i][1], tPoints[i][0], color=color, thickness=thicc)
        except:
            pass
        try:
            cv2.line(image, tPoints[i][0], tPoints[i][2], color=color, thickness=thicc)
        except:
            pass
        try:
            cv2.line(image, tPoints[i][2], tPoints[i][4], color=color, thickness=thicc)
        except:
           pass

        #neck

        try:
            cv2.circle(image, (int((tPoints[i][3][0]+tPoints[i][4][0])/2),int((tPoints[i][3][1]+tPoints[i][4][1])/2)), 3, color, thicc)
            cv2.line(image, (int((tPoints[i][3][0]+tPoints[i][4][0])/2),int((tPoints[i][3][1]+tPoints[i][4][1])/2)), (int((tPoints[i][5][0]+tPoints[i][6][0])/2),int((tPoints[i][5][1]+tPoints[i][6][1])/2)), color=color, thickness=thicc)
        except:
            pass

        # body

        #right arm
        try:
            cv2.line(image, tPoints[i][5], tPoints[i][7], color=color, thickness=thicc)
        except:
            pass
        try:
            cv2.line(image, tPoints[i][7], tPoints[i][9], color=color, thickness=thicc)
        except:
            pass
    
        #left arm
        try:
            cv2.line(image, tPoints[i][6], tPoints[i][8], color=color, thickness=thicc)
        except:
            pass
        try:
            cv2.line(image, tPoints[i][8], tPoints[i][10], color=color, thickness=thicc)
        except:
            pass

        #torso
        try:
            cv2.line(image, tPoints[i][6], tPoints[i][5], color=color, thickness=thicc)
        except:
            pass
        try:
            cv2.line(image, tPoints[i][6], tPoints[i][12], color=color, thickness=thicc)
        except:
            pass
        try:
            cv2.line(image, tPoints[i][5], tPoints[i][11], color=color, thickness=thicc)
        except:
            pass
        try:
            cv2.line(image, tPoints[i][11], tPoints[i][12], color=color, thickness=thicc)
        except:
            pass

        #right leg
        try:
            cv2.line(image, tPoints[i][11], tPoints[i][13], color=color, thickness=thicc)
        except:
            pass
        try:
            cv2.line(image, tPoints[i][13], tPoints[i][15], color=color, thickness=thicc)
        except:
            pass

        #left leg
        try:
            cv2.line(image, tPoints[i][12], tPoints[i][14], color=color, thickness=thicc)
        except:
            pass
        try:
            cv2.line(image, tPoints[i][14], tPoints[i][16], color=color, thickness=thicc)
        except:
            pass

    shape = image.shape
    cv2.imshow('frame', cv2.resize(image, (shape[1]*3, shape[0]*3)))

    if cv2.waitKey(4) & 0xFF == ord('q'):
        break

# Destroy all the windows
cv2.destroyAllWindows()