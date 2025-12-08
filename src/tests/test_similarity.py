import unittest
import numpy as np
import src.processing.similarity as s
from src.Exceptions.NotImageException import NotImageException
from src.processing.Image_obj import Image


class TestSimilarity(unittest.TestCase):
    def test_compute_similarity_raises_non_path(self):
        with self.assertRaises(Exception):
            s.compute_similarity(123)

    def test_compute_similarity_invalid_path(self):
        with self.assertRaises(Exception):
            s.compute_similarity("not_a_real_file.png")

    def test_compute_similarity_returns_image_obj(self):
        pass

    def test_compare_hashes_images_not_list(self):
        with self.assertRaises(TypeError):
            s.compare_hashes(123)

    def test_compare_hashes_wrong_items_in_list(self):
        with self.assertRaises(NotImageException):
            s.compare_hashes([1, 2, 3])

    def test_compare_hashes_empty_list(self):
        with self.assertRaises(IndexError):
            s.compare_hashes([])

    def test_compare_hashes_single_element(self):
        img = Image("x", 1, np.array([1]))
        with self.assertRaises(IndexError):
            s.compare_hashes([img])

    def test_compare_hashes_phash_above_threshold(self):
        img1 = Image("a", 100, np.array([1]))
        img2 = Image("b", 1, np.array([1]))
        res = s.compare_hashes([img1, img2])
        self.assertEqual(res, ["a <-> b: None - 1"])

    def test_compare_hashes_histogram_above_threshold(self):
        img1 = Image("a", 1, 100)
        img2 = Image("b", 2, 1)
        res = s.compare_hashes([img1, img2])
        self.assertEqual(res, ["a <-> b: 1 - None"])

    def test_compare_hashes_histogram_below_threshold(self):
        img1 = Image("a", 1, 0)
        img2 = Image("b", 2, 1)
        with self.assertRaises(ZeroDivisionError):
            s.compare_hashes([img1, img2])

    def test_compare_hashes_output_string_format(self):
        img1 = Image("123", 1, np.array([1.0]))
        img2 = Image("234", 2, np.array([2.0]))
        res = s.compare_hashes([img1, img2])
        self.assertEqual(res, ["123 <-> 234: 1 - None"])