''' 지정 좌표에 따라 이미지를 다각형으로 crop하는 코드 '''
import numpy as np
import cv2

img = cv2.imread("cat.jpg")
# cv2.imshow("test",img)

height = img.shape[0]
width = img.shape[1]
# print(height, width)

point_x = [685,755,767,783,787,823,839,854,904,968,1074,1074,
           1161,1241,1225,1263,1269,1326,1326,1436,1448,1456,
           1460,1522,1504,1486,1482,1454,1476,1438,1380,1293,
           1257,1185,1161,1028,1018,972,962,900,888,844,805,
           831,844,791,799,801,775,809,813,852,839,880,900,
           894,876,886,862,850,870,842,854,801,781,773,751,739,727,719]

point_y = [197,179,153,149,139,139,121,131,108,98,137,149,177,
           229,245,263,301,359,380,534,607,663,763,914,928,916,
           984,1024,1066,1081,1091,1076,1087,1068,1081,1078,1068,
           1068,1060,1066,1028,980,972,916,890,932,876,852,850,
           803,763,717,707,677,643,596,603,572,586,574,534,520,
           482,466,430,382,359,349,291,273]

point_total = list(zip(point_x,point_y))

# print(point_total)

mask = np.zeros((height, width), dtype=np.uint8)
points = np.array(point_total)
cv2.fillPoly(mask,np.array([points],dtype=np.int32),(255))

res = cv2.bitwise_and(img,img,mask = mask)

rect = cv2.boundingRect(points)
cropped = res[rect[1]: rect[1] + rect[3], rect[0]: rect[0] + rect[2]]

cv2.imshow("cropped",cropped)
cv2.imshow("same size", res)
cv2.imwrite("cropped_test.png",cropped)

cv2.imwrite("cropped_img.png",res)
cv2.waitKey(0)
