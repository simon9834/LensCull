class EmptyFolderException(Exception):
    def __init__(self, message="Folder is empty"):
        self.message = message
        super().__init__(self.message)