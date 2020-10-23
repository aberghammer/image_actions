import json
import cv2
import argparse

# command line parser
parser = argparse.ArgumentParser(description="Process a folder of images with a .json")
parser.add_argument('-p', "--base_path", type=str, default="D:/Datasets/", help="basepath of dataset folder")
parser.add_argument('-i', "--image_path", type=str, help="path to image folder")
parser.add_argument('-j', "--json_path", type=str, default=".json", help="path to .json file")
parser.add_argument('-o', "--out_path", type=str, default="Fantasy_512/", help="path to output folder")
parser.add_argument('--save', action="store_true")
args = parser.parse_args()

# get folder name and check out_path
txt = args.image_path.split("/")
check = args.out_path.split("/")
if txt[len(txt)-1] == "":
    folder = txt[len(txt) - 2]
else:
    folder = txt[len(txt) - 1]
    args.image_path = args.image_path + "/"
print("Dataset folder: ", folder)
if check[len(check)-1] != "":
    args.out_path = args.out_path + "/"
print("Output directory: ", args.out_path)

# read images and json
if args.json_path == ".json":
    args.json_path = args.image_path + folder + ".json"
with open(args.base_path + args.json_path, "r") as f:
    data = json.load(f)

# processing
index = 0
while index < len(data):
    print(data[index]["image"])
    path = args.base_path + args.image_path + data[index]["image"]
    img = cv2.imread(path)
    inner = 0
    for item in data[index]["annotations"]:
        print(img.shape)
        x = data[index]["annotations"][inner]["coordinates"]["x"]
        y = data[index]["annotations"][inner]["coordinates"]["y"]
        w = data[index]["annotations"][inner]["coordinates"]["width"]
        h = data[index]["annotations"][inner]["coordinates"]["height"]

        botleftx = int(x - (w / 2))
        botlefty = int(y - (h / 2))
        print("botleft: ", botleftx, botlefty)
        toprightx = int(x + (w / 2))
        toprighty = int(y + int(h / 2))
        print("topright: ", toprightx, toprighty)

        # img = cv2.circle(img, (393 - int(187/2), 102 - int(172/2)), 5, (0,0,0), 5)
        # img = cv2.circle(img, (393 + int(187/2), 102 + int(172/2)), 5, (0,0,0), 5)

        # cv2.rectangle(image1, (rects[1], rects[2], rects[3], rects[4]), (255,255,255), 1)
        # cv2.rectangle(img, (startx, endx),(starty, endy), (0, 0, 0), 0)
        crop_img = img[botlefty:toprighty, botleftx:toprightx, :]
        # endx:endx+h, startx:startx+w

        crop_img = cv2.resize(crop_img, (512, 512))
        if args.save is True:
            cv2.imwrite(args.base_path + args.out_path + folder + data[index]["image"][:-4] + ".png", crop_img)
        else:
            cv2.imshow("image", crop_img)
            cv2.waitKey(0)
        inner = inner + 1
    index = index + 1
