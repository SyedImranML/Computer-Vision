# importing libraries
import cv2
import numpy as np

# Create a VideoCapture object and read from input file
cap = cv2.VideoCapture('1.mp4')

# Check if camera opened successfully
if (cap.isOpened()== False):
       print("Error opening video file")

# Read until video is completed
while(cap.isOpened()):
       # Capture frame-by-frame
       ret, frame = cap.read()
       if ret == True:
              # Display the resulting frame
              frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
              cv2.imshow('Frame', frame)
              # Press Q on keyboard to exit
              if cv2.waitKey(1) & 0xFF == ord('q'):
                     break
       else:
              break

cap.release()
cv2.destroyAllWindows()
