class NotImageException(Exception):
    def __init__(self, message="The object that is passed is not an image"):
        self.message = message
        super().__init__(self.message)