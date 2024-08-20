import cv2
import numpy as np
import os

current_dir = os.getcwd()

# Load the HED model
hed_model = cv2.dnn.readNetFromCaffe("deploy.prototxt", "hed_pretrained_bsds.caffemodel")

# Function to perform edge detection
def detect_edges(frame):
    # Resize the frame to 500x500 (the input size required by the HED model)
    frame_resized = cv2.resize(frame, (500, 500))
    # Convert the frame to grayscale
    gray = cv2.cvtColor(frame_resized, cv2.COLOR_BGR2GRAY)
    # Normalize the grayscale image
    blob = cv2.dnn.blobFromImage(gray, scalefactor=1.0, size=(500, 500), mean=(104.00698793, 116.66876762, 122.67891434), swapRB=False, crop=False)
    # Set the input to the HED model
    hed_model.setInput(blob)
    # Perform forward pass and get the output
    hed_output = hed_model.forward()
    # Get the binary edge map (thresholding)
    _, edge_map = cv2.threshold(hed_output[0, 0], 50, 255, cv2.THRESH_BINARY)
    # Convert the edge map back to 3 channels
    edge_map = cv2.merge([edge_map, edge_map, edge_map])
    # Resize the edge map to the original frame size
    edge_map = cv2.resize(edge_map, (frame.shape[1], frame.shape[0]))
    # Combine the original frame and the edge map
    result = np.hstack((frame, edge_map))
    return result

# Capture video from the camera
cap = cv2.VideoCapture(0)

while True:
    # Read a frame from the camera feed
    ret, frame = cap.read()
    if not ret:
        break

    # Detect edges
    result = detect_edges(frame)

    # Display the result
    cv2.imshow("Holistically-Nested Edge Detection", result)

    # Break the loop if 'q' is pressed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the camera and close all OpenCV windows
cap.release()
cv2.destroyAllWindows()

