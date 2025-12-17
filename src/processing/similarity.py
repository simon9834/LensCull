import numpy as np
from PIL import Image
import imagehash
import itertools
from src.Exceptions.NotImageException import NotImageException
from src.processing import Image_obj
from pathlib import Path

def compare_hashes(images):
    """
    method that logically compares the calculated histograms and p_hashes
    :param images: a list of image_obj
    :return: returns a list of image paths pairs and their differences
    """
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
                    image1.add_similar(image2.path)
                else:
                    histogram_distance = None
            else:
                raise ZeroDivisionError("the histogram is zero")
        else:
            phash_distance = None
        image1.add_comparison(f"{Path(image1.path).name} <-> {Path(image2.path).name}: {phash_distance} - {histogram_distance}")

def compute_similarity(image_object):
    """
    a method to parallel calculate the histogram value and p_hash value
    :param image_object: the object of an image
    :return: returns an image_obj with all attributes
    """
    try:
        img = Image.open(image_object.path)
        img = img.resize((256, 256)).convert('RGB')
        image_object.p_hash(imagehash.phash(img))
        image_object.histogram(np.array(img.histogram(), dtype=np.float64).flatten())
    except Exception as e:
            raise Exception(image_object.path, f"Error: {e}")

