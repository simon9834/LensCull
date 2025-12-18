import unittest
from unittest.mock import patch, MagicMock
from src.processing.image_loader import ImageLoader
from src.Exceptions.EmptyFolderException import EmptyFolderException
from src.Exceptions.FolderNotFoundException import FolderNotFoundException


class TestImageLoader(unittest.TestCase):

    def setUp(self):
        self.loader = ImageLoader()

    # ------------------- Constructor -------------------

    def test_default_supported_extensions(self):
        self.assertIn(".jpg", self.loader.SUPPORTED)
        self.assertIn(".png", self.loader.SUPPORTED)
        self.assertIn(".jpeg", self.loader.SUPPORTED)

    def test_custom_supported_extensions(self):
        loader = ImageLoader(SUPPORTED={".bmp"})
        self.assertEqual(loader.SUPPORTED, {".bmp"})

    # ------------------- Folder does not exist -------------------

    @patch("src.processing.image_loader.Path.exists", return_value=False)
    @patch("src.processing.image_loader.Path.is_dir", return_value=False)
    def test_folder_not_found(self, mock_is_dir, mock_exists):
        with self.assertRaises(FolderNotFoundException):
            self.loader.load_images_from_folder("some/folder")

    # ------------------- No read permission -------------------

    @patch("src.processing.image_loader.Path.exists", return_value=True)
    @patch("src.processing.image_loader.Path.is_dir", return_value=True)
    @patch("src.processing.image_loader.os.access", return_value=False)
    def test_folder_no_permission(self, mock_access, mock_is_dir, mock_exists):
        with self.assertRaises(PermissionError):
            self.loader.load_images_from_folder("some/folder")

    # ------------------- Empty folder -------------------

    @patch("src.processing.image_loader.Path.exists", return_value=True)
    @patch("src.processing.image_loader.Path.is_dir", return_value=True)
    @patch("src.processing.image_loader.os.access", return_value=True)
    @patch("src.processing.image_loader.Path.iterdir", return_value=[])
    def test_empty_folder(self, mock_iterdir, mock_access, mock_is_dir, mock_exists):
        with self.assertRaises(EmptyFolderException):
            self.loader.load_images_from_folder("some/folder")

    # ------------------- Unsupported files ignored -------------------

    @patch("src.processing.image_loader.Path.exists", return_value=True)
    @patch("src.processing.image_loader.Path.is_dir", return_value=True)
    @patch("src.processing.image_loader.os.access", return_value=True)
    def test_unsupported_files_are_ignored(self, mock_access, mock_is_dir, mock_exists):

        txt_file = MagicMock()
        txt_file.is_file.return_value = True
        txt_file.suffix = ".txt"
        txt_file.name = "file1.txt"

        png_file = MagicMock()
        png_file.is_file.return_value = True
        png_file.suffix = ".png"
        png_file.name = "file2.png"

        with patch(
            "src.processing.image_loader.Path.iterdir",
            return_value=[txt_file, png_file]
        ):
            result = self.loader.load_images_from_folder("some/folder")
            self.assertEqual(result, [png_file])


if __name__ == "__main__":
    unittest.main()
