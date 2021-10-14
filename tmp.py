import cv2
import numpy as np 

img = cv2.imread('./day_traffic2.png')
res = cv2.resize(img, (700, 500))
res2 = res.copy()

# roi 지정 
w = 500; h = 350

img_gray = cv2.cvtColor(res, cv2.COLOR_BGR2GRAY)
roi = img_gray[0:h, 0:w]
# cv2.imshow('img_gray', img_gray)   # 흑백 
# cv2.imshow('roi', roi)
ret, th = cv2.threshold(roi, 127, 255, cv2.THRESH_BINARY_INV)
# cv2.imshow('th', th)
k = cv2.getStructuringElement(cv2.MORPH_RECT, (3, 3))   # 모폴로지 연산 필터 
# erosion = cv2.erode(th, k) 
# cv2.imshow('erosion', erosion)
dst = cv2.morphologyEx(th, cv2.MORPH_OPEN, k)   # 모폴로지 닫기 연산 
cv2.imshow('dst', dst)

# BLOB 필터 생성하기 
params = cv2.SimpleBlobDetector_Params()

# 경계 값 조정
params.minThreshold = 10
params.maxThreshold = 240
params.thresholdStep = 5
params.filterByArea = True
params.maxArea = 300
params.minArea = 250
params.filterByColor = False
# params.blobColor = 255

params.filterByConvexity = False 
params.filterByInertia = False 
params.filterByCircularity = False 

detector = cv2.SimpleBlobDetector_create(params)
keypoints = detector.detect(dst)
img_draw = cv2.drawKeypoints(dst, keypoints, None, None, cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)
# cv2.imshow('keypoints', keypoints)
cv2.imshow('img_draw', img_draw)

xy_p = []
for keypoint in keypoints:
    cx, cy = keypoint.pt 
    size = keypoint.size
    print(cx, cy, size)

cv2.waitKey()
cv2.destroyAllWindows()