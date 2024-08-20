import cv2
import numpy as np

# Initialize video capture
cap = cv2.VideoCapture(0)  # Change 0 to the appropriate video source if you have multiple cameras


# Function to track circles in the frame
def track_circles(frame, edges_smoothed = None):
    # Initialize variables for temporal smoothing
    alpha = 0.5  # Smoothing factor

    # Convert frame to grayscale
    gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Apply Gaussian blur
    blurred = cv2.GaussianBlur(gray_frame, (7, 7), 0)

    # Apply adaptive thresholding
    adaptive_thresh = cv2.adaptiveThreshold(blurred, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 11, 4)

    # Apply Canny edge detection
    edges = cv2.Canny(adaptive_thresh, 100, 200)  # You can adjust these thresholds as needed

    # Apply temporal smoothing
    if edges_smoothed is None:
        edges_smoothed = edges
    else:
        cv2.addWeighted(edges, alpha, edges_smoothed, 1 - alpha, 0, edges_smoothed)

    # Display the result
    cv2.imshow('Canny Edge Detection', edges_smoothed)

    # Apply morphological operations to close gaps in between edge contours
    kernel = np.ones((5, 5), np.uint8)
    closed_edges = cv2.morphologyEx(edges_smoothed, cv2.MORPH_CLOSE, kernel)

    # Detect circles using Hough Circle Transform with adaptive thresholding
    circles = cv2.HoughCircles(closed_edges, cv2.HOUGH_GRADIENT, dp=1, minDist=50, param1=50, param2=30, minRadius=5, maxRadius=100)

    if circles is not None:
        # Convert the (x, y) coordinates and radius of the circles to integers
        circles = np.round(circles[0, :]).astype("int")

        # Loop over all detected circles and draw them on the frame
        for (x, y, r) in circles:
            # Draw the circle
            cv2.circle(frame, (x, y), r, (0, 255, 0), 4)

            # Draw a red contour around the circle
            cv2.circle(frame, (x, y), r, (0, 0, 255), 2)

    cv2.imshow('Grayscale', gray_frame)
    cv2.imshow('Canny Edge Detection', edges)
    return frame


while True:
    # Read a frame from the video stream
    ret, frame = cap.read()
    if not ret:
        break

    circles = track_circles(frame)
    # Display the result
    cv2.imshow('Original', frame)

    # Check for 'q' key press to exit the loop
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the video capture object and close the OpenCV windows
cap.release()
cv2.destroyAllWindows()