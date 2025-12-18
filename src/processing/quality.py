
import cv2
import numpy as np

def calculate_quality(img_obj):
    """
    Calculate an overall quality score for an image based on brightness, sharpness, and noise.
    Sharpness is given higher weight in the final score. The final estimated quality is scaled
    to a 0–100 range.
    :param img_obj: Image object with a `path` attribute pointing to the image file.
                    The function will update the following attributes of img_obj:
                        - brightness_quality (float, 0–1)
                        - sharpness (float, 0–1, normalized)
                        - noise (float, 0–1)
                        - est_quality (int, 0–100)
    :return: The same img_obj with updated quality metrics.
    """
    img = cv2.imread(img_obj.path, cv2.IMREAD_GRAYSCALE)
    img_small = cv2.resize(img, (512, 512), interpolation=cv2.INTER_AREA)

    img_obj.brightness_quality = brightness_score(img_small)
    sharpness = sharpness_score(img_small)
    img_obj.noise = noise_score(img_small)
    img_obj.sharpness = np.clip((sharpness - 100) / (500 - 100), 0, 1)
    est_quality = 0.2 * img_obj.brightness_quality + 0.7 * img_obj.sharpness + 0.1 * (1 - img_obj.noise)
    img_obj.est_quality = int(np.clip(est_quality * 170, 0, 100))
    return img_obj

def brightness_score(image_opened):
    """
    Calculate a normalized brightness score for a grayscale image.
    :param image_opened: Grayscale image as a NumPy array.
    :return: Brightness quality as a float between 0 and 1.
             Ideal values are approximately 0.4–0.7.
    """
    return np.mean(image_opened) / 255


def sharpness_score(image_opened):
    """
    Calculate a sharpness score using the variance of the Laplacian.
    :param image_opened: Grayscale image as a NumPy array.
    :return: Sharpness as a float. Interpretation:
             - <100: blurry
             - 100–500: acceptable
             - >500: oversharpened
    """
    return cv2.Laplacian(image_opened, cv2.CV_64F).var()


def noise_score(image_opened):
    """
    Estimate the noise level of a grayscale image using Gaussian smoothing.
    :param image_opened: Grayscale image as a NumPy array.
    :return: Normalized noise level as a float between 0 and 1.
             Higher numbers indicate more noise.
    """
    h, w = image_opened.shape
    M = 5
    smooth = cv2.GaussianBlur(image_opened, (M, M), 0)
    noise = image_opened - smooth
    return np.std(noise) / 255


