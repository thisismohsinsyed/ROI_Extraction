import streamlit as st
from PIL import Image
import cv2
import numpy as np
# Make sure ROI_Extraction.py is in the same directory or the path is adjusted accordingly
from ROI_Extraction import extract_roi_from_image_array

st.title("ROI Extraction App")

uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "jpeg", "png"])
if uploaded_file is not None:
    image = Image.open(uploaded_file).convert("RGB")
    image_array = np.array(image)
    
    # Convert RGB to BGR for OpenCV
    image_array = cv2.cvtColor(image_array, cv2.COLOR_RGB2BGR)
    
    # Perform ROI extraction
    image_with_contour, roi = extract_roi_from_image_array(image_array)
    
    # Display the results
    if image_with_contour is not None:
        st.image(image_with_contour, caption='Detected Inner Square From Input Image', use_column_width=True)
    if roi is not None:
        st.image(roi, caption='Detected Region Of Interest', use_column_width=True)