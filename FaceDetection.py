import cv2;

image = cv2.imread("C:\Users\Paul\Downloads\z.png")

facecascadePath = "C:\\Users\\Paul\\Downloads\\OpenCv\\opencv\\build\\share\\OpenCV\\haarcascades\haarcascade_frontalface_default.xml"

faceCascade = cv2.CascadeClassifier(facecascadePath)


gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

faces = faceCascade.detectMultiScale(
    gray,
    scaleFactor=1.1,
    minNeighbors=5,
    minSize=(30, 30),
    flags=cv2.cv.CV_HAAR_SCALE_IMAGE
)
for (x, y, w, h) in faces:
     cv2.imshow(str(x),image[y:y+h,x:x+w])

for (x, y, w, h) in faces:
     cv2.ellipse(image, (x+w/2, y+h/2), (w/2, h/2),0,360,0, (0, 255, 0), 2)
         

# Display the resulting frame
cv2.imshow('Video', image)


while cv2.waitKey(1) & 0xFF != ord('q'):
    pass
cv2.destroyAllWindows()
        