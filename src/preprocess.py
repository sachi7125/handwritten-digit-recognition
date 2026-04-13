import cv2
import numpy as np
import torch
from torchvision import transforms

transform = transforms.Compose([
    transforms.ToPILImage(),
    transforms.Resize((64, 256)),
    transforms.ToTensor(),
    transforms.Normalize((0.5,), (0.5,))
])

def preprocess_image(img_bgr: np.ndarray) -> torch.Tensor:
    gray = cv2.cvtColor(img_bgr, cv2.COLOR_BGR2GRAY)
    tensor = transform(gray).unsqueeze(0)
    return tensor