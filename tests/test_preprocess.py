import numpy as np
from src.preprocess import preprocess_image

def test_preprocess_shape():
    fake = np.zeros((100, 300, 3), dtype=np.uint8)
    t = preprocess_image(fake)
    assert tuple(t.shape) == (1, 1, 64, 256)