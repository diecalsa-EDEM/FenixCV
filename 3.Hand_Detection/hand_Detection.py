import cv2
import numpy as np
import os

print(cv2.__version__)
# Change working directory
os.chdir("/Users/Diego/Desktop/YOLO")

# Load yolov3 config and weights
#net = cv2.dnn.readNetFromDarknet("./models/yolov3_hand_2.cfg","./models/yolov3_hand_2.weights")
net = cv2.dnn.readNetFromDarknet("./models/yolov3_custom.cfg","./models/yolov3_hand_3.weights")

# Load classes to detect
classes = []
with open("obj.names", "r") as f:
    classes = [line.strip() for line in f.readlines()]

# Select the outputlayers to use
layer_names = net.getLayerNames()
output_layers = [layer_names[i[0] - 1] for i in net.getUnconnectedOutLayers()]

# Randomly generate colors to display bboxes
color = (255,0,0)

# Initialize video capture and video Writter
cap = cv2.VideoCapture(0)
ret,frame = cap.read()

# Setup variables
font = cv2.FONT_HERSHEY_PLAIN

nframe = 0

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

    #Get image size
    height, width, c = frame_disp.shape

    # Detecting objects
    blob = cv2.dnn.blobFromImage(frame, 0.00392, (224, 224), (0, 0, 0), True, crop=False)
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

            label = str(classes[class_ids[i]])
            cv2.rectangle(frame_disp, (x1, y1), (x2, y2), color, 2)
            cv2.putText(frame_disp, label, (x1, y1 + 30), font, 3, color, 3)

    cv2.imshow('frame', frame_disp)
    nframe+=1
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break


cap.release()
cv2.destroyAllWindows()

