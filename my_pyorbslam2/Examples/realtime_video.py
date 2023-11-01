import cv2

# Open the camera
cap = cv2.VideoCapture(0)  # 0 represents the default camera, change it if necessary

while True:
    ret, frame = cap.read()

    if not ret:
        break

    # Perform image processing on 'frame' here
    # For ORB-SLAM, you may need to convert the frame to grayscale

    cv2.imshow('Camera Feed', frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()