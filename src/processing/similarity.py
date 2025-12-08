import numpy as np
from PIL import Image
import imagehash
import itertools
from src.Exceptions.NotImageException import NotImageException
from src.processing import Image_obj
from pathlib import Path

def compare_hashes(images):
    results = []
    if not isinstance(images, list):
        raise TypeError("images object must be a list")
    if len(images) < 2:
        raise IndexError("images list must have at least 2 images")
    for image in images:
        if not isinstance(image, Image_obj.Image):
            raise NotImageException("the object image is not an instance of class Image.Image")
    for pair in itertools.combinations(images, 2):
        histogram_distance = 1
        image1, image2 = pair
        phash_distance = abs(image1.p_hash - image2.p_hash)
        if phash_distance <= 8:
            if np.linalg.norm(image1.histogram) != 0:
                histogram_distance = np.linalg.norm(image1.histogram - image2.histogram) / np.linalg.norm(image1.histogram)
                if histogram_distance <= 0.25:
                    image1.similar.append(image2.path)
                else:
                    histogram_distance = None
            else:
                raise ZeroDivisionError("the histogram is zero")
        else:
            phash_distance = None
        results.append(f"{Path(image1.path).name} <-> {Path(image2.path).name}: {phash_distance} - {histogram_distance}")
    return results

def compute_similarity(img_path):
    try:
        img = Image.open(img_path)
        img = img.resize((256, 256)).convert('RGB')
        return Image_obj.Image(img_path, imagehash.phash(img), (np.array(img.histogram(), dtype=np.float64).flatten()))
    except Exception as e:
            raise Exception(img_path, f"Error: {e}")

