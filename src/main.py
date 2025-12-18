import time
from pathlib import Path
from src.processing.image_loader import ImageLoader
from src.processing.parallel import ParallelProcessor
import src.processing.log_inicialization # noqa
import logging

def main():
    """
    method to run the program
    :return: None
    """
    try:
        folder = Path("../data").resolve()
        start = time.time()

        image_loader = ImageLoader()
        image_paths = image_loader.load_images_from_folder(folder)
        print(f"Loaded {len(image_paths)} images.")
        print("\nRunning parallel similarity comparison...")

        processor = ParallelProcessor(image_paths)
        images = processor.run()

        for img in images:
            for comp in img.comparison:
                print(comp)
            print(f"image: {Path(img.path).name}, score: {img.est_quality}")
        end = time.time()
        print(f"Parallel processing finished in {end - start:.2f}s")

    except Exception as e:
        logging.exception(e)
        print(e)

if __name__ == "__main__":
    main()
