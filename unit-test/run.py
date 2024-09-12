from keras.models import load_model
from PIL import Image
import numpy as np

model_path = 'model_20240912-174238.keras'
model = load_model(model_path)
model.summary()

class_names = []
with open('labels.txt', 'r') as f:
    for l in f:
        class_names += [l.strip()]
   
def test(img_name):
    img = Image.open(img_name)
    img = img.resize((28, 28))
    img = img.convert('L')
    img = np.array(img)
    img = img.reshape((1, 28, 28, 1))

    predicted_class_id = np.argmax(model.predict(img))
    return class_names[predicted_class_id]

print(test('img/img1.png'))
print(test('img/img2.png'))
print(test('img/img3.png'))
