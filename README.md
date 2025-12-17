# Image Similarity Checker

A Python tool to compute similarity between images

## Requirements

- Python 3.8 or higher
- Packages:
  - `Pillow`
  - `numpy`

## How to run
Configure local interpreter (if needed)

Install the required packages using pip:
```bash
pip install -r requirements.txt
```

Insert photos into the data file that can be found at:
```bash
LensCull/data
```

## LensCull Project Structure

```
LensCull/
│
├── data/
│   # Folder to store input images.
│
├── notebooks/
│   └── similarity_test.py #testing on different devices
│
├── src/
│   ├── Exceptions/  # Custom exception classes.
│   └── processing/
│       ├── __init__.py  # Marks the folder as a Python package.
│       ├── image_loader.py  # Loads images from data folder.
│       ├── Image_obj.py  # Serves as an object to define an Image.
│       ├── parallel.py  # Implements parallel processing.
│       ├── quality.py  # Quality assessment functions.
│       └── similarity.py  # Image similarity calculations with p_hashes and histograms.
│
├── tests/
│   ├── __init__.py  # Marks the folder as a Python package.
│   ├── test_image_loader.py  # Unit tests for image loader.
│   ├── test_quality.py  # Unit tests for quality module.
│   └── test_similarity.py  # Unit tests for similarity module.
│
├── web/
│   ├── templates/
│   │   └── index.html  # HTML template for the web interface.
│   ├── __init__.py  # Marks the folder as a Python package.
│   └── server.py  # Web server code.
│
├── __init__.py  # Root package initializer.
├── app.log  # Log file for application events.
├── config.py  # Configuration settings.
├── main.py  # Main entry point for the application.
├── LICENCE  # Project license.
├── pyproject.toml  # Python project configuration.
├── README.md  # Project README.
└── requirements.txt  # Python dependencies.
```

