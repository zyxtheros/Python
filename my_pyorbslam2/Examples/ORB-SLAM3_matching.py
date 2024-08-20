import cv2
from matplotlib import pyplot as plt

from python_orb_slam3 import ORBExtractor
# source and target are seperate frmaes that can be used for matching
source = cv2.imread("images/sample1.jpg", cv2.IMREAD_GRAYSCALE)
target = cv2.imread("images/sample1.jpg", cv2.IMREAD_GRAYSCALE)

orb_extractor = ORBExtractor()

source_keypoints, source_descriptors = orb_extractor.detectAndCompute(source)
target_keypoints, target_descriptors = orb_extractor.detectAndCompute(target)

# Match Features
bf = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=True)
matches = bf.match(source_descriptors, target_descriptors)

# Draw matches
source_image = cv2.drawKeypoints(source, source_keypoints, None)
target_image = cv2.drawKeypoints(target, target_keypoints, None)
matches_image = cv2.drawMatches(source_image, source_keypoints, target_image, target_keypoints, matches, None)

# Show images
plt.imshow(matches_image)
plt.show()