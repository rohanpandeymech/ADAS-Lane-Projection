import cv2

def perform_canny(frame):
    # To Convert frame to grayscale
    gray = cv2.cvtColor(frame, cv2.COLOR_RGB2GRAY)
    cv2.imshow("Grayscale",gray)
    # Applies a 5x5 gaussian blur with deviation of 0 to frame - not mandatory since Canny will do this for us
    blur = cv2.GaussianBlur(gray, (5, 5), 0)
    cv2.imshow("GaussianBlur",blur)
    # Applies Canny edge detector with minVal of 50 and maxVal of 150
    canny = cv2.Canny(blur, 50, 150)
    return canny 
cap = cv2.imread("Temple_khajurao.jpg")
cv2.imshow("InputFrame",cap)
canny=perform_canny(cap)
cv2.imshow("Canny",canny)
cv2.waitKey(0)
cap.release()