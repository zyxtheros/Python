import cv2
import numpy as np


def preprocess_frame(frame):
    # Convert frame to grayscale
    gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    return gray_frame


def ceiling(a, b):
    return -(a // -b)


def create_blank_image(width, height, channels=3):
    # Create a blank image with zeros
    blank_image = np.zeros((height, width, channels), dtype=np.uint8)
    # Fill the image with white color (255)
    blank_image.fill(255)
    return blank_image

def gallery(array, ncols=3):
    # print(f"array size: {array.size}")
    nindex = len(array)
    width, height, intensity = array[0].shape
    nrows = ceiling(nindex, ncols)

    # fill with blanks
    if nindex < nrows * ncols:
        print(f"filling with elements of size {height}x{width}")
        while nindex < nrows*ncols:
            # print(f'array size before append: {array.size}')
            nindex += 1
            img_blank = np.zeros((width, height, 3), dtype=np.uint8)
            img_blank.fill(255)
            print(f"blank size: {img_blank.shape}, list element size: {array[0].shape}")
            # _, new_frame = cv2.VideoCapture(0).read()
            array.append(img_blank)
            print(f"length of list: {len(array)}")
            # print(f'array size after append: {array.size}')

    assert nindex == nrows*ncols, f'Expected {nrows*ncols} elements but {nindex} were created (nrows={nrows} ncols={ncols})'
    # print(f"nindex from array: {array.shape[0]}")
    #assert nindex == array.size/(width*height*intensity), f"elements now: {array.size/(width*height*intensity)}, element wanted: {nindex}"

    array = np.array(array)
    # want result.shape = (height*nrows, width*ncols, intensity)
    result = (array.reshape(nrows, ncols, height, width, intensity)
              .swapaxes(1, 2)
              .reshape(height*nrows, width*ncols, intensity))
    return result


def main():
    # Open video capture device (webcam)
    cap = cv2.VideoCapture(0)

    while True:
        # Read a frame from the video stream
        ret, frame = cap.read()

        # Initialize an empty numpy array
        array = []

        if not ret:
            print("Failed to capture frame")
            break

        # Apply preprocessing to the frame
        gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY) # Convert frame to grayscale
        blurred_frame = cv2.GaussianBlur(gray_frame, (5, 5), 0) # Apply Gaussian blur
        adaptive_frame = cv2.adaptiveThreshold(blurred_frame, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 11, 4) # Apply adaptive thresholding

        # array = np.array([cv2.cvtColor(gray_frame, cv2.COLOR_GRAY2RGB), cv2.cvtColor(blurred_frame, cv2.COLOR_GRAY2RGB), cv2.cvtColor(adaptive_frame, cv2.COLOR_GRAY2RGB)])
        array.append(cv2.cvtColor(gray_frame, cv2.COLOR_GRAY2RGB))
        array.append(cv2.cvtColor(blurred_frame, cv2.COLOR_GRAY2RGB))
        array.append(cv2.cvtColor(adaptive_frame, cv2.COLOR_GRAY2RGB))
        # TODO: convert list back to array to fix banding issue
        output = gallery(array, 2)
        cv2.imshow('Edge Detection', output)
        # Display the original and processed frames
        # cv2.imshow('Original', frame)
        # cv2.imshow('Grayscale', gray_frame)
        # cv2.imshow('Gaussian', blurred_frame)
        # cv2.imshow('Adaptive Thresholding', adaptive_frame)

        # Check for key press to exit the loop
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    # Release the video capture object and close windows
    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()