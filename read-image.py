import cv2
import pytesseract


# get grayscale image
def get_grayscale(image):
    return cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)


base = cv2.imread("test.jpg", 0)
image = get_grayscale(base)
thresh = 255 - cv2.threshold(image, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)[1]

x, y, w, h = 37, 625, 309, 28
ROI = thresh[y : y + h, x : x + w]
data = pytesseract.image_to_string(ROI, lang="eng", config="--psm 6")
print(data)

cv2.imshow("thresh", thresh)
cv2.imshow("ROI", ROI)
cv2.waitKey()
