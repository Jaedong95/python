from PIL import Image 

img = Image.open('baby.jpg')

# 이미지 포맷 정보 확인 
print(img.format)   

# 이미지 사이즈 확인 
print(img.size)   

# 이미지 사이즈 조절하기
print(img.resize((500, 500)))

# 이미지 자르기 
xy = (500, 100, 900, 400)    # 좌표 지정 
crop_img = img.crop(xy) 

# 이미지 저장
crop_img.save('crop_baby.jpg')

# 이미지 병합하기 
xy = (0, 0, 400, 300)   # 붙여넣을 위치 지정 
img.paste(crop_img, xy) 

# 이미지 회전하기
img_r = img.rotate(90)   

# 이미지 반전하기 
img_opp = img.transpose(Image.FLIP_LEFT_RIGHT)   # 좌우 반전 
img_opp2 = img.transpose(Image.FLIP_TOP_BOTTOM)   # 상하 반전 


# 모드 확인 (RGB) 후 분리하여 담기
print(img.mode)   # RGB
r, g, b = img.split() 
r.show()
g.show()
b.show() 

# RGB 합치기 
rgb_img = Image.merge('RGB', (r, g, b))   # RGB모드 r, g, b로 merge 
bgr_img = Image.merge('RGB', (b, r, g))   # RGB모드 b, r, g로 merge 

# Image Filter
from PIL import ImageFilter 

img1 = img.filter(ImageFilter.BLUR)
img2 = img.filter(ImageFilter.EMBOSS)
img3 = img.filter(ImageFilter.CONTOUR)

# 이미지 보여주기 
img.show()   


''' Pillow + Tkinter '''
# PIL 내의 imageTK 모듈 이용 
from PIL import image, ImageTk
import tkinter 

# Canvas 
root = tkinter.Tk()
canvas = tkinter.Canvas(root, width = 1200, height=867)   # Canvas 지정 
canvas.pack()   # Canvas 생성 
img = image.open('baby.jpg') 

# tkinter에서 Image를 사용할 수 있도록 형식 변환 
img_tk = ImageTk.PhotoImage(img)

# 변환한 이미지 띄우기 
canvas.create_image(600, 430, image=img_tk)


''' RGB picker '''
# 그림의 한 곳을 클릭하면 해당 RGB 값을 출력하는 프로그램 
import tkinter 

root = tkinter.Tk()
cv = tkinter.Canvas(root, width=500, height=300)

# 클릭 이벤트 생성 
def click(event):
    print('클릭 위치: ', event.x, event.y)   # event.x: 클릭 이벤트시의 x 좌표 
    
    # getpixel(x, y)을 이용해 해당 부분의 픽셀 구하기
    r, g, b = img.getpixel((event.x, event.y))
    print(f'R: {r}, G: {g}, B: {b}')

cv.bind('<Button-1>', click)  
cv.pack() 

from PIL import Image, ImageTk

img = Image.open('baby.jpg')
img_tk = ImageTk.PhotoImage(img)
cv.create_image(250, 250, image=img_tk)   # Canvas에 이미지 출력 

root.mainloop()
