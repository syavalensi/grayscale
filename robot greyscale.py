import cv2

# Load an color image 
img = cv2.imread('robot.jpg')
cv2.imshow('image',img)
gray_image = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
cv2.imshow('image',gray_image)
cv2.waitKey(0)
cv2.destroyAllWindows()

