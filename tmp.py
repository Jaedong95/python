import cv2
import numpy as np
import imutils  # resize1
import cv2
import numpy as np
#신호등
def set_blob_param(r_type: str):
    # BLOB 필터 생성하기 
    params = cv2.SimpleBlobDetector_Params()
    
    params.minThreshold = 10
    params.maxThreshold = 255
    params.thresholdStep = 10
    params.filterByArea = False
    params.filterByColor = False
    params.filterByCircularity = True
    params.filterByConvexity = False 
    params.filterByInertia = False 
    
    if r_type == 'color':
        # 경계 값 조정
        params.minCircularity = 0.8
        params.maxCircularity = 1     
    elif r_type == 'shape':
        params.filterByArea = True 
        params.minArea = 100
        params.maxArea = 250
        
        params.filterByColor = False
#         params.blobColor = 0
        
        params.minCircularity = 0.4
        params.maxCircularity = 0.8
    
    return params 
# 신호등으로 추정되는 영역 검출 
def subtract_shape(img):
    global k, h, w   # 모폴로지 연산 필터 
    
    img_gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    # roi_s = img_gray[int((1/5)*w):int((4/5) * w), int((1/5)*h): int((4/5)*h)]
    roi_s = img_gray[int((1/5)*w):int((3/5) * w), int((1/5)*h): int((3/5)*h)]
    blur = cv2.GaussianBlur(roi_s, (3, 3), 0)

    # ret, th = cv2.threshold(roi_s, 55, 255, cv2.THRESH_BINARY)
    _, t_otsu = cv2.threshold(blur, -1, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)

    cv2.imshow('th',t_otsu)
    dst_s = cv2.morphologyEx(t_otsu, cv2.MORPH_OPEN, k)   # 모폴로지 열기 연산 
    #필터 확인
    edge_s = cv2.Laplacian(dst_s, -2)
    detector = cv2.SimpleBlobDetector_create(param_s)
    
    s_keypoints = detector.detect(edge_s)
    img_draw_s = cv2.drawKeypoints(roi_s, s_keypoints, None, None, cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS) 
            
    global shape_list 
    
    for s_keypoint in s_keypoints:
        roi_cx, roi_cy = map(int, s_keypoint.pt)
        cx, cy = int(roi_cx + h * (1/5)), int(roi_cy + w * (1/5))
#        cx, cy = int(roi_cx + h * (1/13)), int(roi_cy + w * (1/13))
        
        cv2.putText(img_gray, '!', (cx, cy), cv2.FONT_HERSHEY_TRIPLEX, 1,(255, 255, 255))
        size = int(s_keypoint.size)
        cx2, cy2 = cx + size // 2, cy + size // 2    
        shape_list.append([cx, cx2, cy, cy2])
    cv2.imshow('img_gray',img_gray)
    return shape_list  
###########
# 신호등 색상에 해당되는 영역 검출 
def subtract_color(img, color):
    global k, w, h   # 모폴로지 연산 필터 
    
    lower_green = np.array([50, 50, 80]); upper_green = np.array([90, 255, 255])
    lower_red = np.array([-10, 30, 30]);  upper_red = np.array([10, 255, 255])
    lower_yellow = np.array([11, 50, 50]); upper_yellow = np.array([30, 255, 255])
    
    img_hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

    roi_c = img_hsv[int((1/5)*w):int((3/5) * w), int((1/5)*h): int((3/5)*h)]
    #roi_c = img_hsv[int((1/13)*w):int((2/5) * w), int((1/13)*h): int((2/5)*h)]
        
    if color == 'red':
        mask = cv2.inRange(roi_c, lower_red, upper_red)
    elif color == 'green':
        mask = cv2.inRange(roi_c, lower_green, upper_green)   
    elif color == 'yellow':
        mask = cv2.inRange(roi_c, lower_yellow, upper_yellow) 
        
    img_mask = cv2.bitwise_and(roi_c, roi_c, mask=mask)
    edge_c = cv2.Laplacian(img_mask, -1)
    # dst_c = cv2.morphologyEx(edge_c, cv2.MORPH_OPEN, k) 적용 x (검출률 저하)
    detector = cv2.SimpleBlobDetector_create(param_c)
    c_keypoints = detector.detect(edge_c)
    img_draw_c = cv2.drawKeypoints(roi_c, c_keypoints, None, None, cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)
    # cv2.imshow('img_draw_c', img_draw_c)

    global color_list 
    
    for c_keypoint in c_keypoints:
        roi_cx, roi_cy = map(int, c_keypoint.pt)
        cx, cy = int(roi_cx + h * (1/5)), int(roi_cy + w * (1/5))
        #cx, cy = int(roi_cx + h * (2/5)), int(roi_cy + w * (2/5))
        
        cv2.putText(img_hsv, '!', (cx, cy), cv2.FONT_HERSHEY_TRIPLEX, 1,(255, 255, 255))
        size = int(c_keypoint.size)
        cx2, cy2 = cx + size // 2, cy + size // 2 
        color_list.append([cx, cx2, cy, cy2])
    
    cv2.imshow('img_hsv', img_hsv)        
    return color_list
                
##########################################################################
##겹치는 사각형 영역의 꼭지점 수 검출 함수
def spot_check(rect1, rect2):
    #좀더 좌측 상단에 있는 시작점을 검출해 이것을 기준으로 함
    #x좌표를 기준으로 검출
    if rect1[0] < rect2[0]:
        standard_rect = rect1
        other_rect= rect2
    else:
        standard_rect = rect2
        other_rect= rect1
    #standard 사각형 기준    
                                                           #list(range(1,3)) >>> [1,2]
    #range(          x좌표,           x좌표+가로길이(너비)+range는 미만으로 수를 잡으므로 +1 
    xrange= range(int(standard_rect[0]),int(standard_rect[0])+int(standard_rect[2])+1) 
    #range(          y좌표,           y좌표+세로길이(높이)+range는 미만으로 수를 잡으므로 +1 
    yrange= range(int(standard_rect[1]),int(standard_rect[1])+int(standard_rect[3])+1)   
    
    #겹치는지 확인하기 위한 비교대상이 되는 사각형(other_rect) 기준
    min_check_x=int(other_rect[0])                #x의 최소값: check_x
    max_check_x=int(other_rect[0]+other_rect[2])  #x의 최대값:check_x+check_w
    min_check_y=int(other_rect[1])                #y의 최소값: check_y   
    max_check_y=int(other_rect[1]+other_rect[3])  #y의 최대값:check_y+check_h 
    
    #검출된 겹치는 꼭지점 개수 초기화
    total_points=0
    #좌측상단 꼭지점 확인
    if min_check_x in xrange and min_check_y in yrange:
        total_points+=1
    #우측상단 꼭지점 확인
    if max_check_x in xrange and min_check_y in yrange:
        total_points+=1
    #좌측하단 꼭지점 확인
    if max_check_y in yrange and min_check_x in xrange:
        total_points+=1
    #우측하단 꼭지점 확인
    if max_check_x in xrange and max_check_y in yrange:
        total_points+=1
    
    return total_points
###############################################################################################################################
##겹치는 사각형 영역의 꼭지점 수 검출 함수
def spot_check(rect1, rect2):
    #좀더 좌측 상단에 있는 시작점을 검출해 이것을 기준으로 함
    #x좌표를 기준으로 검출
    if int(rect1[0]) < int(rect2[0]):
        standard_rect = rect1
        other_rect= rect2
    else:
        standard_rect = rect2
        other_rect= rect1
    #standard 사각형 기준    
                                                           #list(range(1,3)) >>> [1,2]
    #range(          x좌표,           x좌표+가로길이(너비)+range는 미만으로 수를 잡으므로 +1 
    xrange= range(int(standard_rect[0]),int(standard_rect[0])+int(standard_rect[2])+1) 
    #range(          y좌표,           y좌표+세로길이(높이)+range는 미만으로 수를 잡으므로 +1 
    yrange= range(int(standard_rect[1]),int(standard_rect[1])+int(standard_rect[3])+1)   
    
    #겹치는지 확인하기 위한 비교대상이 되는 사각형(other_rect) 기준
    min_check_x=int(other_rect[0])                #x의 최소값: check_x
    max_check_x=int(other_rect[0])+int(other_rect[2])  #x의 최대값:check_x+check_w
    min_check_y=int(other_rect[1])                #y의 최소값: check_y   
    max_check_y=int(other_rect[1])+int(other_rect[3])  #y의 최대값:check_y+check_h 
    
    #검출된 겹치는 꼭지점 개수 초기화
    total_points=0
    #좌측상단 꼭지점 확인
    if min_check_x in xrange and min_check_y in yrange:
        total_points+=1
    #우측상단 꼭지점 확인
    if max_check_x in xrange and min_check_y in yrange:
        total_points+=1
    #좌측하단 꼭지점 확인
    if max_check_y in yrange and min_check_x in xrange:
        total_points+=1
    #우측하단 꼭지점 확인
    if max_check_x in xrange and max_check_y in yrange:
        total_points+=1
    
    return total_points
###############################################################################################################################
##횡단보도와 사람객체 roi 추적 API
#디폴트 에이다 부스트를 이용한 검출 
#영상의 길이가 멀어질 수록 잘 검출이 안됨 
#사각은 정면보다 특히나 검출이 더 안됨
#트랙커 객체 생성자 함수 리스트 
trackers = [cv2.TrackerBoosting_create,
            cv2.TrackerMIL_create,
            cv2.TrackerKCF_create,
            cv2.TrackerTLD_create,
            cv2.TrackerMedianFlow_create,
            cv2.TrackerGOTURN_create, #버그로 오류 발생 안하는게 좋음
            cv2.TrackerCSRT_create,
            cv2.TrackerMOSSE_create]
trackerIdx = 0  # 트랙커 생성자 함수 선택 인덱스
tracker1 = None
tracker2 = None
isFirst = True
video_src = 0 # 비디오 파일과 카메라 선택 
video_src = "./cropped_traffic2.mp4"
cap = cv2.VideoCapture(video_src)
fps = cap.get(cv2.CAP_PROP_FPS) # 프레임 수 구하기
delay = int(1000/fps)
win_name = 'Tracking APIs'
ROIs=0
crop_imgs= [] 
param_c = set_blob_param('color')
param_s = set_blob_param('shape')
k = cv2.getStructuringElement(cv2.MORPH_RECT, (2, 2))   # 모폴로지 연산 필터 
shape_list = []
color_list = [] 
w = 800; h = 800      
color_flag = 'green'

while cap.isOpened():
    global fps, delay, k    
    ret, frame = cap.read()
    
    frame = imutils.resize(frame, width = 800)  # resize1
    #frame = cv2.resize(img, (800,800))
    
    if not ret:
        print('Cannot read video file')
        break
    img_draw = frame.copy()
    if tracker1 is None and tracker2 is None: # 트랙커 생성 안된 경우
        cv2.putText(img_draw, "Press the Space to set ROI", \
            (100,80), cv2.FONT_HERSHEY_SIMPLEX, 0.75,(0,0,255),2,cv2.LINE_AA)
    else:
        ok1, bbox1 = tracker1.update(frame)   # 새로운 프레임에서 추적 위치 찾기 
        ok2, bbox2 = tracker2.update(frame)   # 새로운 프레임에서 추적 위치 찾기 
        (x1,y1,w1,h1) = bbox1
        #print('bbox1',bbox1)
        (x2,y2,w2,h2) = bbox2
        #print('bbox2',bbox2)
                
        if ok1 and ok2: # 추적 성공
            cv2.rectangle(img_draw, (int(x1), int(y1)), (int(x1 + w1), int(y1 + h1)), \
                          (255,0, 0), 2, 1) #img_draw
            cv2.rectangle(img_draw, (int(x2), int(y2)), (int(x2 + w2), int(y2 + h2)), \
                          (0,0,255), 2, 1) #img_draw
            #1번째 조건부여   
            #if사람 객체 roi가 횡단보도 객체roi와 겹친다면 횡단보도 보행자로 인식
            if spot_check(bbox1, bbox2)>0: #최소한 꼭지점 하나영역이 겹친다면 
                cv2.putText(img_draw, "STOP!", (100,80), cv2.FONT_HERSHEY_SIMPLEX, 2,(0,0,255),2,cv2.LINE_AA)  
                shape_list = subtract_shape(img_draw)
                #print('shape_list', shape_list) 
                color_list = subtract_color(img_draw, color_flag)
                #print('color_list', color_list)
                tl_flag = False 
                for a1, a2, b1, b2 in color_list:
                    for x1, x2, y1, y2 in shape_list:
                        if ((a1 >= x1 and a1 <= x2) and (b1 >= y1 and b1 <= y2)) and tl_flag == False:
                            cv2.putText(img_draw, f'{color_flag} Light Detected!', (100, 120), cv2.FONT_HERSHEY_TRIPLEX, 1,(255, 255, 255))
                            tl_flag = True 
            else:
                cv2.putText(img_draw, "", (100,80), cv2.FONT_HERSHEY_SIMPLEX, 2,(0,0,255),2,cv2.LINE_AA)
                
        else : # 추적 실패
            cv2.putText(img_draw, "Tracking fail.", (100,80), \
                        cv2.FONT_HERSHEY_SIMPLEX, 0.75,(0,0,255),2,cv2.LINE_AA)
    trackerName = tracker1.__class__.__name__
    cv2.putText(img_draw, str(trackerIdx) + ":"+trackerName , (100,20), \
                 cv2.FONT_HERSHEY_SIMPLEX, 0.75, (0,0,255),2,cv2.LINE_AA)
    cv2.imshow(win_name, img_draw)
    key = cv2.waitKey(delay) & 0xff
    # 스페이스 바 또는 비디오 파일 최초 실행 
    if (video_src != 0 and isFirst):#key == ord(' ') or (video_src != 0 and isFirst): 
        isFirst = False
        ##
        hogdef = cv2.HOGDescriptor()
        hogdef.setSVMDetector(cv2.HOGDescriptor_getDefaultPeopleDetector())
        hogdaim = cv2.HOGDescriptor((48,96), (16,16), (8,8), (8,8), 9)
        hogdaim.setSVMDetector(cv2.HOGDescriptor_getDaimlerPeopleDetector())
        cap = cv2.VideoCapture(video_src)
        while cap.isOpened():
            global ROIs, crop_imgs
            ret, img = cap.read()
            if img is None:
                break
            img2 = img.copy()
            if ret :
                # resize
                img = imutils.resize(img, width = 800)  # resize1#counter to save image with different name
                # default 디텍터로 보행자 검출
                found, _ = hogdef.detectMultiScale(img)
                for (x0, y0, w0, h0) in found:
                    cv2.rectangle(img, (x0, y0), (x0 + w0, y0 + h0), (0, 255, 255), 2)
                cv2.putText(img, 'Detector:%s'%('Default'), (10, 50), cv2.FONT_HERSHEY_DUPLEX,1, (0, 255, 0),1)
                cv2.imshow(win_name, img)
                # daimler 디텍터로 보행자 검출
                key = cv2.waitKey(1)
                if key == 27:
                    break
                if key == 32: # 스페이스
                    ROIs = cv2.selectROIs(win_name,img)
                    crop_imgs= [] 
                    for rect in ROIs:
                        x1=rect[0]
                        y1=rect[1]
                        x2=rect[2]
                        y2=rect[3]
                        crop_imgs.append((x1,y1,xdsa2,y2))
                    cv2.waitKey()sdas
            else:
                break
        if len(crop_imgs) != 0:         # 위치 설정 값 있는 경우
            tracker1 = trackers[trackerIdx]()    #트랙커 객체 생성 
            isInit1 = tracker1.init(frame, crop_imgs[0]) #roi1
            tracker2 = trackers[trackerIdx]sa()    #트랙커 객체 생성
            isInit2 = tracker2.init(frame, crop_imgs[1]) #roi2
    elif key in range(48, 56): # 0~7 숫자 입력  #근데 안될 수 있는게 있을 수도 있음
        trackerIdx = key-48     # 선택한 숫자로 트랙커 인덱스 수정
        if bbox1 is not None and bbox2 is not None:
            tracker1 = trackers[trackerIdx]() # 선택한 숫자의 트랙커 객체 생성 
            isInit1 = tracker1.init(frame, bbox1) # 이전 추적 위치로 추적 위치 초기화
            tracker2 = trackers[trackerIdx]() # 선택한 숫자의 트랙커 객체 생성 
            isInit2 = tracker2.init(frame, bbox2) # 이전 추적 위치로 추적 위치 초기화
    elif key == 27 : 
        breakasd
else:
    print( "Could not open video")sda
cap.release()
cv2.destroyAllWindows() sda