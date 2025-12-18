import unittest
from unittest.mock import patch
import numpy as np
import src.processing.quality as quality


class DummyImage:
    def __init__(self, path="dummy.jpg"):
        self.path = path
        self.brightness_quality = None
        self.sharpness = None
        self.noise = None
        self.est_quality = None


class TestBrightnessScore(unittest.TestCase):
    def test_black_image_returns_zero(self):
        img = np.zeros((100, 100), dtype=np.uint8)
        score = quality.brightness_score(img)
        self.assertEqual(score, 0.0)

    def test_white_image_returns_one(self):
        img = np.full((100, 100), 255, dtype=np.uint8)
        score = quality.brightness_score(img)
        self.assertEqual(score, 1.0)

    def test_mid_gray_image(self):
        img = np.full((100, 100), 128, dtype=np.uint8)
        score = quality.brightness_score(img)
        self.assertAlmostEqual(score, 128 / 255, places=5)


class TestSharpnessScore(unittest.TestCase):
    def test_uniform_image_is_blurry(self):
        img = np.full((100, 100), 128, dtype=np.uint8)
        score = quality.sharpness_score(img)
        self.assertLess(score, 100)

    def test_high_frequency_image_is_sharp(self):
        img = np.zeros((100, 100), dtype=np.uint8)
        img[::2, ::2] = 255
        score = quality.sharpness_score(img)
        self.assertGreater(score, 100)


class TestNoiseScore(unittest.TestCase):
    def test_no_noise_image(self):
        img = np.full((100, 100), 128, dtype=np.uint8)
        score = quality.noise_score(img)
        self.assertLess(score, 0.01)

    def test_noisy_image(self):
        rng = np.random.default_rng(42)
        img = rng.integers(0, 256, size=(100, 100), dtype=np.uint8)
        score = quality.noise_score(img)
        self.assertGreater(score, 0.05)


class TestCalculateQuality(unittest.TestCase):
    @patch("src.processing.quality.cv2.resize")
    @patch("src.processing.quality.cv2.imread")
    def test_calculate_quality_sets_all_fields(self, mock_imread, mock_resize):
        img_array = np.full((600, 600), 128, dtype=np.uint8)
        mock_imread.return_value = img_array
        mock_resize.return_value = img_array

        img_obj = DummyImage()
        result = quality.calculate_quality(img_obj)

        self.assertIs(result, img_obj)
        self.assertIsNotNone(img_obj.brightness_quality)
        self.assertIsNotNone(img_obj.sharpness)
        self.assertIsNotNone(img_obj.noise)
        self.assertIsNotNone(img_obj.est_quality)

    @patch("src.processing.quality.cv2.resize")
    @patch("src.processing.quality.cv2.imread")
    def test_est_quality_bounds(self, mock_imread, mock_resize):
        img_array = np.zeros((600, 600), dtype=np.uint8)
        mock_imread.return_value = img_array
        mock_resize.return_value = img_array

        img_obj = DummyImage()
        quality.calculate_quality(img_obj)

        self.assertGreaterEqual(img_obj.est_quality, 0)
        self.assertLessEqual(img_obj.est_quality, 100)

    @patch("src.processing.quality.cv2.resize")
    @patch("src.processing.quality.cv2.imread")
    def test_sharpness_normalization_clipping_low(self, mock_imread, mock_resize):
        img_array = np.full((600, 600), 128, dtype=np.uint8)
        mock_imread.return_value = img_array
        mock_resize.return_value = img_array

        img_obj = DummyImage()
        quality.calculate_quality(img_obj)

        self.assertGreaterEqual(img_obj.sharpness, 0.0)

    @patch("src.processing.quality.cv2.resize")
    @patch("src.processing.quality.cv2.imread")
    def test_sharpness_normalization_clipping_high(self, mock_imread, mock_resize):
        img_array = np.zeros((600, 600), dtype=np.uint8)
        img_array[::2, ::2] = 255
        mock_imread.return_value = img_array
        mock_resize.return_value = img_array

        img_obj = DummyImage()
        quality.calculate_quality(img_obj)

        self.assertLessEqual(img_obj.sharpness, 1.0)

    @patch("src.processing.quality.cv2.resize")
    @patch("src.processing.quality.cv2.imread")
    def test_high_sharpness_produces_higher_quality(self, mock_imread, mock_resize):
        blurry = np.full((600, 600), 128, dtype=np.uint8)
        sharp = np.zeros((600, 600), dtype=np.uint8)
        sharp[::2, ::2] = 255

        mock_resize.side_effect = [blurry, sharp]
        mock_imread.side_effect = [blurry, sharp]

        img_blurry = DummyImage("blurry.jpg")
        img_sharp = DummyImage("sharp.jpg")

        quality.calculate_quality(img_blurry)
        quality.calculate_quality(img_sharp)

        self.assertGreater(img_sharp.est_quality, img_blurry.est_quality)


if __name__ == "__main__":
    unittest.main()
