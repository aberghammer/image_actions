import json
import glob
import cv2

images = [cv2.imread(file) for file in glob.glob("./img/0-102/img/*")]
#image1 = cv2.imread("./test1.jpg")
with open('./img/0-102/Character.json') as f:
  data = json.load(f)

print(data)
index = 0
print(len(data[index]["annotations"]))
for img in images:
  inner = 0
  for item in data[index]["annotations"]:
    (height1, width1) = img.shape[:2]
    print(width1)
    print(height1)
    x = data[index]["annotations"][inner]["coordinates"]["x"]
    y = data[index]["annotations"][inner]["coordinates"]["y"]
    w = data[index]["annotations"][inner]["coordinates"]["width"]
    h = data[index]["annotations"][inner]["coordinates"]["height"]
    print("index" + str(index) + "inner" + str(inner))

    startx = int(x - (w/2))
    print("startx: ", startx)
    endx = int(y - (h/2))
    print("endx: ", endx)
    starty = int(x + (w/2))
    print("starty: ", starty)
    endy = int(y + int(h/2))
    print("endy: ", endy)

    #img = cv2.circle(img, (393 - int(187/2), 102 - int(172/2)), 5, (0,0,0), 5)
    #img = cv2.circle(img, (393 + int(187/2), 102 + int(172/2)), 5, (0,0,0), 5)

    #cv2.rectangle(image1, (rects[1], rects[2], rects[3], rects[4]), (255,255,255), 1)
    #cv2.rectangle(img, (startx, endx),(starty, endy), (0, 0, 0), 0)
    crop_img = img[endx:int(endx+h), startx:int(startx+w)]
    #endx:endx+h, startx:startx+w

    crop_img = cv2.resize(crop_img, (512, 512))
    cv2.imwrite("./img/0-102/results/"+str(index)+".png", crop_img)


    #cv2.imshow("image",crop_img)
    #cv2.waitKey(0)
    inner = inner + 1
  index = index + 1


