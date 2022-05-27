# Importing the OpenCV library
import cv2

# Reading the image using imread() function
image = cv2.imread('image.jpg')

# Displaying the image

window_name="Displaying Image"

cv2.imshow(window_name, image)


img = cv2.imread("image.jpg", cv2.IMREAD_COLOR)
cv2.imshow(window_name, img)


#img = cv2.imread("image.jpg", cv2.IMREAD_GRAYSCALE)
#cv2.imshow(window_name, img)

#img = cv2.imread("image.jpg", cv2.IMREAD_UNCHANGED)
#cv2.imshow(window_name, img)


#img = cv2.imread("image.jpg", 0)
#cv2.imshow(window_name, img)


#waits for user to press any key
#this is necessary to avoid Python kernel form crashing

img= cv2.imwrite("sample.jpg",img)
cv2.waitKey(0)

#closing all open windows
cv2.destroyAllWindows()
