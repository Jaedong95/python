''' 1. 비디오 -> 이미지 (이미지 이름: 0 ~ n) ''' 
import cv2

vidcap = cv2.VideoCapture('3rd_26_reversed.mp4')
stat, image = vidcap.read()

fps = vidcap.get(cv2.CAP_PROP_FPS)
delay = int(1000 / fps)
print('FPS: %f, Delay: %dms' % (fps, delay))

count = 1
idx = 1
success = True
img_cat = "3rd_video_"

while success:
    success, image = vidcap.read()
    if count % 12 == 0:
        cv2.imwrite("3rd_reversed/" + img_cat + "%d.jpg" % idx, image)
        #cv2.imwrite('TLH_11/A1_additional_procedures/img/%d.jpg' % idx, image)
        print("saved image %d.jpg" % idx)
        idx += 1

    if cv2.waitKey(10) == 27:
        break
    count += 1


''' 2. 비디오 -> 이미지 (이미지 이름: 현재 시간) '''
import cv2
import datetime

video_file = '1st_55.mp4'
	
cap = cv2.VideoCapture(video_file)

if cap.isOpened():
    fps = cap.get(cv2.CAP_PROP_FPS)
    delay = int(1000/fps)
    print('FPS: %f, Delay: %dms' %(fps, delay))

    while True:
        ret, img = cap.read()
        now = datetime.datetime.now().strftime("%d_%H-%M-%S")
        print(now)

        if ret:
            cv2.imshow(video_file, img)
            key = cv2.waitKey(12)
            if key == 27:
                break

            cv2.imwrite('1st/'+ now + '.jpg',img)

            '''
            if cv2.waitKey(1) != -1:
                cv2.imwrite('tmp.jpg', img)
                break
            '''
        else:
            break
else:
    print("can't open video.")

cap.release()
cv2.destroyAllWindows()
