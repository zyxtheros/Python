import cv2


def preprocess_frame(frame):
    # Convert frame to grayscale
    gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    return gray_frame


def main():
    # Open video capture device (webcam)
    cap = cv2.VideoCapture(0)

    while True:
        # Read a frame from the video stream
        ret, frame = cap.read()

        if not ret:
            print("Failed to capture frame")
            break

        # Apply preprocessing to the frame
        gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        # gaussian_frame = cv2.GaussianBlur(gray_frame, (5, 5), 0)
        sharpened_frame = cv2.addWeighted(gray_frame, 1.5, gray_frame, -0.5, 0)

        # Display the original and processed frames
        cv2.imshow('Original', frame)
        cv2.imshow('Grayscale', gray_frame)
        # cv2.imshow('Gaussian', gaussian_frame)
        cv2.imshow('Sharpened', sharpened_frame)


        # Check for key press to exit the loop
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    # Release the video capture object and close windows
    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()