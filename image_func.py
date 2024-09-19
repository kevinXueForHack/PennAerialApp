
import cv2
import numpy as np
import matplotlib.pyplot as plt

#basic image processing. I was going to using a Canny formula but I found a one that seems to work better by thresholding

def process_image(img, alpha=0.5, beta=0.6):
    img1 = img
    img1 = cv2.medianBlur(img1, 5)
    # threshold
    thresh = cv2.threshold(img1, 180, 255, cv2.THRESH_BINARY)[1]
    # morphology edgeout = dilated_mask - mask
    # morphology dilate
    kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (5,5))
    dilate = cv2.morphologyEx(thresh, cv2.MORPH_DILATE, kernel)
    # get absolute difference between dilate and thresh
    diff = cv2.absdiff(dilate, thresh)
    # invert
    edges = 255 - diff
    edges = cv2.resize(edges, (img.shape[1], img.shape[0]))
    img = cv2.resize(img, (img.shape[1], img.shape[0]))
    result = cv2.addWeighted(img, alpha, edges, beta, 0)
    return result


#We find the center of images by processing the image and then creating contours, before getting the center of each contours
def contours_center(img, edge_low=400, edge_high=500):
    
    # Apply Gaussian blur to reduce noise
    blurred = cv2.GaussianBlur(img, (3, 3), 0)
    
    # Adaptive thresholding for better edge detection
    edges = cv2.Canny(blurred, edge_low, edge_high)
    
    # Apply morphological operations to close gaps in edges so we have cleaner linews
    kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (3, 3))
    morphed = cv2.morphologyEx(edges, cv2.MORPH_CLOSE, kernel)
    
    # Find contours in the processed image
    contours, hierarchy = cv2.findContours(morphed, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    
    # Filter contours based on area and shape
    min_area = 100  # Adjust this value to be more or less selective, but it doesn't really work
    filtered_contours = [c for c in contours if cv2.contourArea(c) > min_area]
    for c in filtered_contours:
        # Calculate moments for each contour
        M = cv2.moments(c)
        # Calculate x,y coordinate of center
        if M["m00"] != 0:
            cX = int(M["m10"] / M["m00"])
            cY = int(M["m01"] / M["m00"])
            cv2.circle(img, (cX, cY), 5, (0, 0, 0), -1)
            cv2.putText(img, "centroid", (cX - 25, cY - 25), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 0), 2)

    
    return img

