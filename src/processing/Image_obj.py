from imagehash import ImageHash
from numpy import ndarray

class Image:
    def __init__(self, path, histogram=None, p_hash=None, brightness_quality=None,sharpness=None, noise=None, est_quality=None):
        """
        this method defines the variables for this class with their setters and getters
        :param path: define when initializing the image
        :param histogram: should not be initialized here
        :param p_hash: should not be initialized here
        :param brightness_quality: should not be initialized here
        :param sharpness: should not be initialized here
        :param noise: should not be initialized here
        :param est_quality: should not be initialized here
        """
        self._path = None
        self._histogram = None
        self._p_hash = None
        self._brightness_quality = None
        self._sharpness = None
        self._noise = None
        self._est_quality = None
        self._similar = []
        self._comparison = []

        self.path = path
        self.histogram = histogram
        self.p_hash = p_hash
        self.brightness_quality = brightness_quality
        self.sharpness = sharpness
        self.noise = noise
        self.est_quality = est_quality

    # ---------------- Path ----------------
    @property
    def path(self):
        """
        returns the local variable _path
        :return: string, path
        """
        return self._path

    @path.setter
    def path(self, value):
        """
        sets the path for the image
        :param value: string, path
        :return: may return Errors if wrong type or is empty
        """
        if not isinstance(value, str):
            raise TypeError(f"Failed to set path: expected str, got {type(value).__name__}")
        if not value:
            raise ValueError("Failed to set path: path cannot be empty")
        self._path = value

    # ---------------- Histogram ----------------
    @property
    def histogram(self):
        """
        returns the local variable _histogram
        :return: ndarray, histogram
        """
        return self._histogram

    @histogram.setter
    def histogram(self, value):
        """
        sets the histogram for the image
        :param value: ndarray, histogram
        :return: may  return Errors if wrong type
        """
        if value is not None and not isinstance(value, ndarray):
            raise TypeError(f"Failed to set histogram: expected list or tuple, got {type(value).__name__}")
        self._histogram = value

    # ---------------- Perceptual Hash ----------------
    @property
    def p_hash(self):
        """
        returns the local variable _p_hash
        :return: ImageHash, p_hash
        """
        return self._p_hash

    @p_hash.setter
    def p_hash(self, value):
        """
        sets the p_hash for the image
        :param value: ImageHash, p_hash
        :return: may  return Errors if wrong type
        """
        if value is not None and not isinstance(value, ImageHash):
            raise TypeError(f"Failed to set p_hash: expected str or int, got {type(value).__name__}")
        self._p_hash = value

    # ---------------- Brightness Quality ----------------
    @property
    def brightness_quality(self):
        """
        returns the local variable _brightness_quality
        :return: int or float, brightness_quality
        """
        return self._brightness_quality

    @brightness_quality.setter
    def brightness_quality(self, value):
        """
        sets the brightness_quality for the image
        :param value: int or float, brightness_quality
        :return: may  return Errors if wrong type or is not between 0 and 1
        """
        if value is not None:
            if not isinstance(value, (int, float)):
                raise TypeError(
                    f"Failed to set brightness_quality: expected int or float, got {type(value).__name__}"
                )
            if not (0 <= value <= 1):
                raise ValueError(
                    f"Failed to set brightness_quality: expected value between 0 and 1, got {value}"
                )
        self._brightness_quality = value

        # ---------------- Sharpness ----------------
    @property
    def sharpness(self):
        """
        returns the local variable _sharpness
        :return: int or float, sharpness
        """
        return self._sharpness

    @sharpness.setter
    def sharpness(self, value):
        """
        sets the sharpness for the image
        :param value: int or float, sharpness
        :return: may  return Errors if wrong type
        """
        if value is not None and not isinstance(value, (int, float)):
            raise TypeError(f"Failed to set sharpness: expected int or float, got {type(value).__name__}")
        self._sharpness = value

    # ---------------- Noise ----------------
    @property
    def noise(self):
        """
        returns the local variable _noise
        :return: int or float, noise
        """
        return self._noise

    @noise.setter
    def noise(self, value):
        """
        sets the noise for the image
        :param value: int or float, noise
        :return: may  return Errors if wrong type
        """
        if value is not None and not isinstance(value, (int, float)):
            raise TypeError(f"Failed to set noise: expected int or float, got {type(value).__name__}")
        self._noise = value

    # ---------------- Estimated Quality ----------------
    @property
    def est_quality(self):
        """
        returns the local variable _est_quality
        :return: int or float, est_quality
        """
        return self._est_quality

    @est_quality.setter
    def est_quality(self, value):
        """
        sets the est_quality for the image
        :param value: int or float, est_quality
        :return: may  return Errors if wrong type
        """
        if value is not None and not isinstance(value, (int, float)):
            raise TypeError(f"Failed to set est_quality: expected int or float, got {type(value).__name__}")
        self._est_quality = value

    # ---------------- Similar Images ----------------
    def add_similar(self, image_object):
        """
        adds similar images to the list similar in an image
        :param image_object: Image_obj -> (this class), image_object
        :return: may  return Errors if wrong type
        """
        if not isinstance(image_object, Image):
            raise TypeError(f"Failed to add similar: expected Image, got {type(image_object).__name__}")
        self._similar.append(image_object)

    @property
    def similar(self):
        """
        returns the list of similar images
        :return: list, similar
        """
        return self._similar

    # ---------------- Comparisons of Images ----------------
    def add_comparison(self, myString_comparison):
        """
        adds comparisons of images to the list comparison in an image if its not already in it
        :param myString_comparison: string, myString_comparison
        :return: may  return Errors if wrong type
        """
        if not isinstance(myString_comparison, str):
            raise TypeError(f"Failed to add comparison: expected str, got {type(myString_comparison).__name__}")
        if myString_comparison not in self.comparison:
            self.comparison.append(myString_comparison)

    @property
    def comparison(self):
        """
        returns the list of comparisons
        :return: list, comparison
        """
        return self._comparison


