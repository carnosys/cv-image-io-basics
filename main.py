import cv2 as cv
from pathlib import Path
import numpy as np


def load_image(path: Path, image_name: str) -> np.ndarray:
    img = cv.imread(str(path / image_name))
    assert img is not None, "image could not be read."
    return img


def process_image(img: np.ndarray):
    # basic information about the image
    size = img.size
    print(f"size of the image is: {size}")

    height, width, channels = img.shape
    print(f"The image has height: {height}, width: {width}, channels: {channels}")

    dtype = img.dtype
    print(f"data type of image pixels is: {dtype}")

    # conversion step
    img_grayscale = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
    img_rgb = cv.cvtColor(img, cv.COLOR_BGR2RGB)

    return img_grayscale, img_rgb



def main():
    input_folder = Path("images")
    output_folder = Path("outputs")
    output_folder.mkdir(exist_ok=True)

    img = load_image(input_folder, "image.jpeg")
    img_grayscale, img_rgb = process_image(img)

    cv.imshow("grayscale version", img_grayscale)
    cv.waitKey(0)
    cv.imshow("rgb version", img_rgb)
    cv.waitKey(0)
    cv.destroyAllWindows()

    cv.imwrite(str(output_folder / "grayscale_version.jpeg"), img_grayscale)
    cv.imwrite(str(output_folder / "rgb_version.jpeg"), img_rgb)


if __name__ == "__main__":
    main()

