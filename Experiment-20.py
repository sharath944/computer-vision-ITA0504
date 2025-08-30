import cv2
import numpy as np

# Load the image
image = cv2.imread(r"C:\Users\Amar\OneDrive\Desktop\PRACTICE.jpg")

# Convert to grayscale
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Define a kernel (structuring element)
kernel = np.ones((5, 5), np.uint8)

# Apply dilation
dilated_image = cv2.dilate(gray, kernel, iterations=1)

# Display original and dilated images
cv2.imshow("Original Image", gray)
cv2.imshow("Dilated Image", dilated_image)

cv2.waitKey(0)
cv2.destroyAllWindows()
