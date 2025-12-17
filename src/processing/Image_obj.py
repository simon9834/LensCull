class Image:
    def __init__(self, path, histogram=None, p_hash=None, brightness_quality=None,sharpness=None, noise=None, est_quality=None):
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
        return self._path

    @path.setter
    def path(self, value):
        if not isinstance(value, str):
            raise TypeError(f"Failed to set path: expected str, got {type(value).__name__}")
        if not value:
            raise ValueError("Failed to set path: path cannot be empty")
        self._path = value

    # ---------------- Histogram ----------------
    @property
    def histogram(self):
        return self._histogram

    @histogram.setter
    def histogram(self, value):
        if value is not None and not isinstance(value, (list, tuple)):
            raise TypeError(f"Failed to set histogram: expected list or tuple, got {type(value).__name__}")
        self._histogram = value

    # ---------------- Perceptual Hash ----------------
    @property
    def p_hash(self):
        return self._p_hash

    @p_hash.setter
    def p_hash(self, value):
        if value is not None and not isinstance(value, (str, int)):
            raise TypeError(f"Failed to set p_hash: expected str or int, got {type(value).__name__}")
        self._p_hash = value

    # ---------------- Brightness Quality ----------------
    @property
    def brightness_quality(self):
        return self._brightness_quality

    @brightness_quality.setter
    def brightness_quality(self, value):
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
        return self._sharpness

    @sharpness.setter
    def sharpness(self, value):
        if value is not None and not isinstance(value, (int, float)):
            raise TypeError(f"Failed to set sharpness: expected int or float, got {type(value).__name__}")
        self._sharpness = value

    # ---------------- Noise ----------------
    @property
    def noise(self):
        return self._noise

    @noise.setter
    def noise(self, value):
        if value is not None and not isinstance(value, (int, float)):
            raise TypeError(f"Failed to set noise: expected int or float, got {type(value).__name__}")
        self._noise = value

    # ---------------- Estimated Quality ----------------
    @property
    def est_quality(self):
        return self._est_quality

    @est_quality.setter
    def est_quality(self, value):
        if value is not None and not isinstance(value, (int, float)):
            raise TypeError(f"Failed to set est_quality: expected int or float, got {type(value).__name__}")
        self._est_quality = value

    # ---------------- Similar Images ----------------
    def add_similar(self, image_object):
        if not isinstance(image_object, Image):
            raise TypeError(f"Failed to add similar: expected Image, got {type(image_object).__name__}")
        self._similar.append(image_object)

    @property
    def similar(self):
        return self._similar

    # ---------------- Comparisons of Images ----------------
    def add_comparison(self, myString):
        if not isinstance(myString, str):
            raise TypeError(f"Failed to add comparison: expected str, got {type(myString).__name__}")
        self._comparison.append(myString)

    @property
    def comparison(self):
        return self._comparison


