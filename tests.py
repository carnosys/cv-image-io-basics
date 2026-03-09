import pytest
import cv2
import numpy as np
from main import process_image

def test_process_image_conversion_shapes():
    dummy_image = np.random.randint(0,255,(100,100,3), dtype = np.uint8)
    gray_img, rgb_img = process_image(dummy_image)
    
    assert gray_img.shape == (100,100)
    assert rgb_img.shape == (100,100,3)

def test_process_image_conversion_values():
    dummy_image = np.zeros((100,100,3), dtype=np.uint8)
    dummy_image[0,0,2] = 255
    gray_img, rgb_img = process_image(dummy_image)
    

    assert rgb_img[0,0,0] == 255
    assert gray_img[0,0]>0

