import cv2
import numpy as np
import os
import dlib

# Change working directory
os.chdir("/Users/Diego/Desktop/YOLO")

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

# Load dlib Face detector
face_detector = dlib.get_frontal_face_detector()
#face_detector = dlib.cnn_face_detection_model_v1("./models/mmod_human_face_detector.dat")

# Initialize video capture
cap = cv2.VideoCapture(0)


nframe = 0
face_detected = False
hand_detected = False

#------------------- Main Lop --------------------
while(cap.isOpened()):
    # New frame from video capture
    ret, frame = cap.read()

    # Resize frame for displaying on display (if necessary)
    frame = cv2.resize(frame,dsize=None,fx=0.5,fy=0.5,interpolation=cv2.INTER_LINEAR)

    frame_disp = frame.copy()
    #Get image size
    height, width, c = frame_disp.shape

    try:
        bboxes = []
        if(nframe == 0 or not face_detected):
            nframe+=1
            face_tracker = cv2.MultiTracker_create()

            # Detect faces
            faces = face_detector(frame)
            bboxes=[]
            for face in faces:
                face_detected = True
                # Get the bbox
                x1 = face.left()
                y1 = face.top()
                x2 = face.right()
                y2 = face.bottom()
                bbox = (x1,y1,x2-x1,y2-y1)

                #x = face.rect.left()
                #y = face.rect.top()
                #w = face.rect.right() - x
                #h = face.rect.bottom() - y
                #bbox = (x,y,w,h)
                face_tracker.add(cv2.TrackerCSRT_create(), frame, bbox)
                bboxes.append(bbox)

                # Face bbox
                frame_disp = cv2.rectangle(frame_disp,(x1,y1),(x2,y2), color = (255,0,0), thickness = 3)
                #frame_disp = cv2.rectangle(frame_disp,(x,y),(x+w,y+h),color = (255,0,0), thickness = 3)
        else:
            nframe+=1
            ok,bboxes = face_tracker.update(frame)

            if(not ok):
                face_detected = False
            else:
                for i,bbox in enumerate(bboxes):
                    p1 = (int(bbox[0]), int(bbox[1]))
                    p2 = (int(bbox[0] + bbox[2]), int(bbox[1] + bbox[3]))
                    frame_disp = cv2.rectangle(frame_disp,p1,p2, color = (0,255,0), thickness = 3)

        # Detecting objects
        blob = cv2.dnn.blobFromImage(frame, 0.00392, (128, 128), (0, 0, 0), True, crop=False)

        net.setInput(blob)
        outs = net.forward(output_layers)


        # Showing informations on the screen
        class_ids = []
        confidences = []
        boxes = []
        for out in outs:
            for detection in out:
                scores = detection[5:]
                class_id = np.argmax(scores)
                confidence = scores[class_id]
                if confidence > 0.2:
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

