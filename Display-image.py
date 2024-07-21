import cv2

# Load an image
image = cv2.imread('sample1.jpg')

# Display the result
cv2.imshow('Edges', image)
cv2.waitKey(0)
cv2.destroyAllWindows()
