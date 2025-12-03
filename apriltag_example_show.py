import numpy as np
import cv2
import sys
import traceback

while True:
    width = 160
    height = 120
    #data = sys.stdin.buffer.read(width * height)
    #detections = eval(sys.stdin.readline())
    while True:
        line = sys.stdin.readline()[:-1]
        print(line)
        if not line.startswith(':'):
            #print(line)
            continue
        det,enc = line[1:-1].split(':', 1)
        data = eval(enc)
        detections = eval(det)
        break

    img = np.zeros([height,width,3])
    img[:,:,0] = np.ones([height,width])*64
    img[:,:,1] = np.ones([height,width])*128
    img[:,:,2] = np.ones([height,width])*192
    for x in range(width):
        for y in range(height):
            r = data[1*(y*width+x)]
            g = data[1*(y*width+x)]
            b = data[1*(y*width+x)]
            img[y][x] = [b, g, r]

    print(detections)
    for detection in detections:
        center = list(int(c) for c in detection)
        img = cv2.circle(img, center, 5, [255, 0, 0], 1)
    #cv2.waitKey(0)
    #cv2.destroyAllWindows()
    cv2.imwrite("out.png", img)
#print(img[10][10])
#cv2.imwrite("out.png", img)
