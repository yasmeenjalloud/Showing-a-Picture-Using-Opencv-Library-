import cv2 as cv 
img = cv.imread("download.jpeg", 1)
cv.imshow("download", img)
size_image = cv.resize(img, (800,600))
cv.imshow("download", size_image)
cv.waitKey() 
key = cv.waitKey(1) 
while cv.waitkey():
    if key == ord('q') or key== ord('Q'):
        break; 
img.release()
cv.destroyAllWindows()