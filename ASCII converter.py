import cv2, os
import numpy as np

def imageprepare(frame, sizeh, sizev):
    img = cv2.imread(frame,0)
    #img = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    img = cv2.resize(img, (sizeh, sizev))
    return img

os.chdir(os.path.dirname(__file__))

gscale1 = [' ','.',',',':',';','+','*','?','%','S','#','@']

sizeh = 16*20
sizev = 9*20
ratio = 255/len(gscale1)

path = 'img/guts.jpg'
frame = imageprepare(path, sizeh, sizev)


txt = ''

for i in range(sizev):
    for j in range(sizeh):
        pixel = int(round(frame[i][j]/ratio))
        txt += gscale1[pixel-1]

    print(txt)
    txt = ''
    



