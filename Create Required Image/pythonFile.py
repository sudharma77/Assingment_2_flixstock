import cv2
logo = cv2.imread("input.png")
img = cv2.imread("backGround.jpg")
rows ,cols ,channels = logo.shape
roi = img[0:rows, 0:cols]
m = cv2.imread("mask.png")
logoGray = cv2.cvtColor(m,cv2.COLOR_BGR2GRAY)
ret ,mask = cv2.threshold(logoGray,220,255,cv2.THRESH_BINARY)

inverseMask = cv2.bitwise_not(mask)

background = cv2.bitwise_and(roi,roi, mask = inverseMask)
frontImage = cv2.bitwise_and(logo,logo, mask = mask)
result = cv2.add(background,frontImage)
img[0:rows, 0:cols] = result
cv2.imwrite("outImgPy.png", result)
cv2.imshow("result",result)
# cv2.imshow("final",img)
# cv2.imshow('gray',logoGray)
# cv2.imshow('mask',mask)
# cv2.imshow('inverse',inverseMask)

cv2.waitKey(0)
cv2.destroyAllWindows()