import cv2
import os

DATA_DIR = './data'

dataset_size = 100
folder_name = "26"
cap = cv2.VideoCapture(0)


if not os.path.exists(os.path.join(DATA_DIR, folder_name)):
    os.makedirs(os.path.join(DATA_DIR, folder_name))
print(folder_name)

done = False
while True:
    ret, frame = cap.read()
    cv2.putText(frame, 'Ready? Press "Q" ! :)', (100, 50), cv2.FONT_HERSHEY_SIMPLEX, 1.3, (0, 255, 0), 3, cv2.LINE_AA)
    cv2.imshow('frame', frame)
    if cv2.waitKey(25) == ord('q'):
        break
counter = 0
while counter < dataset_size:
    ret, frame = cap.read()
    cv2.imshow('frame', frame)
    cv2.waitKey(25)
    cv2.imwrite(os.path.join(DATA_DIR, folder_name, '{}.jpg'.format(counter)), frame)

    counter += 1

cap.release()
cv2.destroyAllWindows()