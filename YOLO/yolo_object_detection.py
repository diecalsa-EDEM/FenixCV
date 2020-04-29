import cv2
import numpy as np
import os
import dlib

# Change working directory
os.chdir("/Users/Diego/Desktop/YOLO")

#--------- Load Yolo hand detector ---------------
# Load yolov3 config and weights
net = cv2.dnn.readNetFromDarknet("./models/yolov3_hand_2.cfg","./models/yolov3_hand_2.weights")

# Load classes to detect
classes = []
with open("obj.names", "r") as f:
    classes = [line.strip() for line in f.readlines()]

# Select the outputlayers to use
layer_names = net.getLayerNames()
output_layers = [layer_names[i[0] - 1] for i in net.getUnconnectedOutLayers()]

# Randomly generate colors to display bboxes
colors = np.random.uniform(0, 255, size=(len(classes), 3))
#-------------------------------------------------

#--------- Load dlib Face detector ---------------
face_detector = dlib.get_frontal_face_detector()
#-------------------------------------------------

# Initialize video capture
cap = cv2.VideoCapture(0)

#------------------- Main Lop --------------------
while(cap.isOpened()):
    # New frame from video capture
    ret, frame = cap.read()

    # Resize frame for displaying on display (if necessary)
    frame = cv2.resize(frame,dsize=None,fx=0.5,fy=0.5,interpolation=cv2.INTER_LINEAR)
    
    # Convert to grayscale for face detection
    gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)

    frame_disp = frame.copy()
    #Get image size
    height, width, c = frame_disp.shape

    try:
        # Detecting objects
        blob = cv2.dnn.blobFromImage(frame, 0.00392, (128, 128), (0, 0, 0), True, crop=False)

        net.setInput(blob)
        outs = net.forward(output_layers)

        # Detect faces
        faces = face_detector(gray)
        bboxes=[]
        for face in faces:
            # Get the bbox
            x1 = face.left()
            y1 = face.top()
            x2 = face.right()
            y2 = face.bottom()
            bbox = (x1,y1,x2-x1,y2-y1)
            bboxes.append(bbox)

            frame_disp = cv2.rectangle(frame_disp,(x1,y1),(x2,y2), color = (255,0,0), thickness = 3)
        # Showing informations on the screen
        class_ids = []
        confidences = []
        boxes = []
        for out in outs:
            for detection in out:
                scores = detection[5:]
                class_id = np.argmax(scores)
                confidence = scores[class_id]
                if confidence > 0.5:
                    # Object detected
                    center_x = int(detection[0] * width)
                    center_y = int(detection[1] * height)
                    w = int(detection[2] * width)
                    h = int(detection[3] * height)

                    # Rectangle coordinates
                    x = int(center_x - w / 2)
                    y = int(center_y - h / 2)

                    boxes.append([x, y, w, h])
                    confidences.append(float(confidence))
                    class_ids.append(class_id)

        indexes = cv2.dnn.NMSBoxes(boxes, confidences, 0.1, 0.1)
        #print(indexes)
        font = cv2.FONT_HERSHEY_PLAIN
        for i in range(len(boxes)):
            if i in indexes:
                x, y, w, h = boxes[i]
                label = str(classes[class_ids[i]])
                color = colors[i]
                cv2.rectangle(frame_disp, (x, y), (x + w, y + h), (255,0,0), 2)
                cv2.putText(frame_disp, label, (x, y + 30), font, 3, (255,0,0), 3)
        cv2.imshow('frame', frame_disp)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    except:
        print("An exception occurred")

cap.release()
cv2.destroyAllWindows()

