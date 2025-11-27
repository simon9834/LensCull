import numpy as np
from PIL import Image


def image_histogram_similarity(img1: Image.Image, img2: Image.Image, resize=(512, 512)):
    """
    Method for computing image histogram similarity between two images and calculate the difference between the images
    :param img1: first image
    :param img2: second image
    :param resize: for custom resizing making the program faster
    :return: returns the similarity between two images as a number between 0 and 1
    """
    img1 = img1.resize(resize).convert('RGB')
    img2 = img2.resize(resize).convert('RGB')

    hist1 = np.array(img1.histogram(), dtype=np.float64)
    hist2 = np.array(img2.histogram(), dtype=np.float64)

    hist1 /= hist1.sum()
    hist2 /= hist2.sum()

    similarity = np.minimum(hist1, hist2).sum()
    return similarity


def compute_similarity(pair):
    """
    Method for reading image paths and calling similarity function
    :param pair: a pair of paths to an image
    :return: returns the images that were compared and their similarity or
    an exception if something fails
    """
    path1, path2 = pair[0], pair[1]
    try:
        img1 = Image.open(path1)
        img2 = Image.open(path2)
        score = image_histogram_similarity(img1, img2)
        return path1.name, path2.name, score
    except Exception as e:
            return path1.name, path2.name, f"Error: {e}"



