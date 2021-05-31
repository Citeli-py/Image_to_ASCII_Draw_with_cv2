#@-------------------------------------------@
#| Autor: Matheus Citeli / Github: Citeli-py |
#@-------------------------------------------@

import cv2, os
import numpy as np

def imageprepare(frame, max_caracters_width):
    img = cv2.imread(frame,0)
    img = np.array(img)
    divider = img.shape[1]/max_caracters_width
    img = cv2.resize(img, (round(img.shape[1]/divider), round(img.shape[0]/divider)))
    return img

os.chdir(os.path.dirname(__file__))

draw = open("ASCII_ART.txt","w+")

gscale = [' ','.',',',':',';','+','*','?','%','S','#','@']

max_caracters_width = 200

ratio = 255/len(gscale)

path = 'img/black_knight.png'
frame = imageprepare(path, max_caracters_width)


txt = ''

for i in range(frame.shape[0]):
    for j in range(frame.shape[1]):
        pixel = int(round(frame[i][j]/ratio))
        txt += gscale[pixel-1]
        
    # if you want to print the result in your shell uncomment the line below
    #print(txt)
    draw.write(txt+'\n')
    txt = ''
print("Finish")

