import unittest
import numpy as np
from imagehash import ImageHash
from src.processing.Image_obj import Image


class TestImage(unittest.TestCase):

    def setUp(self):
        self.img = Image(path="dummy_path.jpg")

    # ---------------- Path Tests ----------------
    def test_path_valid(self):
        self.img.path = "new_path.jpg"
        self.assertEqual(self.img.path, "new_path.jpg")

    def test_path_type_error(self):
        with self.assertRaises(TypeError):
            self.img.path = 123  # not str

    def test_path_value_error(self):
        with self.assertRaises(ValueError):
            self.img.path = ""  # empty string

    # ---------------- Histogram Tests ----------------
    def test_histogram_valid(self):
        arr = np.array([1, 2, 3])
        self.img.histogram = arr
        self.assertTrue(np.array_equal(self.img.histogram, arr))

    def test_histogram_type_error(self):
        with self.assertRaises(TypeError):
            self.img.histogram = [1, 2, 3]  # list instead of ndarray

    # ---------------- p_hash Tests ----------------
    def test_p_hash_valid(self):
        # noinspection PyTypeChecker
        h = ImageHash(np.array([1, 0, 1, 0]))
        self.img.p_hash = h
        self.assertEqual(self.img.p_hash, h)

    def test_p_hash_type_error(self):
        with self.assertRaises(TypeError):
            self.img.p_hash = "hash_string"  # must be ImageHash

    # ---------------- Brightness Quality Tests ----------------
    def test_brightness_quality_valid(self):
        self.img.brightness_quality = 0.5
        self.assertEqual(self.img.brightness_quality, 0.5)

    def test_brightness_quality_type_error(self):
        with self.assertRaises(TypeError):
            self.img.brightness_quality = "high"

    def test_brightness_quality_value_error_low(self):
        with self.assertRaises(ValueError):
            self.img.brightness_quality = -0.1

    def test_brightness_quality_value_error_high(self):
        with self.assertRaises(ValueError):
            self.img.brightness_quality = 1.1

    # ---------------- Sharpness Tests ----------------
    def test_sharpness_valid(self):
        self.img.sharpness = 150.0
        self.assertEqual(self.img.sharpness, 150.0)

    def test_sharpness_type_error(self):
        with self.assertRaises(TypeError):
            self.img.sharpness = "sharp"

    # ---------------- Noise Tests ----------------
    def test_noise_valid(self):
        self.img.noise = 0.25
        self.assertEqual(self.img.noise, 0.25)

    def test_noise_type_error(self):
        with self.assertRaises(TypeError):
            self.img.noise = "noisy"

    # ---------------- Estimated Quality Tests ----------------
    def test_est_quality_valid(self):
        self.img.est_quality = 75
        self.assertEqual(self.img.est_quality, 75)

    def test_est_quality_type_error(self):
        with self.assertRaises(TypeError):
            self.img.est_quality = "good"

    # ---------------- Similar Images Tests ----------------
    def test_add_similar_valid(self):
        other = Image(path="other.jpg")
        self.img.add_similar(other)
        self.assertIn(other, self.img.similar)

    def test_add_similar_type_error(self):
        with self.assertRaises(TypeError):
            self.img.add_similar("not_an_image")

    # ---------------- Comparison Tests ----------------
    def test_add_comparison_valid(self):
        self.img.add_comparison("Compared successfully")
        self.assertIn("Compared successfully", self.img.comparison)

    def test_add_comparison_type_error(self):
        with self.assertRaises(TypeError):
            self.img.add_comparison(12345)


if __name__ == "__main__":
    unittest.main()
