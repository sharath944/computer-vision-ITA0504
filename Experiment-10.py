import cv2

# Load the image
image = cv2.imread(r"C:\Users\Amar\OneDrive\Desktop\PRACTICE.jpg")

# Rotate 90 degrees clockwise
rotated_img = cv2.rotate(image, cv2.ROTATE_90_CLOCKWISE)

# Display the rotated image
cv2.imshow("Rotated Image", rotated_img)
cv2.waitKey(0)
cv2.destroyAllWindows()
