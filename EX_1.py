#Day 1 Read,Display,and Save an image 

# Importing the OpenCV library
import cv2
# Reading the image using imread() function
image = cv2.imread('image.jpg')

# Extract the height and width of an image
h, w = image.shape[:2]
# Displaying the height and width
print("Height = {}, Width = {}".format(h, w))


#To Display image
# Window name in which image is displayed
window_name = 'image'

# Using cv2.imshow() method
# Displaying the image
cv2.imshow(window_name, image)

#waits for user to press any key
#(this is necessary to avoid Python kernel form crashing)
cv2.waitKey(0)

#closing all open windows
cv2.destroyAllWindows()

#resizing an image
# resize() function takes 2 parameters,
# the image and the dimensions
imr = cv2.resize(image, (80, 80))


# Using cv2.imwrite() method
# Saving the image
filename="test.jpg"
cv2.imwrite(filename, imr)


