import cv2
def get_person():
    # 준비
    face_cascade = cv2.CascadeClassifier(
        './data/haarcascades/haarcascade_frontalface_default.xml')

    image = cv2.imread('C:\\Users\\user\\Desktop\\test_img.jpg')
    grayImage = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)


    faces = face_cascade.detectMultiScale(grayImage, 1.03, 5)

    print(faces.shape)
    print("Number of faces detected: " + str(faces.shape[0]))

if __name__ == "__main__":
    get_person()