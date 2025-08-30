import cv2
import os
image = cv2.imread(r"C:\Users\Amar\OneDrive\Desktop\PRACTICE.jpg")

# Check if image loaded successfully
if image is None:
    print(f"Error: Could not load image at {os.path.abspath(image_path)}")
else:
    # Convert to grayscale
    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Apply Canny edge detection
    edges = cv2.Canny(gray_image, 100, 200)

    # Show results
    cv2.imshow("Original Image", image)
    cv2.imshow("Edge Detected Image", edges)

    cv2.waitKey(0)
    cv2.destroyAllWindows()
print(image)
