import cv2
import os
path='mani-image/'
images=os.listdir('mani-image/')
pathSaved=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))+'/resize-images/kid/'

percent=40
width=64
height=64
dsize=(width,height)
counter=1
for im in images:
    image=cv2.imread(path+im)
    resize=cv2.resize(image,dsize=dsize)
    gray = cv2.cvtColor(resize, cv2.COLOR_BGR2GRAY)
    status=cv2.imwrite(os.path.join(pathSaved,'{}.jpeg'.format(counter)),gray)
    print('Picture {} Success'.format(status))
    counter+=1

print(pathSaved)