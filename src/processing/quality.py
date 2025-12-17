
import cv2
import numpy as np

class Quality_assessment:
    def __init__(self, image_objects):
        self.image_objects = image_objects

    def calculate_quality(self):
        for img_obj in self.image_objects:
            img = cv2.imread(img_obj.path, cv2.IMREAD_GRAYSCALE)
            img_small = cv2.resize(img, (512, 512), interpolation=cv2.INTER_AREA)

            img_obj._brightness_quality = self.brightness_score(img_small)
            img_obj.sharpness = self.sharpness_score(img_small)
            img_obj.noise = self.noise_score(img_small)
            img_obj.est_quality = max(0, min(0.4 * self.image_objects.bright + 0.4 * self.image_objects.sharp + 0.2 * self.image_objects.noise, 1))

    def brightness_score(self, image_opened):
        #0-1 Ideal values: ~0.4–0.7
        return np.mean(image_opened) / 255

    def sharpness_score(self, image_opened):
        #<100 blurry, 100-500 ok, 500+ oversharpened
        return cv2.Laplacian(image_opened, cv2.CV_64F).var()

    def noise_score(self, image_opened):
        #0-1 more number -> more noise
        h, w = image_opened.shape
        M = 5
        smooth = cv2.GaussianBlur(image_opened, (M, M), 0)
        noise = image_opened - smooth
        return np.std(noise) / 255




