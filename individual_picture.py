import cv2
import numpy as np
import matplotlib.pyplot as plt
import image_func as f 


#video stuff

cap = cv2.VideoCapture('path to video file')
count = 0
while cap.isOpened():
    ret,frame = cap.read()
    cv2.imshow('window-name', frame)
    cv2.imwrite("frame%d.jpg" % count, frame)
    count = count + 1
    if cv2.waitKey(10) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()


# Specify the image path
image = "testing_inputs/PennAir 2024 App Static.png"
# Read image
img = cv2.imread(image)
if img is None:
    raise ValueError(f"Could not read the image: {img}")
# Process the image
processed_image = f.process_image(img)
# Find and mark contours
final_image = f.contours_center(processed_image)
# Display the result
cv2.imshow('Processed Image with Contours', processed_image)
cv2.waitKey(0)
cv2.destroyAllWindows()
# Save the output image
cv2.imwrite("picture_output/output_image_with_contours.jpg", final_image)

