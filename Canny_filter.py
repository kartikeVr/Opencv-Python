import cv2 as cv
cam = cv.VideoCapture(0)

while 1:
    ok, img = cam.read()

    can = cv.Canny(img, 50, 150)
    cv.imshow("Canny",can)

    if cv.waitKey(1) & 0xFF ==ord('q'):
        break

cam.release()
cv.destroyAllWindows()
