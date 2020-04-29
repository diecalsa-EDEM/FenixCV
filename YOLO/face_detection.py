import cv2
import dlib
import numpy as np
from pathlib import Path

PATH = "/Users/Diego/Desktop/AI/00_PROYECTOS/01_FENIXCV/Imagenes_Sin_Etiquetar"
images = Path(PATH)
face_detector = dlib.get_frontal_face_detector()

#cap = cv2.VideoCapture(0)


image_list = list(images.iterdir())
for image in image_list:
    #ret,frame = cap.read()
    frame = cv2.imread(str(image))
    h,w,c = frame.shape
    gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    gray = cv2.resize(gray,(512,512))
    faces = face_detector(gray)
    color = (255,0,0)
    frame_rect = frame.copy()
    frame_rect = cv2.resize(frame_rect,(512,512))
    bboxes = []
    for face in faces:
        x1 = face.left()
        y1 = face.top()
        x2 = face.right()
        y2 = face.bottom()

        bbox = (x1,y1,x2-x1,y2-y1)
        bboxes.append(bbox)

        frame_rect = cv2.rectangle(frame_rect,(x1,y1),(x2,y2), color = color, thickness = 4)

    cv2.imshow("Image",frame_rect)

    if(cv2.waitKey(0) & 0xFF == ord('q')):
        break

#cap.release()
cv2.destroyAllWindows()