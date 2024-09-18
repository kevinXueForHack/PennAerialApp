
import cv2
import numpy as np
import matplotlib.pyplot as plt

def process_image(img, edge_low=200, edge_high=500, alpha=1, beta=0.8):
    # Apply Canny edge detection
    blurred = cv2.GaussianBlur(img, (5, 5), 0)
    # Apply Canny edge detection
    edges = cv2.Canny(blurred, edge_low, edge_high)
    # Convert edges to 3-channel image
    edges_color = cv2.cvtColor(edges, cv2.COLOR_GRAY2BGR)
    # Combine original image with edges
    result = cv2.addWeighted(img, alpha, edges_color, beta, 0)
    return result

def countours_center(img, edge_low=200, edge_high=500):
    gray_image = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    # Apply Gaussian blur to reduce noise
    blurred = cv2.GaussianBlur(gray_image, (5, 5), 0)
    # Adaptive thresholding for better edge detection
    edges = cv2.Canny(blurred, edge_low, edge_high)
    # Apply morphological operations to close gaps in edges
    kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (3, 3))
    morphed = cv2.morphologyEx(edges, cv2.MORPH_CLOSE, kernel)

    # Find contours in the processed image
    contours, hierarchy = cv2.findContours(morphed, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    
    # Filter contours based on area and shape
    min_area = 50  # Adjust this value to be more or less selective
    filtered_contours = [c for c in contours if cv2.contourArea(c) > min_area]
    
    for c in filtered_contours:
        # Calculate moments for each contour
        M = cv2.moments(c)
        # Calculate x,y coordinate of center
        if M["m00"] != 0:
            cX = int(M["m10"] / M["m00"])
            cY = int(M["m01"] / M["m00"])
            cv2.circle(img, (cX, cY), 5, (255, 255, 255), -1)
            cv2.putText(img, "centroid", (cX - 25, cY - 25), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 2)

    
    return img

