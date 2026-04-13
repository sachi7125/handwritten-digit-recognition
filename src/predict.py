import torch
from .preprocess import preprocess_image
from .decode import ctc_greedy_decode

def predict_crnn(model, img_bgr, device="cpu"):
    x = preprocess_image(img_bgr).to(device)
    
    with torch.no_grad():
        logits = model(x)
    
    return ctc_greedy_decode(logits)