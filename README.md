# PennAerialApp
Videos are in .mkv format because of OBS weirdness, sorry about that.

My Penn Aerial technical for software section.
There are 3 functions:

image_func -> two individual functions, one that marks and one that countours to find the center
individual picture -> this is the main I use to process and test single images
video fbf -> this is the main I use to process and test videos

Within image_func, I have two functions

    process_image -> this runs a filter I found on stackoverflow to get the edges and overlay them onto a transparent version of the original image

    contours_center -> this runs a cammy filter along with some other basic processing before getting the center of every contour and displaying them.

individual_picture is just set as a few lines of code, since it wasn't reusable. If I was optimizing and making this software for future use, I would turn it into a function so I can direct different input and output images

video_fbf is the code that runs the frame_by_frame video detection of the opencv. I set it up as a function so I can run and direct output to two different folders at the same time. 

Code flaws:
    My image_func file is flawed, and thus it has an issue getting edges of one of the 5 objects at any given point. It additionally finds some small distortion edges as well, but at least those aren't getting detected by the centering/contour function. Additionally, for objects that fade or have two different colors, the edge detection breaks down.

    My contours_center struggles with detecting centers in similar situations to image_func, and it struggles to find centers of different-color images.

Stuff I wish I had done:

    Realistically, if I found a way to convert my image_func to a more generic function that just outputs the edges instead of overlaying them, I could refactor contours_center to be easier and more understandable. Unfortunately, the Cammy edge detection and the edge detection used in image_func output completely different data types.

    Fixing the flaws in my algorithms would realistically probably just require a better understanding of OpenCV so I don't run into flaws with contour center.







