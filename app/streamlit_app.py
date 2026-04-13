import streamlit as st
import cv2
import numpy as np

from src.model_crnn import load_crnn
from src.predict import predict_crnn

st.title("Handwritten Digit Recognition")

@st.cache_resource
def get_model():
    return load_crnn("models/crnn_best.pth")

model = get_model()

file = st.file_uploader("Upload an image", type=["png", "jpg", "jpeg"])

if file:
    arr = np.frombuffer(file.read(), np.uint8)
    img = cv2.imdecode(arr, cv2.IMREAD_COLOR)

    st.image(img[:, :, ::-1], caption="Input")

    pred = predict_crnn(model, img)

    st.success(f"Prediction: {pred}")