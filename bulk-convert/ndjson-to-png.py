import json
from PIL import Image, ImageDraw

def makePng(arr, path, nameIndex):
    image = Image.new('RGB', (1000, 1000))
    image_draw = ImageDraw.Draw(image)
    image_draw.rectangle([0, 0, 1000, 1000], fill=(255, 255, 255))

    min_x = 10000
    min_y = 10000
    max_x = 0
    max_y = 0
    for stroke in arr:
        for i in range(len(stroke[0]) - 1):
            if stroke[0][i] < min_x:
                min_x = stroke[0][i]
            if stroke[1][i] < min_y:
                min_y = stroke[1][i]
            if stroke[0][i] > max_x:
                max_x = stroke[0][i]
            if stroke[1][i] > max_y:
                max_y = stroke[1][i]

    for stroke in arr:
        for i in range(len(stroke[0]) - 1):
            image_draw.line([stroke[0][i] - min_x, stroke[1][i] - min_y, stroke[0][i + 1] - min_x, stroke[1][i + 1] - min_y], fill=(0, 0, 0), width=5)
    
    image = image.crop((0, 0, max_x - min_x, max_y - min_y))

    if not os.path.exists(path):
        os.makedirs(path)
    image.save(path + 'output' + str(nameIndex) + '.png')

def convertNdjson(file, pathId):
    with open(file) as f:
        lines = f.readlines()
    filename = file.split('.')[0]
    filename = filename.split('/')[1]
    currPath = filename + '/'
    for i in range(lines.__len__()):
        raw_drawing = json.loads(lines[i])
        arr = raw_drawing['strokes']
        # catch exception
        try:
            makePng(arr, 'png/' + currPath, str(i))
        except:
            print('error')
            continue

# iterate all files in ndjson
import os
path = 'ndjson/'
files = os.listdir(path)
pathId = 0
for file in files:
    convertNdjson(path + file, str(pathId))
    pathId += 1
