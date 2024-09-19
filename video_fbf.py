import cv2
import numpy as np
import matplotlib.pyplot as plt
import image_func as f 

def videofilter (video_path, output_place):
    # Open the video file
    cap = cv2.VideoCapture(video_path)

    # Check if the video opened successfully
    if not cap.isOpened():
        print("Error opening video file")
        exit()
        
    count = 0
    while True:
        # Read a frame from the video
        ret, frame = cap.read()
        
        # If frame is read correctly ret is True
        if not ret:
            print("Can't receive frame (stream end?). Exiting ...")
            break
        
        # Process the frame for edges
        processed_frame = f.process_image(frame)
        # Find and mark contours and centers
        final_frame = f.contours_center(processed_frame)
        # Display the result
        cv2.imshow('Processed Video with Contours', final_frame)
        #Save frames
        cv2.imwrite(f"{output_place}_frame + {count:04d}.jpg", final_frame)
        count += 1
        # Break the loop if 'q' is pressed
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    # Release the video capture object and close windows
    cap.release()
    cv2.destroyAllWindows()
videofilter("testing_inputs/PennAir 2024 App Dynamic.mp4", 'basic_video_output/')    
videofilter("testing_inputs/PennAir 2024 App Dynamic Hard.mp4", 'advanced_video_output/')
