class Image:
    def __init__(self, path, p_hash, histogram):
        self.path = path
        self.histogram = histogram
        self.p_hash = p_hash
        self.similar = []