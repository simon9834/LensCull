from pathlib import Path
from src.Exceptions.EmptyFolderException import EmptyFolderException
from src.Exceptions.UnsupportedFileTypeException import UnsupportedFileTypeException
from src.Exceptions.FolderNotFoundException import FolderNotFoundException
import os

class ImageLoader:
    """
    Class to load image paths from a folder
    """
    def __init__(self, SUPPORTED=None):
        if SUPPORTED is None:
            self.SUPPORTED = {".jpg", ".jpeg", ".png"}
        else:
            self.SUPPORTED = SUPPORTED


    def load_images_from_folder(self, folder_path):
        """
        Method to load image paths from a folder defined by path
        :return: returns either with an exception if something fails or with the list of paths to all photos
        """
        folder = Path(folder_path)
        print(self.SUPPORTED)
        try:
            if not folder.exists() or not folder.is_dir():
                raise FolderNotFoundException(f"folder {folder.name} does not exist")
            if not os.access(folder, os.R_OK):
                raise PermissionError(f"Permission at folder {folder.name} denied")
            files = list(folder.iterdir())
            if not files:
                raise EmptyFolderException(f"Folder {folder.name} is empty")
            image_paths = []
            for file in files:
                if file.is_file() and file.suffix.lower() in self.SUPPORTED:
                    try:
                        image_paths.append(file)
                    except Exception as e1:
                        raise Exception(f"Failed to load {file.name}. Why? Here's why: {e1}")
                else:
                    print(f"{file.name} is not supported")
            return image_paths
        except Exception as e:
            raise UnsupportedFileTypeException(f"Error at: {e.__class__.__name__}, Error: {e}")
