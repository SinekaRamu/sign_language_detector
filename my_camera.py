import cv2
cap = cv2.VideoCapture(0)
if cap.isOpened():
    print("Camera is working! Press 'q' to quit.")
    while True:
        ret, frame = cap.read()
        cv2.imshow('Test', frame)
        if cv2.waitKey(1) == ord('q'):
            break
else:
    print("ERROR: Camera not detected.")
cap.release()
cv2.destroyAllWindows()