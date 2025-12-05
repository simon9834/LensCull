import numpy as np
from PIL import Image
import imagehash
import itertools
from src.processing import Image_obj

def compare_hashes(images):
    results = []

    for pair in itertools.combinations(images, 2):
        histogram_distance = 1
        image1, image2 = pair
        phash_distance = abs(image1.p_hash - image2.p_hash)
        if phash_distance <= 8:
            histogram_distance = np.linalg.norm(image1.histogram - image2.histogram) / np.linalg.norm(image1.histogram)
            if histogram_distance <= 0.25:
                image1.append(image2.path)
        results.append(f"{image1.path.name} <-> {image2.path.name}: {phash_distance} - {histogram_distance}")
    return results

def compute_similarity(img_path):
    try:
        img = Image.open(img_path)
        img = img.resize((256, 256)).convert('RGB')
        return Image_obj.Image(img_path, imagehash.phash(img), (np.array(img.histogram(), dtype=np.float64).flatten()))
    except Exception as e:
            return img_path, f"Error: {e}"

