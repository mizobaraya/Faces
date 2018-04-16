import dlib
from skimage.io import imread
from imutils import face_utils as face
import cv2 as cv
detector = dlib.get_frontal_face_detector()
pose_detect = dlib.shape_predictor("shape_predictor_68_face_landmarks.dat")
cap = cv.VideoCapture(0)
while True:
    ret, img = cap.read()
    faces = detector(img, 1)
    for face in faces:
        x, y, w, h = face.rect_to_bb(face)
        cv.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2)
        cv.imshow("Frame", img)
        if cv.waitKey(1) & 0xFF == ord('q'):
            break