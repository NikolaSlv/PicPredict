# IMPORTANT
# unless you're willing to change the run.py script, keep the new_case, guess, and add_score methods.

from keras.models import load_model
from PIL import Image, ImageDraw
import numpy as np

currArr = []
def newDoodle(arr):
    arr = []

model_path = 'model_20240912-174238.keras'
model = load_model(model_path)

class_names = []
with open('labels.txt', 'r') as f:
    for l in f:
        class_names += [l.strip()]

def modelPredict(arr):
    image = Image.new('RGB', (1000, 1000))
    image_draw = ImageDraw.Draw(image)
    image_draw.rectangle([0, 0, 1000, 1000], fill=(255, 255, 255))

    min_x = 1000
    min_y = 1000
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
    image = image.resize((28, 28))
    image = image.convert('L')
    image = np.array(image)
    image = image.reshape((1, 28, 28, 1))

    predicted_class_id = np.argmax(model.predict(image))
    return class_names[predicted_class_id]

class Solution:
    def __init__(self):
        pass

    # this is a signal that a new drawing is about to be sent
    def new_case(self):
        newDoodle(currArr)
        pass

    # given a stroke, return a string of your guess
    
    def guess(self, x: list[int], y: list[int]) -> str:
        currArr.append([x, y])
        pred = modelPredict(currArr)
        
        return pred

        pass

    # this function is called when you get
    def add_score(self, score: int):
        print(score)
        pass
