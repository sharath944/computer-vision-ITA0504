import cv2
import numpy as np

# Load the image
image = cv2.imread(r"C:\Users\Amar\OneDrive\Desktop\PRACTICE.jpg")

# Convert to grayscale (optional but common for morphological operations)
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Define a kernel (structuring element)
kernel = np.ones((5, 5), np.uint8)  # 5x5 square kernel

# Apply erosion
eroded_image = cv2.erode(gray, kernel, iterations=1)

# Display original and eroded images
cv2.imshow("Original Image", gray)
cv2.imshow("Eroded Image", eroded_image)

cv2.waitKey(0)
cv2.destroyAllWindows()
