from multiprocessing import Pool
from src.processing.similarity import compute_similarity, compare_hashes
from src.processing import Image_obj
from src.processing.quality import calculate_quality
import os, random


class ParallelProcessor:
    """
    Class for parallel image similarity calculation
    """
    def __init__(self, paths):
        """
        method for initialization the paths list as local variable
        :param paths: list of paths to the photos
        """
        if not isinstance(paths, list):
            raise TypeError("paths must be a list")
        if len(paths) < 2:
            raise ValueError("paths must have at least 2 elements")
        self.paths = paths
        self.workers = self.estimate_processes(self.estimate_avg_size_mb())

    def run(self):
        """
           Method for parallel image similarity calculation and quality estimation
           :return: returns with the list of calculated similarities with each photo
        """
        images = [Image_obj.Image(str(path)) for path in self.paths]

        with Pool(processes=self.workers) as pool:
            images = pool.map(compute_similarity, images)
            images = pool.map(calculate_quality, images)
        compare_hashes(images)
        return images

    def estimate_processes(self, avg_mb_size):
        """
        Method for estimating the best number of cpus to use in a pc
        :param avg_mb_size: average size of an image
        :return: returns either with an exception if something fails or
        with the number of processes that should be optimally used
        """
        cpu_count = os.cpu_count()
        if not avg_mb_size:
            raise ValueError("avg_mb_size cannot be None")

        K_MB = 0.2  # compute scaling per MB
        WORK_PER_CPU = 1.5  # recommended load per CPU

        work_unit = avg_mb_size * K_MB
        total_work = work_unit * len(self.paths)

        processes = min(cpu_count, max(1, int(total_work / WORK_PER_CPU)))
        return processes

    def estimate_avg_size_mb(self, sample_size=10):
        """
        Method for estimating the average size of an image based on 10 random image sizes
        :param sample_size: the number of random images to compare sizes form
        :return: returns either with an exception if something fails or average size of an image in MB
        """
        if not self.paths:
            raise ValueError("No paths")

        if len(self.paths) <= sample_size:
            sample = self.paths
        else:
            sample = random.sample(self.paths, sample_size)
        total = 0

        for p in sample:
            total += os.path.getsize(p)

        avg_bytes = total / len(sample)
        return avg_bytes / (1024 * 1024)
