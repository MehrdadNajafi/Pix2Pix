import numpy as np
import cv2
from tensorflow.keras.models import load_model

class GeneratorModel:
    def __init__(self):
        self.generator_model = load_model("model/map_to_aerial.h5")
    
    def loadImage(self, image_path):
        image = cv2.imread(image_path)
        image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
        image = cv2.resize(image, (256, 256)).astype(np.float32)
        image = (image / 127.5) - 1
        image = image[np.newaxis, ...]
        return image
    
    def generate(self, image_path):
        image = self.loadImage(image_path)
        gen_image = self.generator_model(image, training=True)
        gen_image = np.array((gen_image + 1) * 127.5).astype(np.uint8)
        gen_image = np.squeeze(gen_image, axis=0)
        return gen_image