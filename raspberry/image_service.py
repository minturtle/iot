
import cv2


def get_person_count(path):
    face_cascade = cv2.CascadeClassifier(
        './data/haarcascades/haarcascade_frontalface_default.xml')
    image = cv2.imread(path)
    grayImage = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    faces = face_cascade.detectMultiScale(grayImage, 1.03, 5)
    return faces.shape[0]

if __name__ == "__main__":
    get_person_count()