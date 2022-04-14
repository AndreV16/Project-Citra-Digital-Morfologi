import cv2
imgrgb = cv2.imread("mawar.jpg")
imggray = cv2.imread("mawar.jpg",0)

cv2.imshow("gambar rgb",imgrgb)
cv2.imshow("gambar gray",imggray)
cv2.waitKey()
