import torch
import cv2
from time import time

class PeopleDetected:
    # best2 my scales created on the yolov5 architecture.
    def __init__(self,model_name='best'):
        self.model = torch.hub.load('C:/Users/gotic/yolov5','custom', model_name,source='local')
        #cuda:0 allows you to run yolov5 on the GPU. Works only on nvidia cards.
        self.device = "cuda:0"
        self.model.to(self.device)
        print("Using Device: ", self.device)

    def detect(self,screen):
        actualTime=time()
        screen = [screen]
        results = self.model(screen)
        print(1//(time()-actualTime))
        return results.xyxyn[0][:, -1], results.xyxyn[0][:, :-1]

    def drawBoxes(self,results,frame):
        labels, cord = results
        n = len(labels)
        x_shape, y_shape = frame.shape[1], frame.shape[0]
        for i in range(n):
            row = cord[i]
            if row[4] >= 0.55:
                if (labels[i]==0):
                    bgr = (51, 0, 102)
                    union = 'gangB'
                elif (labels[i]==1):
                    bgr = (0,255,255)
                    union = 'gangV'
                elif (labels[i]==2):
                    bgr = (0,255,0)
                    union = 'cop'
                else:
                    bgr = (0,0,255)
                    union = 'corpse'
                x1, y1, x2, y2 = int(row[0] * x_shape), int(row[1] * y_shape), int(row[2] * x_shape), int(row[3] * y_shape)
                cv2.rectangle(frame, (x1, y1), (x2, y2), bgr, 2)
                cv2.putText(frame, union+" ("+str(int((float(str(row[4])[7:14])*100)))+"%)", (x1, y1), cv2.FONT_HERSHEY_SIMPLEX, 0.9, bgr, 2)

        return frame
