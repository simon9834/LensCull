import unittest
from unittest.mock import patch, MagicMock
from src.processing.image_loader import ImageLoader
from src.Exceptions.EmptyFolderException import EmptyFolderException
from src.Exceptions.FolderNotFoundException import FolderNotFoundException

class TestImageLoader(unittest.TestCase):

    def setUp(self):
        self.loader = ImageLoader()

    # ------------------- Test constructor -------------------
    def test_default_supported_extensions(self):
        self.assertIn(".jpg", self.loader.SUPPORTED)
        self.assertIn(".png", self.loader.SUPPORTED)
        self.assertIn(".jpeg", self.loader.SUPPORTED)

    def test_custom_supported_extensions(self):
        loader = ImageLoader(SUPPORTED={".bmp"})
        self.assertIn(".bmp", loader.SUPPORTED)
        self.assertNotIn(".jpg", loader.SUPPORTED)

    # ------------------- Test folder does not exist -------------------
    @patch("pathlib.Path.is_dir", return_value=False)
    @patch("pathlib.Path.exists", return_value=False)
    def test_folder_not_found(self, mock_exists, mock_is_dir):
        with self.assertRaises(FolderNotFoundException):
            self.loader.load_images_from_folder("some/folder")

    # ------------------- Test folder not readable -------------------
    @patch("pathlib.Path.is_dir", return_value=True)
    @patch("pathlib.Path.exists", return_value=True)
    @patch("os.access", return_value=False)
    def test_folder_no_permission(self, mock_access, mock_exists, mock_is_dir):
        with self.assertRaises(PermissionError):
            self.loader.load_images_from_folder("some/folder")

    # ------------------- Test empty folder -------------------
    @patch("pathlib.Path.is_dir", return_value=True)
    @patch("pathlib.Path.exists", return_value=True)
    @patch("os.access", return_value=True)
    @patch("pathlib.Path.iterdir", return_value=[])
    def test_empty_folder(self, mock_iterdir, mock_access, mock_exists, mock_is_dir):
        with self.assertRaises(EmptyFolderException):
            self.loader.load_images_from_folder("some/folder")

    # ------------------- Test unsupported files are ignored -------------------
    @patch("pathlib.Path.is_dir", return_value=True)
    @patch("pathlib.Path.exists", return_value=True)
    @patch("os.access", return_value=True)
    def test_unsupported_files_are_ignored(self, mock_access, mock_exists, mock_is_dir):
        mock_file1 = MagicMock()
        mock_file1.is_file.return_value = True
        mock_file1.suffix = ".txt"
        mock_file1.name = "file1.txt"

        mock_file2 = MagicMock()
        mock_file2.is_file.return_value = True
        mock_file2.suffix = ".png"
        mock_file2.name = "file2.png"

        with patch("pathlib.Path.iterdir", return_value=[mock_file1, mock_file2]):
            result = self.loader.load_images_from_folder("some/folder")
            self.assertEqual(result, [mock_file2])

if __name__ == "__main__":
    unittest.main()
