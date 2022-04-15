''' 이미지 사이즈 조절 (용량 조절용) ''' 
import glob 
from PIL import Image 

image_dir = './'
image_name = '증명사진.jpg'
image_width = 120
image_height = 160

files = glob.glob(image_dir + image_name)
for i, f in enumerate(files):
    img = Image.open(f)
    img = img.resize((image_width, image_height))

img2 = img.save('me.jpg')