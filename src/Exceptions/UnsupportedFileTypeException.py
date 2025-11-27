class UnsupportedFileTypeException(Exception):
    def __init__(self, message="File type not supported"):
        self.message = message
        super().__init__(self.message)