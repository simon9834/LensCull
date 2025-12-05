import time
from pathlib import Path
from src.processing.image_loader import ImageLoader
from src.processing.parallel import ParallelProcessor

def main():
    """
    method main to run the program
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
        results = processor.run()

        for comparison in results:
            print(comparison)

        end = time.time()
        print(f"Parallel processing finished in {end - start:.2f}s")

    except Exception as e:
        print(e)

if __name__ == "__main__":
    main()
