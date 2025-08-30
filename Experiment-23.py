import cv2
import numpy as np

# Load the image
image = cv2.imread(r"C:\Users\Amar\OneDrive\Desktop\PRACTICE.jpg")

# Convert to grayscale
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Define kernel
kernel = np.ones((5, 5), np.uint8)

# Apply Top Hat
tophat_image = cv2.morphologyEx(gray, cv2.MORPH_TOPHAT, kernel)

# Display results
cv2.imshow("Original Image", image)
cv2.imshow("Top Hat Image", tophat_image)
cv2.waitKey(0)
cv2.destroyAllWindows()
