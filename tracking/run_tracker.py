import cv2
from Detector import detect
from KalmanFilter import KalmanFilter

cap = cv2.VideoCapture('example.mp4')

KF = KalmanFilter(0.1, 1, 1, 1, 0.1, 0.1)

while(True):

    ret, frame = cap.read()
    frame = cv2.resize(frame, (960, 540))  

    centers, mask = detect(frame)

    if (len(centers) > 0):

        # draw circle on detected object
        cv2.circle(frame, (int(centers[0][0]), int(centers[0][1])), 10, (0, 255, 0), 2)

        (x, y) = KF.predict()

        # draw rectangle as the predicted object position
        cv2.rectangle(frame, (int(x) - 15, int(y) - 15), (int(x) + 15, int(y) + 15), (255, 0, 0), 2)

        # update
        (x1, y1) = KF.update(centers[0])

        # draw rectangle as the estimated object position
        cv2.rectangle(frame, (int(x1) - 15, int(y1) - 15), (int(x1) + 15, int(y1) + 15), (0, 0, 255), 2)

        cv2.putText(frame, "Measured Position", (int(centers[0][0]) + 15, int(centers[0][1]) - 15), 0, 0.5, (0,255,0), 2)
        cv2.putText(frame, "Predicted Position", (int(x) + 15, int(y)), 0, 0.5, (255, 0, 0), 2)
        cv2.putText(frame, "Estimated Position", (int(x1) + 15, int(y1) + 15), 0, 0.5, (0, 0, 255), 2)
      
    cv2.imshow("Frame", frame)
    cv2.imshow("Mask", mask)

    key = cv2.waitKey(50)
    if key == 27:
        break

cap.release()
cv2.destroyAllWindows()
