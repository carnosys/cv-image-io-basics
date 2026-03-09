# CV Image I/O Basics

Small OpenCV practice project for loading an image, inspecting its metadata, converting it to grayscale and RGB, previewing the results, and saving the processed outputs.

## What the project does

The script in `main.py`:

- loads `images/image.jpeg`
- prints basic image metadata
- converts the image from BGR to grayscale
- converts the image from BGR to RGB
- displays both processed images in OpenCV windows
- writes the processed images to `outputs/`

## Project structure

```text
.
├── images/
│   └── image.jpeg
├── main.py
├── tests.py
└── README.md
```

## Requirements

- Python 3
- `opencv-python`
- `numpy`
- `pytest`

## Install dependencies

```bash
python -m venv .venv
source .venv/bin/activate
pip install opencv-python numpy pytest
```

## Run the project

```bash
python main.py
```

When the script runs, it will:

1. read `images/image.jpeg`
2. print the image size, shape, and pixel data type
3. open preview windows for the grayscale and RGB versions
4. save:
   - `outputs/grayscale_version.jpeg`
   - `outputs/rgb_version.jpeg`

## Run tests

```bash
pytest tests.py
```

The tests verify that:

- grayscale conversion returns a 2D image
- RGB conversion preserves the 3-channel shape
- channel conversion behaves as expected for a simple test pixel

## Notes

- `cv.imread()` loads color images in BGR order, which is why the script explicitly converts to RGB.
- `cv.imshow()` requires a graphical environment. If you run this in a headless terminal or remote environment without display support, the preview windows will not open.
- The script creates the `outputs/` directory automatically if it does not already exist.
