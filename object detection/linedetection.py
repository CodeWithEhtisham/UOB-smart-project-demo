import os
import math
import time
import numpy as np
import cv2
from datetime import datetime , timedelta
import imutils
import argparse

ap = argparse.ArgumentParser()
ap.add_argument("-f", "--frame", required=True,
	help="path to input frame")
ap.add_argument("-y", "--yolo", required=True,
 	help="base path to YOLO directory")
ap.add_argument("-c", "--confidence", type=float, default=0.4,
 	help="minimum probability to filter weak detections")
ap.add_argument("-t", "--threshold", type=float, default=0.3,
	help="threshold when applying non-maxima suppression")
args = vars(ap.parse_args())



def drawLine(event, x, y, flags, param):
	# Mouse event handlers for drawing lines
	global x1, y1, drawing, detectionLines
	if event == cv2.EVENT_LBUTTONDOWN:
		if not drawing:  # Start drawing a line
			x1, y1 = x, y
			drawing = True
		else:  # Stop drawing a line
			x2, y2 = x, y
			detectionLines.append([x1, y1, x2, y2])
			drawing = False
	elif event == cv2.EVENT_RBUTTONDOWN:
		# Delete right clicked line
		for i in detectionLines:
			p1 = np.array([i[0], i[1]])
			p2 = np.array([i[2], i[3]])
			p3 = np.array([x, y])
			if i[0] < i[2]:
				largerX = i[2]
				smallerX = i[0]
			else:
				largerX = i[0]
				smallerX = i[2]
			if abs(np.cross(p2 - p1, p3 - p1) / np.linalg.norm(p2 - p1)) < 10 and smallerX - 10 < x < largerX + 10:
				detectionLines.remove(i)

labelsPath = os.sep.join([args['yolo'], 'obj.names'])
Labels = open(labelsPath).read().strip().split("\n")
# create dictionary of labels is used as a key and count is used as value
labelCount = {}
for label in Labels:
    labelCount[label] = 0
weightsPath = os.path.sep.join([args["yolo"], 'yolov4.weights'])
configPath = os.path.sep.join([args["yolo"], 'yolov4.cfg'])
print("loading YOLO from disk...")
np.random.seed(42)
COLORS = np.random.randint(0, 255, size=(len(Labels), 3),
	dtype="uint8")

net = cv2.dnn.readNetFromDarknet(configPath, weightsPath)
ln = net.getLayerNames()
ln = [ln[i[0] - 1] for i in net.getUnconnectedOutLayers()]

cam = cv2.VideoCapture(args["frame"])

try:
	prop = cv2.cv.CV_CAP_PROP_FRAME_COUNT if imutils.is_cv2() \
		else cv2.CAP_PROP_FRAME_COUNT
	total = int(cam.get(prop))
	print("{} total frames in video".format(total))
except:
	print("could not determine # of frames in video")
	print("no approx. completion time can be provided")
	total = -1

offset = 10
velocityoffset = 10
distancethres = 40
x1 = 0
y1 = 0
drawing = False
framecount = 0
vehiclecount = 0
lanesCount = [0, 0, 0, 0, 0, 0]
vehicleTypesCount = [0, 0, 0, 0]
detectionLines = []
previousCentersAndIDs = []
id = 0
detectedVehicleIDs = []
cache = []
vehicleVelocities = {}
while True:
	labelData = []
	centersAndIDs = []
	#image = cv2.imread(args["image"])
	ret, frame = cam.read()
	(H, W) = frame.shape[:2]
	if framecount == 0:
		cv2.namedWindow("Draw Lines")
		cv2.setMouseCallback("Draw Lines", drawLine)
		while 1:
			frame2 = frame.copy()
			if cv2.waitKey(1) & 0xFF == ord('q'):
				cv2.destroyAllWindows() 
				lanesCount = [0] * len(detectionLines)
				break
			for l in detectionLines:
				cv2.line(frame, (l[0],l[1]), (l[2],l[3]), (255,203,48),6)
			cv2.imshow("Draw Lines", frame2)

	for dl in detectionLines:
		cv2.line(frame, (dl[0], dl[1]), (dl[2], dl[3]), (255, 203, 48), 6)
	
	frame_size = frame
	frame_size = imutils.resize(frame, width=1080, height=720)
	grayA = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
	
	blob = cv2.dnn.blobFromImage(frame, 1 / 255.0, (416, 416),
		swapRB=True, crop=False)
	net.setInput(blob)
	start = time.time()
	layerOutputs = net.forward(ln)
	end = time.time()
	
	boxes = []
	confidences = []
	classIDs = []   

	for output in layerOutputs:
		# print('Outputs', output)
		for detection in output:
			# print('Detection', detection)
			scores = detection[5:]
			# print('Scrores', scores)
			classID = np.argmax(scores)
			confidence = scores[classID]
			# print('Confidence', confidence)
			if confidence > args["confidence"]:
				box = detection[0:4] * np.array([W, H, W, H])
				# print('BOX', box)
				(centerX, centerY, width, height) = box.astype("int")
				x = int(centerX - (width / 2))
				y = int(centerY - (height / 2))
				boxes.append([x, y, int(width), int(height)])
				confidences.append(float(confidence))
				classIDs.append(classID)
	
	unavailableIDs = []			
	idxs = cv2.dnn.NMSBoxes(boxes, confidences, args["confidence"], args["threshold"])
	
	count = []
	extraction = []          
	if len(idxs) > 0:
		for ind, i in enumerate(idxs.flatten()):
			(x, y) = (boxes[i][0], boxes[i][1])
			(w, h) = (boxes[i][2], boxes[i][3])
			center = (x * 2 + w) / 2, (y * 2 + h) / 2
			sameVehicleDetected = False
			alreadyCounted = False
			for indx,c in enumerate(cache):
				minDistance = distancethres * ((indx+2)/2)
				for cid in c:
					if cid[2] in unavailableIDs:
						continue
					distance = math.sqrt((center[0] - cid[0]) ** 2 + (center[1] - cid[1]) ** 2)
					if distance < minDistance:
						nearestBox = cid[2]
						minDistance = distance
						sameVehicleDetected = True
				if sameVehicleDetected:
					break

			if not sameVehicleDetected:
				centersAndIDs.append([center[0], center[1],id])
				id+=1
			else:
				centersAndIDs.append([center[0], center[1], nearestBox])
				unavailableIDs.append(nearestBox)
			
			if len(centersAndIDs) !=0:
				vehicleId = centersAndIDs[len(centersAndIDs) -1][2] 
			cv2.circle(frame, (int(center[0]), int(center[1])), 4, (41, 18, 252), 5)   # Plot center point

			for i, dl in enumerate(detectionLines):
				p1 = np.array([dl[0], dl[1]])
				p2 = np.array([dl[2], dl[3]])
				p3 = np.array([center[0], center[1]])
				if dl[0] < dl[2]:
					largerX = dl[2]
					smallerX = dl[0]
				else:
					largerX = dl[0]
					smallerX = dl[2]
				if dl[1] < dl[3]:
					largerY = dl[3]
					smallerY = dl[1]
				else:
					largerY = dl[1]
					smallerY = dl[3]
				
				if abs(np.cross(p2 - p1, p3 - p1) / np.linalg.norm(p2 - p1)) < offset and \
						smallerX - offset < center[0] < largerX + offset and \
						smallerY - offset < center[1] < largerY + offset:

						for dvi in detectedVehicleIDs:
							if dvi == vehicleId:
								cv2.line(frame, (dl[0], dl[1]), (dl[2], dl[3]), (90, 224, 63), 6)
								alreadyCounted = True
								break
						
						if not alreadyCounted:
							detectedVehicleIDs.append(vehicleId)
							vehiclecount += 1
                            # print("Vehicle Count: ", vehiclecount)
							cv2.line(frame, (dl[0], dl[1]), (dl[2], dl[3]), (90, 224, 63), 6)
                            # labelCount[i] += 1

							print("Vehicle Count: ", vehiclecount, "Lane: ", i)
							lanesCount[i] += 1
                            # print("Lanes Count: ", lanesCount)
                            	
				if abs(np.cross(p2 - p1, p3 - p1) / np.linalg.norm(p2 - p1)) < velocityoffset and \
						smallerX - velocityoffset < center[0] < largerX + velocityoffset and \
						smallerY - velocityoffset < center[1] < largerY + velocityoffset:
						foundInPreviousFrame = False
						pixelsOverFrames = []
						for s in range(len(cache) - 1):
							for c in range(len(cache[s])):
								if cache[s][c][2] == vehicleId:
									if not foundInPreviousFrame:
										pixelsOverFrames.append(math.sqrt((cache[s][c][0] - center[0]) ** 2 + (cache[s][c][1] - center[1]) ** 2) / (s + 1))
										foundInPreviousFrame = True
									cachehit = False
									for ss in range(s+1, len(cache)):
										for cc in range(len(cache[ss])):
											if cache[ss][cc][2] == vehicleId:
												pixelsOverFrames.append(math.sqrt((cache[s][c][0] - cache[ss][cc][0]) ** 2 + (cache[s][c][1] - cache[ss][cc][1]) ** 2)/ ss - s)
												cachehit = True
												break
										if cachehit:
											break
		
			color = [int(c) for c in COLORS[classIDs[i]]]
			cv2.rectangle(frame, (x, y), (x + w, y + h), color, 2)
			text = "{}: {:.4f}".format(Labels[classIDs[i]], confidences[i])
			cv2.putText(frame, text, (x, y - 5), cv2.FONT_HERSHEY_SIMPLEX,
				0.5, color, 2)
											
		for index, dl in enumerate(detectionLines): 
			cv2.putText(frame, "Crossed:" + str(lanesCount[index]), (int((dl[0] + dl[2]) / 2) + 10,
					int((dl[1] + dl[3]) / 2) - 10), cv2.FONT_HERSHEY_SIMPLEX, 1.3, (209, 21, 77), 2)
	
		
		cv2.imshow("Frame", frame)
		framecount +=1
		cacheSize = 5
		cache.insert(0, centersAndIDs.copy())
		if len(cache) > cacheSize:
			del cache[cacheSize]
									
		if cv2.waitKey(1) == 27 or framecount == len(labelData) - 2:
			break

cam.release()
cv2.destroyAllWindows()
