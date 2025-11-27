class FolderNotFoundException(Exception):
    def __init__(self, message="Folder does not exist"):
        self.message = message
        super().__init__(self.message)