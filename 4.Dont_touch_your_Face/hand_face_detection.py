import cv2
import numpy as np
import os
import dlib
import math

print(cv2.__version__)
# Change working directory
os.chdir("/Users/Diego/Desktop/YOLO")

# Load yolov3 config and weights
#net = cv2.dnn.readNetFromDarknet("./models/yolov3_hand_2.cfg","./models/yolov3_hand_2.weights")
net = cv2.dnn.readNetFromDarknet("./models/yolov3_custom.cfg","./models/yolov3_hand_3.weights")

# Load face detector
face_detector = dlib.get_frontal_face_detector()

# Load classes to detect
classes = []
with open("obj.names", "r") as f:
    classes = [line.strip() for line in f.readlines()]

# Select the outputlayers to use
layer_names = net.getLayerNames()
output_layers = [layer_names[i[0] - 1] for i in net.getUnconnectedOutLayers()]

# Randomly generate colors to display bboxes
colors = np.random.uniform(0, 255, size=(len(classes), 3))

# Initialize video capture and video Writter
#cap = cv2.VideoCapture(0)
cap = cv2.VideoCapture('Video_Fenix.mp4')
ret,frame = cap.read()
frame_width, frame_height, c = frame.shape

outVideo = cv2.VideoWriter('outpy.avi',cv2.VideoWriter_fourcc('M','J','P','G'), 10, (frame_height,frame_width))

# Setup variables
font = cv2.FONT_HERSHEY_PLAIN

nframe = 0

#------------------- Functions --------------------

def calculate_IoU(boxA,boxB):
    xA = min(boxA[0],boxB[0])
    yA = min(boxA[1],boxB[1])
    xB = max(boxA[2],boxB[2])
    yB = max(boxA[3],boxB[3])

    print(xA,yA,xB,yB)
    # compute the area of intersection rectangle
    interArea = max(0, xB - xA + 1) * max(0, yB - yA + 1)
    # compute the area of both the prediction and ground-truth
    # rectangles
    wA = abs(boxA[0]-boxA[2]+1)
    hA = abs(boxA[1]-boxA[3]+1)
    centerxA = xA+wA/2
    centeryA = yA+hA/2

    wB = abs(boxB[0]-boxB[2]+1)
    hB = abs(boxB[1]-boxB[3]+1)
    centerxB = xB+wB/2
    centeryB = yB+hB/2

    boxAArea = wA*hA
    boxBArea = wB*hB

    areaRatio=boxAArea/boxBArea
    centerDistance = math.sqrt((xA-xB)**2+(yA-yB)**2)

    print("Area A:",boxAArea,"Area B:",boxBArea)
    print("Area ratio:",areaRatio)
    print("Center distance:", centerDistance)

    # compute the intersection over union by taking the intersection
    # area and dividing it by the sum of prediction + ground-truth
    # areas - the interesection area

    return areaRatio, centerDistance

#------------------- Main Lop --------------------
while(cap.isOpened()):
    # Initialize color green
    color = (0,255,0)
    # New frame from video capture
    ret, frame = cap.read()

    if(not ret):
        break
    # Resize frame for displaying on display (if necessary)
    frame = cv2.resize(frame,dsize=None,fx=1,fy=1,interpolation=cv2.INTER_LINEAR)
    frame_disp = frame.copy()
    # Detect faces
    faces = face_detector(frame)
    face_bboxes=[]
    for face in faces:
        # Get the bbox
        x1 = face.left()
        y1 = face.top()
        x2 = face.right()
        y2 = face.bottom()
        bbox = (x1,y1,x2,y2)

        face_bboxes.append(bbox)
        cv2.rectangle(frame_disp,(x1,y1),(x2,y2), color = (255,0,0), thickness = 3)
        cv2.putText(frame_disp, 'Human face', (x1, y1 + 30), font, 3, (255,0,0), 3)
        #frame_disp = cv2.rectangle(frame_disp,(x,y),(x+w,y+h),color = (255,0,0), thickness = 3)

    #Get image size
    height, width, c = frame_disp.shape

    # Detecting objects
    blob = cv2.dnn.blobFromImage(frame, 0.00392, (416, 416), (0, 0, 0), True, crop=False)
    net.setInput(blob)
    outs = net.forward(output_layers)

    # Showing informations on the screen
    class_ids = []
    confidences = []
    hand_bboxes = []
    for out in outs:
        for detection in out:
            scores = detection[5:]
            class_id = np.argmax(scores)
            confidence = scores[class_id]
            if confidence > 0.2:
                hand_detected = True

                # Object detected
                center_x = int(detection[0] * width)
                center_y = int(detection[1] * height)
                w = int(detection[2] * width)
                h = int(detection[3] * height)

                # Rectangle coordinates
                x1 = int(center_x - w / 2)
                y1 = int(center_y - h / 2)
                x2 = int(center_x + w / 2)
                y2 = int(center_y + h / 2)

                hand_bboxes.append([x1, y1, x2, y2])
                confidences.append(float(confidence))
                class_ids.append(class_id)

    indexes = cv2.dnn.NMSBoxes(hand_bboxes, confidences, 0.1, 0.1)
    #print(indexes)

    for i in range(len(hand_bboxes)):
        if i in indexes:
            x1, y1, x2, y2 = hand_bboxes[i]
            bbox = (x1,y1,x2,y2)

            for face_bbox in face_bboxes:
                aratio,cdistance = calculate_IoU(hand_bboxes[i],face_bbox)

                if aratio<2 and cdistance<550:
                    color = (0,0,255)

            label = str(classes[class_ids[i]])
            cv2.rectangle(frame_disp, (x1, y1), (x2, y2), color, 2)
            cv2.putText(frame_disp, label, (x1, y1 + 30), font, 3, color, 3)

    cv2.imshow('frame', frame_disp)
    outVideo.write(frame_disp)
    nframe+=1
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break


cap.release()
outVideo.release()
cv2.destroyAllWindows()

