import cv2
import pytesseract

# Set tesseract executable path
pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

def extract_text_from_video(video_path):
    cap = cv2.VideoCapture(video_path)
    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            break
        gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        text = pytesseract.image_to_string(gray_frame)
        print(text)
    cap.release()
    cv2.destroyAllWindows()

extract_text_from_video(r"C:\Users\Amar\OneDrive\Desktop\hi.mp4")
