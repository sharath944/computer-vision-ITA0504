import cv2
import numpy as np
import matplotlib.pyplot as plt

def analyze_histogram(image_path):
    # Read the image
    image = cv2.imread(image_path)
    
    if image is None:
        print("Error: Image not found. Check the path.")
        return
    
    # Color channels
    color_channels = ('b', 'g', 'r')
    
    # Plot figure
    plt.figure(figsize=(10, 5))
    
    # Calculate and plot histogram for each channel
    for i, color in enumerate(color_channels):
        histogram = cv2.calcHist([image], [i], None, [256], [0, 256])
        plt.plot(histogram, color=color, label=f"{color.upper()} Channel")
        plt.xlim([0, 256])  # Pixel intensity range
    
    # Labels and title
    plt.title("Color Histogram Analysis")
    plt.xlabel("Pixel Intensity")
    plt.ylabel("Frequency")
    plt.legend()
    plt.show()

# ✅ Call the function with image path
analyze_histogram(r"C:\Users\Amar\OneDrive\Desktop\PRACTICE.jpg")
