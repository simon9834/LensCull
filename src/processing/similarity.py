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


"""
import torch
import clip
import numpy as np
from PIL import Image


# Load CLIP model only once (global)
_device = "cuda" if torch.cuda.is_available() else "cpu"
_model, _preprocess = clip.load("ViT-B/32", device=_device)


def image_clip_similarity(img1: Image.Image, img2: Image.Image, resize=(512, 512)):
    """
    Compute similarity between two images using CLIP embeddings.
    :param img1: First image
    :param img2: Second image
    :param resize: Optional resize to speed inference
    :return: similarity between 0 and 1
    """

    # resize + convert
    img1 = img1.resize(resize).convert("RGB")
    img2 = img2.resize(resize).convert("RGB")

    # preprocess for CLIP
    t1 = _preprocess(img1).unsqueeze(0).to(_device)
    t2 = _preprocess(img2).unsqueeze(0).to(_device)

    # compute embeddings
    with torch.no_grad():
        e1 = _model.encode_image(t1)
        e2 = _model.encode_image(t2)

    # flatten + normalize
    e1 = e1.cpu().numpy().reshape(-1)
    e2 = e2.cpu().numpy().reshape(-1)

    e1 /= np.linalg.norm(e1)
    e2 /= np.linalg.norm(e2)

    # cosine similarity => 1 = same image
    similarity = float(np.dot(e1, e2))

    return similarity


def compute_similarity(pair):
    """
    Same structure as your version.
    Reads image paths + computes CLIP similarity.
    """

    path1, path2 = pair[0], pair[1]

    try:
        img1 = Image.open(path1)
        img2 = Image.open(path2)

        score = image_clip_similarity(img1, img2)
        return path1.name, path2.name, score

    except Exception as e:
        return path1.name, path2.name, f"Error: {e}"

"""

