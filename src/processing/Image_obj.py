class Image:
    def __init__(self, path, p_hash, histogram):
        """
        this method defines the variables for the object of Image
        :param path: the path of the image
        :param p_hash: the calculated value of p_hash
        :param histogram: the calculated value of histogram
        """
        self.path = path
        self.histogram = histogram
        self.p_hash = p_hash
        self.similar = []